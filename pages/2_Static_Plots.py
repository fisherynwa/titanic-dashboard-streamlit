from helper_functions.visualize import *
from helper_functions.meta_data import load_data
import plotly.express as px
import numpy as np
import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


titanic = load_data()
# --------------------------------------------------
# Build static plots for demonstration
st.set_page_config(page_title="📊 Static Plot Examples", layout="wide")

st.header("📊 Static Plot Examples")


col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Passenger Survival Distribution")
    fig = px.pie(titanic,  names='survived', title='Passenger Survival Distribution', hole=0.3, 
                 labels={'survived': 'Survived'})
    st.plotly_chart(fig, width="stretch")
with col2:
    st.subheader("Passenger Count by Class")
    fig2 = px.pie(titanic, names='class', title='Passenger Count by Class', hole=0.3, 
                  labels={'class': 'Passenger Class'}, category_orders={"class": ["First", "Second", "Third"]},
                  color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig2, width="stretch")

pie_charts = make_subplots(rows=1, cols=3, specs=[[{"type": "pie"}, {"type": "pie"}, {"type": "pie"}]],
                          subplot_titles=("Cherbourg", "Southampton", "Queenstown"))

st.subheader("Pie Charts: Survival by Embarkation Town")
# the cities are \{"Southampton", "Cherbourg", "Queenstown"\}
pie_charts.add_trace(
            go.Pie(labels=titanic.loc[titanic['embarked'] == 'C']['survived'], pull = [.1, .1], 
                   title = 'Embarked Cherbourg vs. Survived'), row=1, col=1)

pie_charts.add_trace(
            go.Pie(labels=titanic.loc[titanic['embarked'] == 'S']['survived'], pull = [.05, .05],
                   title = 'Embarked Southampton vs. Survived'),row=1, col=2)

pie_charts.add_trace(
            go.Pie(labels=titanic.loc[titanic['embarked'] == 'Q']['survived'], pull = [.1, .1],
                   title = 'Embarked Queenstown  vs. Survived'), row=1, col=3)

#fig_comb.update_layout(title_text="Gene Expression Features")
st.plotly_chart(pie_charts, width="stretch")
