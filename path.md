## Path Parameters

Each target dataset will contain 2 columns:  
The value 1 or 0 in the "Target" column
The location column with one of the following column names:  

Country (2-char), State (2-digit fips), County (5-digit fips), Zip (5 char, 6 in China), or Voxel (2 char).

The term "features" is more prevalent in machine learning and data science. "factors" has a stronger association with statistics and social sciences.

Small sample features and target data will reside within the "input/[data]/features" folders for each data source.

The feature datasets will be merged with 2-column "target" datasets on-the-fly to avoid storing merged files.

The merged data will be sent to multiple models by using these parameters:

	python app.py [features] [target] [models]

TO DO: Update app.py to take parameters. Test that it continues to work with Streamlit.

The parameters will be both shorthand ("bees") and paths ("input/bees/targets").

Setting the models parameter to "all" could be the equivalent to "svc,rfc,lr,rbf,location-forest"
The default model value might be "rbf" (Random Bits Forest) when blank.

**Parameter rules:**
If a slash / is in a parameter, treat it as a path.
If the file name is omitted from a path, append a file name.
Example: For a parameter of "input/bees/targets/increase2024", append the file name "/bees-targets-increase2024.csv"

If the target shorthand parameter is simply "bees", the path would simply [bee](https://model.earth/replicate/): "input/bees/targets/bees-targets.csv"

## Projects

1. Construct more models (i.e. XGBoost, neural networks) - Honglin
2. Improve the testing accuracy.
3. Generate the feature-importance report for available models.
4. Formalize the Jupyter notebooks to convert them into a generalized pipeline, which takes different features and targets inputs.
5. Include industries-features-bkup.ipynb in the pipeline
6. Add startyear and endyear to parameters and Streamlit interface.
7. Maintain notes on how to run and update Streamlit interface locally.
8. Pull accuracy reports (from Ivy's yaml or json files) into one tabulator table for viewing. See our [tabulator sample page](../../data-pipeline/timelines/tabulator/) for merging within javascript.
9. Reuse report display process for other models
10. Push "toy" feature data from CoLabs directly to Github annually.

## Streamlit Interface

Our Streamlit interface will include radio buttons for selecting targets, including:
1. Bee population change (Irene created 4 columns, each would be its own file)
2. Top 20% counties for job growth (to-do)
3. Top 20% counties for wage growth (to-do)