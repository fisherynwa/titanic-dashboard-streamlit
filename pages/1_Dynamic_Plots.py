from helper_functions.visualize import *
from helper_functions.meta_data import load_data
import plotly.express as px
import numpy as np
import streamlit as st
import pandas as pd


# load the Titanic dataset:
titanic = load_data()

# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
st.set_page_config(page_title="📈 Dynamic Plot Examples", layout="wide")
st.sidebar.header("Filter Options")

options_class = titanic["class"].dropna().unique().tolist() # this gets unique values from the 'class' column
selected_class = st.sidebar.multiselect(
    "Passenger Class:",
    options= options_class,
    default= options_class,
)

options_sex = titanic["sex"].dropna().unique().tolist()
selected_sex = st.sidebar.multiselect(
    "Gender:",
    options=options_sex,
    default=options_sex,
)

st.sidebar.header("Optional Filter Options")

options_class_town = titanic["embark_town"].dropna().unique().tolist()
selected_class_town = st.sidebar.multiselect(
    "Embarkation Town:",
    options=options_class_town,
    default=None,
)
# --------------------------------------------------
 # Filter the Titanic dataset
if len(selected_class) == 0  and len(selected_sex) == 0:
     filtered_data = titanic.copy()
     st.error("No filters applied - showing its full dataset.")
else: 
    filtered_data = titanic[
        (titanic["class"].isin(selected_class)) &
        (titanic["sex"].isin(selected_sex))]

# --------------------------------------------------
# Display filtered data
# --------------------------------------------------

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<h3 style="color:#1f77b4;">
    <i class="fa-solid fa-chart-bar"></i> Descriptive Statistics of Filtered Titanic Data
</h3>
""", unsafe_allow_html=True)

if filtered_data.empty:
    st.warning("No results found for the current filters!")

st.markdown(
    f"**Total passengers:** {len(filtered_data)}  |  "
    f"**Survivors:** {filtered_data['survived'].sum()}  |  "
    f"**Survival Rate:** {filtered_data['survived'].sum() / len(filtered_data):.2%} "
)

# --------------------------------------------------
# 2 (top) columns for side-by-side visualizations
# --------------------------------------------------
col1, col2 = st.columns(2, gap="large")

# --- Plot 1: Survival count by gender ---
with col1:
    st.subheader("Survival by Gender")
    fig1 = create_histogram(filtered_data, attribute_col="sex", x_label = "Gender", color_map= {0: "#1f77b4", 1: "#2ca02c"})
    st.plotly_chart(fig1, width="stretch") #`use_container_width` will be removed after 2025-12-31!

# --- Plot 2: Age distribution by class ---
with col2:
    st.subheader("Age Distribution by Class")
    fig2 = box_hist_violin(filtered_data)
    st.plotly_chart(fig2, width="stretch")

# --------------------------------------------------
# 2 (bottom) columns for side-by-side visualizations
# --------------------------------------------------
col3, col4 = st.columns(2, gap="large")

with col3:
    st.subheader("Survival by Passenger Class")
    fig3 = create_histogram(filtered_data, attribute_col="class", x_label="Passenger Class", color_map={0: "#ff7f0e", 1: "#9467bd"})
    st.plotly_chart(fig3,  width="stretch")

with col4:
    st.subheader("The Interplay of Age and Fare in Determining Survival")
    fig4 = px.scatter(filtered_data, x='fare', y='age', color='survived', size='fare',
                      title="Fare vs. Age colored by Survival Status")
    st.plotly_chart(fig4, width="stretch")
    
    
# --------------------------------------------------
# bottom graphs
# --------------------------------------------------

if len(selected_class_town) > 0:

    col5, col6 = st.columns(2, gap="large")
    
    town_df = filtered_data[filtered_data["embark_town"].isin(selected_class_town)]
    
    with col5:
        st.subheader("Survival by Embarkation Town")
        fig5 = create_histogram(
           dataframe= town_df,
            attribute_col="embark_town",
            x_label="Embarkation Town",
            color_map={0: "#d62728", 1: "#8c564b"}
        )
        st.plotly_chart(fig5,  width="stretch")

    with col6:
        st.subheader("Fare Distribution by Embarkation Town")
        fig6 = px.violin(town_df, x='survived', y='fare', color = "sex", title="Comparing Passenger Fare by Survival Status and Gender",
                         box=True, points="all", hover_data=town_df.columns)
        st.plotly_chart(fig6, width="stretch")