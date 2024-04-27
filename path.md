## Path Parameters

TO DO: Update app.py to take data path parameters and run additional models. 

	python app.py [features] [target] [models]

The indicated features dataset will be merged with a 2-column "target" dataset on-the-fly using Pandas to avoid storing merged files.

The term "features" is more prevalent in machine learning and data science.
"factors" has a stronger association with statistics and social sciences.

Each target dataset will contain 2 columns.  
1. The location column with one of the following column names:  
Country (2-char), State (2-digit fips), County or Fips (5-digit fips), Zip (5 char, 6 in China), or Voxel (2 char)
2. The "Target" column containing 1 or 0

Sample features and targets datasets will reside within the "input/[data]/features" and "input/[data]/targets" folders for each data source.

### About path name shortcuts

The parameters will have three versions: short ("bees"), medium ("input/bees/targets") and full ("input/bees/targets/bees-targets.csv").

Setting the models parameter to "all" would be the equivalent to "svc, rfc, lr, rbf, location-forest"
The default model will be "rbf" (Random Bits Forest) when blank.

**Parameter rules:**
If a slash / is in a parameter, treat it as a path.
If the file name is omitted from a path, append a file name.
For a target value of "bees" build the path "input/bees/targets/bees-targets.csv"
For a target value of "bees increase2024" build the path "input/bees/targets/bees-targets-increase2024.csv"

## Projects

1. Construct more models (i.e. XGBoost, neural networks) - Honglin
2. Improve the testing accuracy. - Honglin
3. Generate the feature-importance report for available models.
4. Formalize the Jupyter notebooks to convert them into a generalized pipeline, which takes different features and targets inputs.
5. Include industries-features-bkup.ipynb in the pipeline
6. Add startyear and endyear to parameters and Streamlit interface.
7. Maintain notes on how to run and update Streamlit interface locally.
8. Pull accuracy reports (from Ivy's yaml or json files) into one tabulator table for viewing. See our [tabulator sample page](../../data-pipeline/timelines/tabulator/) for merging within javascript.
9. Reuse report display process for other models
10. Push "toy" feature data from CoLabs directly to Github annually.

