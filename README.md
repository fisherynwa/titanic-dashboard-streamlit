# ***Titanic Dashboard

This dashboard visualizes passenger data from the Titanic dataset. Note that the presented visualizations are exemplary and are subject to change upon request.


![Demo Preview](/demo/demo.png)

# Dashboard Navigation

This dashboard contains 4 tabs

 - Home (this page is essenatial)
 - Dynamic Plots -- Multiple plots are provided that can be adjusted based on the selected filter options
 - Statis Plots -- Users can view multiple pie charts that are fixed; the filters do not affect them
 - Missing Data -- One can find info about 


 ## **Here we go **


### (I) **Clone the repo**


```bash
git clone
cd titanic_dashboard
```

# (II) Set up your env

By means of Conda:

 
Alternatively, one can mimic my env exactly: 
```bash
  conda env create -f environment.yml
  conda activate titanic_dashboard
```

By means of pip:

```bash
pip install -r requirements.txt
```

# (III) Run the Titanic dashboard

```
streamlit run Home.py

 Dependencies (min env)
  - python=3.12
  - numpy
  - pandas
  - plotly
  - streamlit
  - seaborn

