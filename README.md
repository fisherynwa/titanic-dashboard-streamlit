# Titanic Dashboard


This repo utilizes a Streamlit-based interactive dashboard for quick exploration of the Titanic dataset. The dashboard provides several dynamic and static visualizations of passenger data, survival statistics, and demographic distributions. Note that the presented visualizations are exemplary and may be modified upon request.



![Demo Preview](/demo/demo.png)

## Dashboard Navigation Tabs

This dashboard contains 4 tabs

 - Home (this page is essenatial)
 - Dynamic Plots -- Multiple plots are provided that can be adjusted based on the selected filter options
 - Statis Plots -- Users can view multiple pie charts that are fixed; the filters do not affect them
 - Missing Data -- One can find info about 


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

