## About Path Parameters

The term "features" is more prevalent in machine learning and data science. "factors" has a stronger association with statistics and social sciences.

Sample features and target data will reside within "input" folders for:
bees, blinks, trees, jobs, and industries

Sample features file path for industries:

	RealityStream/input/industries/features/fips-naics4.csv

The feature datasets will be merged with 2-column "target" datasets.

The merged data will be sent to multiple models by using these parameters:

	python app.py [features] [target] [models]

TO DO: Update app.py to take parameters. Test that it continues to work with Stremlit.

The parameters will be both shorthand ("bees") and paths ("input/bees/targets").

Setting models to "all" could be the equivalent to "svc,rfc,lr,rbf,location-forest"
The default model value might be "rbf" (Random Bits Forest) when blank.

**Parameter rules:**
If a slash / is in a parameter, treat it as a path.
If the file name is omitted from a path, append the file name with this format:
For a parameter of "input/bees/targets/increase2024", append "/bees-targets-increase2024.csv"
to produce the file path "input/bees/targets/increase2024/bees-targets-increase2024.csv"
(Where "targets-increase2024" is the 1 or 2 child folder(s) on the right side of the input/[target name "bees"].)

If the target shorthand parameter is simply "bees", the path would simply [bee](https://model.earth/replicate/): "input/bees/targets/bees-targets.csv"

