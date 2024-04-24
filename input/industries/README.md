[Industry Timelines Pipeline](../../../data-pipeline/timelines) - [RealityStream](../../) - [Random Bits Forest](../../models/random-bits-forest/)

# Industries Input Data

**Source:** [Community-Timelines](https://github.com/ModelEarth/community-timelines/tree/main/training/naics2/US/counties)
**Combine Years:** [Industry Features CoLab](https://colab.research.google.com/drive/1HJnuilyEFjBpZLrgxDa4S0diekwMeqnh?usp=sharing)
**Save as backup to run locally:** [input/industries/features/industries-features-bkup.ipynb](features/industries-features-bkup.ipynb)
**GitHub Output:** [community-timelines/training/all-years](https://github.com/ModelEarth/community-timelines/tree/main/training/all-years)

## Merging Data in Pandas

Avoid saving large feature datasets in local files, use Pandas to merge features and targets while processing.

Send merged data through multiple models (rbf.py, etc.)

TO DO: Figure out how to call other .ipynb files from one main app .py file, and through local Streamlit UI.

TO DO: Create target datasets for prosperity and jobgrowth

**Prosperity** - Which features forecast prosperity? (Wage growth and Value Added growth)
Features: types of industries, education levels, employment levels, population density, environmental indicators

**JobGrowth** - Which features forecast growth of quality jobs?
Features: types of industries, education levels, employment levels, population density, environmental indicators