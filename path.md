## About Path Parameters

We'll have "toy" factors-dataset input for industries in factor subfolders:

	RealityStream/input/industries/[factorname]/input-industries-[factorname].csv

**Example factor file name:** input-industries-CountiesNaics4.csv

The industry factors datasets will be merged with 2-column target-datasets within input folders for bees, trees and the industries folder itself. All will be usable with multiple models by using these 3 parameter for loading:

	python input-industries.py [factor-dataset] [target-dataset] [models]

The parameters will be both shorthand ("bees") and paths ("input/bees/targets").

Use all models could be: "all", the equivalent to "svc,rfc,lr,rbf,location-forest"
The default model might be Random Bits Forest "rbf" when blank.

**Parameter rules:**
If a slash / is in a parameter, treat it as a path.
If the file name is omitted from a path, append the file name with this format:
For a parameter of "input/bees/targets/increase2024", append "/bees-targets-increase2024.csv"
to produce the file path "input/bees/targets/increase2024/bees-targets-increase2024.csv"
(Where "targets-increase2024" is the 1 or 2 child folder(s) on the right side of the input/[target name "bees"].)

If the target-dataset shorthand parameter is simply "bees", the path would simply [bee](https://model.earth/replicate/): "input/bees/targets/bees-targets.csv"