[RealityStream](../../) - [Random Bits Forest](../../models/random-bits-forest/)

# Industries&nbsp;

[Our Data Pipeline](../../../data-pipeline/) and [NAICS Features Data](../../../data-pipeline/timelines/training/naics/)

TO DO: Implement work done by Yanqing (Lily) and Sijia which loads naics data into Pandas for 2017 to 2021 for Maine. [info](/data-pipeline/timelines/).  Create or modify CoLab for shared util called industry-timeline-bkup.py that pulls data for features columns without saving locally.

Avoid saving large feature datasets in local files, use Pandas to send data directly to processing.

Send features and targets through other models (rbf.py, etc.)

TO DO: Create target datasets for prosperity and jobgrowth

**Prosperity** - Which features forecast prosperity?
Features: types of industries, education levels, employment levels, population density, environmental indicators

**JobGrowth** - Which features forecast growth of quality jobs?
Features: types of industries, education levels, employment levels, population density, environmental indicators