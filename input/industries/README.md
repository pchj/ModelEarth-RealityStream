[Industry Timelines Pipeline](../../../data-pipeline/timelines) - [RealityStream](../../) - [Random Bits Forest](../../models/random-bits-forest/)

# Industries Input Data

**Source:** [Community-Timelines](https://github.com/ModelEarth/community-timelines/tree/main/training/naics2/US/counties)

Our two CoLabs for industries:

1. Create Feature Datasets: [Generate Industry Features](https://colab.research.google.com/drive/1HJnuilyEFjBpZLrgxDa4S0diekwMeqnh?usp=sharing)
GitHub Output: [community-timelines/training/all-years](https://github.com/ModelEarth/community-timelines/tree/main/training/all-years)
Saved and run locally: [input/industries/features/industries-features-bkup.ipynb](features/industries-features-bkup.ipynb)

2. Run models: [Merge with Targets (Bees) for Forests and XGBoost](https://colab.research.google.com/drive/1zu0WcCiIJ5X3iN1Hd1KSW4dGn0JuodB8?usp=sharing)
Saved and run locally: [Merge-with-Target-XGBoost-bkup.ipynb](../../models/Merge-with-Target-XGBoost-bkup.ipynb)


## Merging Data in Pandas

Avoid saving large feature datasets in local files, use Pandas to merge features and targets while processing.

Send merged data through multiple models (rbf.py, etc.)

# Parallel Modeling Environments

| Inflow | Basket of Goods| Outflow | Predicted Results |
| ----------- | ----------- | ----------- | ----------- |
| [Ingredients](/data-commons/docs/food/) | [Healthy Meals](/OpenFootprint) | [Nutrients](/balance/) | [Impact on Body](/balance/label_checker.html) |
| [Suppliers](/data-pipeline/research/economy/) | [Commodities](/localsite/info/) | [Products](https://github.com/ModelEarth/OpenFootprint/tree/main/products/US) | [Impact on Environment](/community/tools/) |
| [Stimulus ML](/RealityStream/) | Brain Waves | [Brain Voxels Firing](/RealityStream/models/random-bits-forest/) | [Eye Blinks](/RealityStream/output/blinks/) |
| [Local Industries](/localsite/info/) | Honey Bees | [Population Change](/data-pipeline/research/bees/) | [Healthy Bee Population](/RealityStream/output/bees) |
| [Local Industries](/localsite/info/) | [Tree Canopy](/data-commons/docs/conservation/) | Biodiversity Change | Healthy Forest Growth |

<br>

## External Targets (Google Data Commons)

## Industry Targets

TO DO: Create target datasets for Job Growth and Wage Growth. - Ronan

Our upcoming [Industry target CoLab](https://colab.research.google.com/drive/19ReOauJDQHPU2a_Fln8-Kcgsd566IYtQ?usp=sharing)

**Job Growth** - Increase in local jobs for states and counties.
Features: types of industries, education levels, employment levels, population density, environmental indicators

**Wage Growth** - Increases in local pay levels
Features: types of industries, education levels, employment levels, population density, environmental indicators

TO DO: Try calling -bkup.ipynb files from app.py file.
