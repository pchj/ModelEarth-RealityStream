[RealityStream](../)
# Streamlit Interface

Interface concepts are in our StreamLit [reality.streamlit.app](https://reality.streamlit.app/). Bugs occur when StreamLit updates python libraries.

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


# Send Data from Streamlit to GitHub

Our Realitystream Streamlit app can push user-generated model performance reports directly to a designated repository location [/output/user_generated_json](https://github.com/ModelEarth/RealityStream/tree/main/output/user_generated_json). 

To configure your credentials, simply copy the example_secrets.toml file to secrets.toml and update it with your own information. The secret is stored under the [.streamlit directory](https://github.com/ModelEarth/RealityStream/tree/main/.streamlit).

When a user runs a model, the report is sent to the specified repository location, and a download option is provided.


# Streamlit URL Parameters

TO DO: [Send a #parameters hash value into Streamlit](https://discuss.streamlit.io/t/get-query-params-not-working-with-instead-of/20314)

Pass in a URL hash #parameters= value with the path to parameters.yaml, like this:  
https://reality.streamlit.app/#parameters=https://raw.githubusercontent.com/ModelEarth/RealityStream/main/parameters.yaml


Test when building the app.py to a localhost port.  
The build steps are here: https://model.earth/RealityStream

Or test by deploying your fork. Sign into share.streamlit.io
Click 'Deploy an app' and then paste in your GitHub fork URL

Parameter can also reside [after ? in Streamlit URL](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params)


