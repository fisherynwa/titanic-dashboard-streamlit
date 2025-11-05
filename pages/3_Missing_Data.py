import pandas as pd
import streamlit as st
import seaborn as sns

from helper_functions.meta_data import load_data 

# Set page configuration
st.set_page_config(page_title="⚠️ Missing Data Analysis", layout="wide")

st.subheader("⚠️ Missing Data Summary")
st.write("This section shows the distribution of missing values in the Titanic dataset."
         "Variables with no missingness are not listed.")

# Load Titanic dataset
titanic = load_data()

  # Drop 'deck' column due to high missingness
# Compute missingness summary
missing_summary = (
    titanic.isnull()
    .sum()
    .reset_index()
    .rename(columns={"index": "Variable", 0: "Missing_Count"})
)
missing_summary["Missing_Percentage"] = 100 * missing_summary["Missing_Count"] / len(titanic)

# Filter only variables with missing data
missing_summary = missing_summary[missing_summary["Missing_Count"] > 0]

missing_summary = missing_summary.loc[missing_summary["Variable"] != "embarked"]

st.dataframe(missing_summary.style.format({"Missing_Percentage": "{:.2f}%"}))
