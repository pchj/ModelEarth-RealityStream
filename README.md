[Active Projects](/projects)

<a href="https://github.com/ModelEarth/RealityStream/" style="float:right">Github</a>
# RealityStream
Parallel development of our [Run Models CoLab](input/industries) and [Reality Streamlit App](https://reality.streamlit.app/)  
which will both weigh correlations between location features and location targets.

**Our Colab provides:** Logistic Regression, SVM, MLP, RandomForest, XGBoost  
**StreamLit provides:** Logistic Regression, RandomForest, Support Vector Machines (currently only for [Jobs: Reality-or-Fiction](output/jobs))

**Example of parameters.yaml format**

	features: "industries"
		startyear: 2017
		endyear: 2021
	 	path: "https://raw.githubusercontent.com/ModelEarth/community-timelines/main/training/naics{naics}/US/counties/{year}/US-{state}-training-naics{naics}-counties-{year}.csv"
	targets: "bees"
	models: rbf"


TO DO: Let's figure out how to pass a URL hash value into both the CoLab and StreamLit  
so we can pass in paths to different parameters.yaml files, live this: 

	#parameters=https://raw.githubusercontent.com/ModelEarth/RealityStream/main/parameters.yaml

## Run Models CoLab

- [Run Models (CoLab)](input/industries) - For feature and target datasets merged on their location columns.
- [Models Overview](models)

The location column joins features and targets. Location column names:  
Country (2-char), State (2-char), Fips (5-digits for state and county), Zip (5 char, 6 in China), or Voxel (2 char)

## Sample Location Data Sources

Our CoLab supports any data with a location column containing multiple locations.  

Add paths to external data by editing a copy of the [parameters.yaml](https://github.com/ModelEarth/RealityStream/blob/main/parameters.yaml) file.

**Industries (Features and Targets)**
<a href="input/industries/">Industries Input Data</a>

**Jobs**
<a href="models/reality-or-fiction/">Reality or Fiction</a>

**Bees (Target)**
<a href="input/bees/">Random Forest (Bees)</a>

**Blinks**
<a href="models/random-bits-forest/">Random Bits Forest (Blinks)</a><br>

**Trees (Target)**
[Tree Targets](input/trees/)


## Streamlit Interface

### Feature Data Sources

Our Streamlit interface includes a dropdown menu for selecting features (factors).

Currently only the "Job Listings" feature is activated.

### Target Data Sources

Our Streamlit interface includes a dropdown menu for selecting targets.

Currently only the "Job Listings" target is activated.
TO DO: Pull in data for the other targets. 

1. [Honey Bee Health](input/bees/) - Bee population change (Irene created 4 columns, each would be its own file)
2. [Job Growth](input/industries/) - Top 20% counties for job growth (to-do)
3. [Wage Growth](input/industries/) - Top 20% counties for wage growth (to-do)
4. [Eye Blinks](output/blinks/) - Brain fMRI Voxels
5. [Job Listings](output/jobs/) - Reality or Fiction

Install the streamlit Command-Line Interface (CLI) if you haven't yet.
If you have an error during the install, our [docs page](docs) may have a fix.

	pip install streamlit

This should launch a browser with demos:

	streamlit hello

## Launch in Virtual Environment

Initiate a virtual environment before running streamlit via `streamlit run app.py`

	python3 -m venv env
	source env/bin/activate

For Windows,

	python3 -m venv env
	.\env\Scripts\activate


Launch our interface locally:

	streamlit run app.py


If an error occurs, our [docs page](docs) may have a fix.

<!--
To also try:

	streamlit run https://raw.githubusercontent.com/streamlit/reality/master/app.py
-->
TO DO: load [parameters.yaml](parameters.yaml) file, add more parameters:

	streamlit run app.py "parameters.yaml"

TO DO: When parameters above are omitted, use defaults.

