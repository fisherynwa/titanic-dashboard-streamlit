# Titanic Dashboard


This repo utilizes a Streamlit-based interactive dashboard for exploring the Titanic dataset. The following dashboard provides several dynamic and static visualizations of passenger data, survival statistics, and demographic distributions. Note that the presented visualizations are exemplary and may be modified upon request.



![Demo Preview](/demo/demo.png)

## Dashboard Navigation Tabs

This dashboard contains 4 tabs

 - Home (this page is essential)
 - Dynamic Plots -- Multiple plots dynamically adjust based on user selections
 - Static Plots -- Users can view multiple pie charts that are fixed; the filters do not affect them
 - Missing Data -- Information about data missingness patterns across the Titanic dataset


## Here we go

### Clone the repo

```bash
git clone https://github.com/fisherynwa/titanic-dashboard-streamlit.git
cd titanic_dashboard
```

# Set up virt env

Using conda:
 
one can mimic my env exactly: 
```bash
conda env create -f environment.yml
conda activate titanic_dashboard
```

Using pip:

```bash
pip install -r requirements.txt
```

# Run the Titanic dashboard

```python
streamlit run Home.py
```


Dependencies (min env)
  - python=3.12
  - numpy
  - pandas
  - plotly
  - streamlit
  - seaborn

