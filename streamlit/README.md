[RealityStream](../)
# Streamlit Interface

TO DO: [Send a #parameters hash value into Streamlit](https://discuss.streamlit.io/t/get-query-params-not-working-with-instead-of/20314) - Manoj

<!--
	And after ? in Streamlit URL:
	https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params
-->

We'll pass in different parameters.yaml paths, like this: 

	#parameters=https://raw.githubusercontent.com/ModelEarth/RealityStream/main/parameters.yaml


### Feature Data Sources

Our Streamlit interface includes a dropdown menu for selecting feature datasets.

Currently only the "Job Listings" feature dataset is activated.

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


<a href="https://docs.streamlit.io/get-started/tutorials/create-an-app">How to create a Streamlit App</a> - <a href="https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app">How to Embed (both use iFrames)</a>