from utils.libraries import st
from utils.explore_page import show_explore_page
from utils.model_page import compare_model_page
from utils.predict_page import show_predict_page

'''
import os
import sys
import random
import argparse


parser = argparse.ArgumentParser(description='pull in 3 parameters: feature, target, and models')

parser.add_argument('features', type = str, require = True, help = "github path to the feature category")
parser.add_argument('target', type = str, require = True, help = "target dataset")
parser.add_argument('models', type = str, require = True, help = "maching leanring model type")
args = parser.parse_args()

'''
page = st.sidebar.selectbox("Explore Or Predict Or Else", ("Understanding the Data","Compare Models","Predict"))

if page == "Understanding the Data":
    show_explore_page()
elif page == "Compare Models":
    compare_model_page()
elif page == "Predict":
    show_predict_page()
