# RealityStream
A Streamlit App which weighs possibilities - <a href="https://github.com/ModelEarth/RealityStream/">Github</a>
Expanded by <a href="https://Model.earth">Model.earth</a> - <a href="https://docs.streamlit.io/get-started/tutorials/create-an-app">How to create a Streamlit App</a> - [How to Embed](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app)
<!-- For ML Classification. -->

## CoLabs

- [Industries](input/industries)

## Models

Our model skeletons are being designed to work with all feature and target datasets.

- [Location Forest (Bees)](models/location-forest)
- [Random Bits Forest (Blinks)](models/random-bits-forest)
- [Logistic Regression (Reality or Fiction Jobs)](models/reality-or-fiction)
- [Random Forest (Reality or Fiction Jobs)](models/reality-or-fiction)
- [Support Vector Machines (Reality or Fiction Jobs)](models/reality-or-fiction)

## Streamlit Interface

Our Streamlit interface will include a dropdown menu for selecting targets, including:
1. [Honey Bee Health](output/bees/) - Bee population change (Irene created 4 columns, each would be its own file)
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

## Data Sources

Each data source has a location column, so it can act as both a feature and target. Location column names:

Country (2-char), State (2-char), Fips (5-digits for state and county), Zip (5 char, 6 in China), or Voxel (2 char)

**Industries (Features and Targets)**
<a href="input/industries/">Industries Input Data</a>

**Jobs**
<a href="models/reality-or-fiction/">Logistic Regression (Jobs)</a>

**Bees (Target)**
<a href="input/bees/">Random Forest (Bees)</a>

**Blinks**
<a href="models/random-bits-forest/">Random Bits Forest (Blinks)</a><br>

**Trees (Target)**
[Tree Targets](input/trees/)