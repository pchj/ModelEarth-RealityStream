import pandas as pd
from sklearn.model_selection import train_test_split
import os

def check_directory(directory_path):
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Directory '{directory_path}' created successfully.")
        except OSError as e:
            print(f"Error creating directory '{directory_path}': {e}")
    else:
        print(f"Directory '{directory_path}' already exists.")
    return directory_path

dataset_name = "blinks"
target_name = "y"
df = pd.read_csv(f'../../input/{dataset_name}/targets/{dataset_name}-targets.csv')

df = df.dropna()
X = df.drop(target_name, axis=1)
y = df[target_name]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

check_directory(f"../../output/{dataset_name}/training")
check_directory(f"../../output/{dataset_name}/saved")

train_df = pd.concat([X_train, y_train], axis=1)
train_df.rename(columns={train_df.columns[-1]: 'target'}, inplace=True)
train_df.to_csv(f'../../output/{dataset_name}/training/{dataset_name}-train.csv', index=False)

test_df = pd.concat([X_test, y_test], axis=1)
test_df.rename(columns={test_df.columns[-1]: 'target'}, inplace=True)
test_df.to_csv(f'../../output/{dataset_name}/training/{dataset_name}-test.csv', index=False)