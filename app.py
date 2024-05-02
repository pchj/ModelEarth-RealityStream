from utils.libraries import st
from utils.explore_page import show_explore_page
from utils.model_page import compare_model_page
from utils.predict_page import show_predict_page

# Let's make the incoming parameters optional. Write them to the UI for now.
# We could select dropdowns based on the incoming args.
# index= is used to select dropdowns below.
# Let's match the short arg "bees" to a name "Honey Bees" rather than hardcoing an index value.
# The name matching could reside in a .csv file that defines a long list of data sources.

# import os
# import sys
# import random
# import argparse

# parser = argparse.ArgumentParser(description='Pull in 3 parameters: feature, target, and models')

# parser.add_argument('features', type=str, help="github path to the feature category")
# sort_order_choices = ('up', 'down', 'random')
# parser.add_argument('targets', type=str, help="target dataset")
# parser.add_argument('models', type=str, help="matching learning model type")

# try:
#     args = parser.parse_args()
# except SystemExit as e:
#     # This exception will be raised if --help or invalid command line arguments
#     # are used. Currently streamlit prevents the program from exiting normally
#     # so we have to do a hard exit.
#     os._exit(e.code)

#st.write("[Model.Earth](https://model.earth)")

features = st.sidebar.selectbox("Features", ("Local Industries", "Local Places", "Local Products", "Job Descriptions", "Brain Voxels"), index=3)
targets = st.sidebar.selectbox("Target", ("Honey Bees", "Job Growth", "Wage Growth", "High Wages", "Real Job Listings", "Tree Canopy", "Eye Blinks"), index=4)
models = st.sidebar.selectbox("Model", ("Location Forest", "Random Forest", "Random Bits Forest", "Logistic Regression ", "Support Vector Machines", "XGBoost Gradient Boosted Trees", "MLP Neural Network"), index=3)
page = st.sidebar.selectbox("Explore or Predict", ("Understanding the Data","Compare Models","Predict"))

if page == "Understanding the Data":
    show_explore_page()
elif page == "Compare Models":
    compare_model_page()
elif page == "Predict":
    show_predict_page()

