[Active Projects](/projects)

<a href="https://github.com/ModelEarth/RealityStream/" style="float:right">Github</a>
# RealityStream
Parallel development of our [Run Models CoLab](input/industries) and [Reality Streamlit App](https://reality.streamlit.app/)  
which will both weigh correlations between location features and location targets.

**Our Colab provides:** Logistic Regression, SVM, MLP, RandomForest, XGBoost  
**StreamLit provides:** Logistic Regression, RandomForest, Support Vector Machines (currently only for [Jobs: Reality-or-Fiction](output/jobs))

[Run-Models-bkup.ipynb](https://github.com/ModelEarth/RealityStream/tree/main/models) is a backup of the [CoLab](https://colab.research.google.com/drive/1zu0WcCiIJ5X3iN1Hd1KSW4dGn0JuodB8?usp=sharing) that we run locally. We append -bkup to indicate it is not the primary source.

## Run Models CoLab

- [Run Models (CoLab)](input/industries) - For feature and target datasets merged on their location columns.
- [Models Overview](models)
- [Accuracy Reports](output/jobs/) - Jobs Example

In Run Models, the "features" dataset is merged with a 2-column "target" dataset on-the-fly using either .csv files or Pandas to avoid storing merged .csv files. The location column joins features and targets. Location column data types:  

World Region (TBD), Country (2-char), State (2-char), County Fips (5-digits for state and county), Zip (5 char, 6 in China), or Brain Voxel (2 char)

## Default Data Sources

Our CoLab feature-target merge supports any data with a location column containing multiple locations.  
Our default data will always use County Fips so features and targets align.

**Industries (Features and Targets)** - County Fips
<a href="input/industries/">Industries Input Data</a>

**Bees (Target)** - County Fips
<a href="input/bees/">Random Forest (Bees)</a>

**Trees (Target)** - County Fips
[Tree Targets](input/trees/)


**Jobs** - Not location-based yet
<a href="models/reality-or-fiction/">Reality or Fiction</a>

**Blinks** - Location is brain voxels
<a href="models/random-bits-forest/">Random Bits Forest (Blinks)</a><br>



You can add paths to external data by editing a copy of the [parameters.yaml](https://github.com/ModelEarth/RealityStream/blob/main/parameters.yaml) file.


## Path Parameters


<!--
The term "features" is more prevalent in machine learning and data science.
"factors" has a stronger association with statistics and social sciences.
-->

TO DO: Finish updating our [Industry Features Colab](https://colab.research.google.com/drive/1HJnuilyEFjBpZLrgxDa4S0diekwMeqnh?usp=sharing) to take data path parameters from [parameters.yaml](https://github.com/ModelEarth/RealityStream/blob/main/parameters.yaml)  

TO DO: Add a python command that the default models locally using [Run-Models-bkup.ipynb](https://github.com/ModelEarth/RealityStream/tree/main/models), so the user does not need to open a notebook. Pass a parameters.yaml path in. 

The Run-Models-bkup.ipynb equivalent for our Streamlit version is app.py


Parameters are loaded from the parameters.yaml file:

	python Run-Models-bkup.ipynb [[path to parameters.yaml]()]

Example of parameters.yaml format:

	features: industries
		startyear: 2017
		endyear: 2021
	 	path: https://raw.githubusercontent.com/ModelEarth/community-timelines/main/training/naics{naics}/US/counties/{year}/US-{state}-training-naics{naics}-counties-{year}.csv
	targets: bees
		path: https://github.com/ModelEarth/RealityStream/raw/main/input/bees/targets/bees-targets.csv
	models: rbf

<!-- For later
	python Run-Models-bkup.ipynb [features] [target] [models]
-->

Each target dataset will contain 2 columns.  
1. The location column with one of the following column names:  
Country (2-char), State (2-char), Fips (5-digits for state and county), Zip (5 char, 6 in China), or Voxel (2 char)
2. The "Target" column containing 1 or 0

### About setting the model in parameters.yaml

Setting the models parameter to "all" would be the equivalent to "svc, rfc, lr, rbf, location-forest"  

For now, the default model will be "rbf" (Random Bits Forest) when blank.

### About path name shortcuts in parameters.yaml

Default features and targets datasets reside in the "input/[data]/features" and "input/[data]/targets" folders for each data source.

The simplest form of the parameters.yaml would be:

	features: "industries"
	targets: "bees"

In the above, the default model(s) would be used with these two file paths:

input/industries/input/industries-targets.csv
input/bees/targets/bees-targets.csv

The features.path and targets.path will have several shorthand versions and a full version from GitHub:

short - bees  
medium - input/bees/targets  
long - input/bees/targets/bees-targets.csv  
full - https://github.com/ModelEarth/RealityStream/raw/main/input/bees/targets/bees-targets.csv



**Parameter rules:**
If a slash / is in a parameter, treat it as a path.
If the file name is omitted from a path, append a file name.
For a target value of "bees" build the path "input/bees/targets/bees-targets.csv"
For a target value of "bees increase2024" build the path "input/bees/targets/bees-targets-increase2024.csv"

## Projects

Replace TO DO with your name as you work on a project.  
Write Loren when you've submitted a pull request to show your name.  
Update related .ipynb and app.py file to also add your name.

1. TO DO: Generate features-importance reports for available models.
2. TO DO: Load industries-features.ipynb colab output into Run Models using parameters.yaml.
3. TO DO: Add startyear and endyear to Streamlit interface, load from parameters.yaml.
4. TO DO: Find a comparison process or pull accuracy reports (from Ivy's yaml or json files) into one tabulator table for viewing. See our [tabulator sample page](../../data-pipeline/timelines/tabulator/) for merging within javascript.
5. TO DO: Reuse report display process for other models.
6. TO DO: Automate updating "toy" feature data using Github Actions.



## Streamlit Interface

TO DO: Set up [sending a hash value into Streamlit](https://discuss.streamlit.io/t/get-query-params-not-working-with-instead-of/20314) - Manoj

<!--
	And after ? in Streamlit URL:
	https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params
-->

We'll pass in different parameters.yaml paths, like this: 

	#parameters=https://raw.githubusercontent.com/ModelEarth/RealityStream/main/parameters.yaml


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

## Launch Streamlit app in a Virtual Environment

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

TO DO: When parameters above are omitted, use defaults (below).


## Send Data from Streamlit to GitHub

Our Streamlit app can push user-generated model performance reports directly to a designated repository location (output/user_generated_json).

To configure your credentials, copy the example_secrets.toml file to secrets.toml and update it with your own information. The secret is stored under the .streamlit directory.

When a user runs a model, the report is sent to the specified repository location, and a download option is provided.



