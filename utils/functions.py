from utils.libraries import *
import streamlit as st
import requests
import base64
import time
import json
import random

# Creating a Dataframe with word-vectors in TF-IDF form and Target values

github_token = st.secrets["GITHUB_TOKEN"]

def final_df(df, is_train, vectorizer, column):

    # TF-IDF form
    if is_train:
        x = vectorizer.fit_transform(df.loc[:,column])
    else:
        x = vectorizer.transform(df.loc[:,column])

    # TF-IDF form to Dataframe
    temp = pd.DataFrame(x.toarray(), columns=vectorizer.get_feature_names_out())

    # Droping the text column
    df.drop(df.loc[:,column].name, axis = 1, inplace=True)

    # Returning TF-IDF form with target
    return pd.concat([temp, df], axis=1)


# Training the model with various combination and returns y_test and y_pred

def train_model(df, input, target, test_size, over_sample, vectorizer, model):

    X = df.drop(target, axis=1)
    y = df[target]
    print("Splitted Data into X and Y.")

    X_train, x_test, Y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    print("Splitted Data into Train and Test.")
    
    # Training Preprocessing
    X_train = final_df(X_train, True, vectorizer, input)
    X_train.dropna(inplace=True)
    print("Vectorized Training Data.")

    if over_sample:
        sm = SMOTE(random_state = 2)
        X_train, Y_train = sm.fit_resample(X_train, Y_train.ravel())
        print("Oversampling Done for Training Data.")

    # Testing Preprocessing
    x_test = final_df(x_test, False, vectorizer, input)
    x_test.dropna(inplace=True)
    print("Vectorized Testing Data.")

    # fitting the model
    model = model.fit(X_train, Y_train)
    print("Model Fitted Successfully.")

    # calculating y_pred
    y_pred = model.predict(x_test)
    y_pred_prob = model.predict_proba(x_test)

    return model, x_test, y_test, y_pred_prob

def evaluate(y_test, y_pred, y_pred_prob):
    roc_auc = round(roc_auc_score(y_test, y_pred_prob[:, 1]), 2)

    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob[:,1], pos_label=1)
    
    # calculate the g-mean for each threshold
    gmeans = sqrt(tpr * (1-fpr))
    
    # locate the index of the largest g-mean
    ix = argmax(gmeans)

    y_pred = (y_pred > thresholds[ix])

    accuracy = accuracy_score(y_test, y_pred)

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**ROC-AUC Score** \t\t: {roc_auc*100} %")
        st.write('**Best Threshold** \t\t: %.3f' % (thresholds[ix]))
    with col2:
        st.write('**G-Mean** \t\t\t: %.3f' % (gmeans[ix]))
        st.write(f"**Model Accuracy** : {round(accuracy,2,)*100} %")

    st.write("**Classification Report:**")
    st.text(classification_report(y_test, y_pred))


def get_cf_report_dict(y_test, y_pred):
    cf_report_dict = classification_report(y_test, y_pred, output_dict = True)
    return cf_report_dict


def trainer(df, test_size, over_sample, vectorizer, model):
    model, x_test, y_test, y_pred_prob = train_model(
        df=df, 
        input='text', 
        target='fraudulent', 
        test_size=test_size,
        over_sample=over_sample, 
        vectorizer=vectorizer, 
        model=model)

    y_pred = model.predict(x_test)
    y_pred_prob = model.predict_proba(x_test)

    evaluate(y_test, y_pred, y_pred_prob)
    
    #get classification report variable
    cf_report_dict = get_cf_report_dict(y_test,y_pred)

     #generate json file
    report_json_str = json.dumps(cf_report_dict)

    report_bytes = report_json_str.encode('utf-8')
    report_base64 = base64.b64encode(report_bytes).decode('utf-8')

    #Generate the name of the file
    model_name = str(model.__class__.__name__)
    random_int = random.randint(1, 1000000)

    #defne the repo route
    url = f"https://api.github.com/repos/Ultracatx/RealityStream/contents/output/user_generated_json/{model_name}_{random_int}"
    headers = {
            "Authorization": f"token {github_token}",
            #"Accept": "application/vnd.github.v3+json",
        }
    data = {
        "message": "testing json file upload",
        "content": report_base64,
        "branch": "interaction_test",
           }
    
    #determine upload status
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201:
        st.success("Report successfully uploaded to GitHub.")
    else:
        st.error(f"Failed to upload: {response.content}")

    #create a download button for user to download the json file
    st.download_button(
    label ="Download Classification Report as JSON",
    data = report_json_str,
    file_name ="classification_report.json",
    mime = "application/json")
    


nlp = spacy.load('en_core_web_sm')

# Text Preprocessing with varoius combination

def spacy_process(text):
  # Converts to lowercase
  text = text.strip().lower()

  # passing text to spacy's nlp object
  doc = nlp(text)
    
  # Lemmatization
  lemma_list = []
  for token in doc:
    lemma_list.append(token.lemma_)
  
  # Filter the stopword
  filtered_sentence =[] 
  for word in lemma_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
      filtered_sentence.append(word)
    
  # Remove punctuation
  punctuations="?:!.,;$\'-_"
  for word in filtered_sentence:
    if word in punctuations:
      filtered_sentence.remove(word)

  return " ".join(filtered_sentence)

# For Loading the Pickle File
def load_model():
    with open('output/jobs/saved/notebook_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

'''
def save_report_to_github(image_content, filename, repo_name, path_in_repo, commit_message, github_token):
    url = f"https://api.github.com/repos/{repo_name}/contents/{path_in_repo}/{filename}"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "message": commit_message,
        "content": base64.b64encode(image_content).decode('utf-8'),
        "branch": "main",
    }
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201:
        st.success("Image successfully uploaded to GitHub.")
    else:
        st.error(f"Failed to upload image: {response.content}") 
'''