## Path Parameters

The term "features" is more prevalent in machine learning and data science. "factors" has a stronger association with statistics and social sciences.

Small sample features and target data will reside within "input" folders for:
bees, blinks, trees, jobs, and industries

The feature datasets will be merged with 2-column "target" datasets.

The merged data will be sent to multiple models by using these parameters:

	python app.py [features] [target] [models]

TO DO: Update app.py to take parameters. Test that it continues to work with Streamlit.

The parameters will be both shorthand ("bees") and paths ("input/bees/targets").

Setting models to "all" could be the equivalent to "svc,rfc,lr,rbf,location-forest"
The default model value might be "rbf" (Random Bits Forest) when blank.

**Parameter rules:**
If a slash / is in a parameter, treat it as a path.
If the file name is omitted from a path, append a file name.
Example: For a parameter of "input/bees/targets/increase2024", append the file name "/bees-targets-increase2024.csv"

If the target shorthand parameter is simply "bees", the path would simply [bee](https://model.earth/replicate/): "input/bees/targets/bees-targets.csv"

TO DO: Create a multi-model accuracy report by pulling multiple yaml or json reports into a single tabulator table. See our [tabulator sample page](../../data-pipeline/timelines/tabulator/) for merging with javascript.

## Upcoming

Thursday April 25 and Sunday next week

1. Construct more models (i.e. XGBoost, neural networks)
2. Improve the testing accuracy
3. Generate the feature-importance report for available models, and 
4. Formatize the jupyter notebook to convert it as a generalized pipeline, which takes different features and targets inputs
