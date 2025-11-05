import streamlit as st
import seaborn as sns
from helper_functions.meta_data import *
import pandas as pd


st.set_page_config(page_title="Titanic Dashboard", layout="wide")

st.title("🏠 Titanic Dashboard")


titanic = load_data()
# Filter data
with st.expander("About this dataset"):
    st.write("""
        The Titanic dataset is well-known in the data science community and contains information
        about the passengers aboard the Titanic. It includes details such as age,
        gender, passenger class, fare paid, and whether or not the passenger survived (the accident).
        This dashboard allows users to explore the dataset interactively using filters and visualizations.
    """)
    st.write("### Filtered Data Preview (inside expander)")
    st.dataframe(titanic.describe())
    
def stream_data():
    meta_df = meta_data()
    yield pd.DataFrame(meta_df) # Use 'yield' to simulate streaming
# Button to trigger streaming output
show_table = st.toggle("Show Titanic Non-Intuitive Variable Definitions")

if show_table:
    st.write_stream(stream_data())
else:
    st.info("👆 Click the toggle to view the data glossary")