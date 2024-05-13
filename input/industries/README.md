[Industry Timelines Pipeline](../../../data-pipeline/timelines) - [RealityStream](../../)

# Industries Input Data

**Our primary CoLab:**
[Run Models](https://colab.research.google.com/drive/1zu0WcCiIJ5X3iN1Hd1KSW4dGn0JuodB8?usp=sharing) (Includes XGBoost) - Merges Features with Targets based on parameters.yaml
Backup and run locally @ models/Run-Models-bkup.ipynb

**Initial Python** (matched Streamlit)
models/reality-or-fiction/reality-or-fiction.ipynb

**Cool processes we're implementing in the Run Models CoLab**
- Toggle between pulling data from Github and local files
- Choose to send results to display, Github and/or local files
- Allow user to save their own Github account in local storage
- Build a yaml file from localStorage that the user can paste or pull into CoLab.
- Run data updates automatically quarterly with Github Actions, send a report

**Big Questions**

Do Google Search Algorithms direct people (bushes and trees) toward training that results in a better world? (Including where they relocate to and the code they focus on and the impact of the software they use.) Compare the outcomes (migrations and design impacts) of using software algorithms (fungus) by Google, Microsoft, Salesforce and others.

Do Facebook, X, Douyin and BlueSky have similar outcomes?  
Coordinate analysis tools with researchers who are subscribing to backend network data.
[Our BlueSky Projects](https://bsky.app/profile/modelearth.bsky.social) and [Feed Player Displays](https://model.earth/feed/view/) (For CORS feeds, hit refresh after <a href="https://cors-anywhere.herokuapp.com/" target="passthrough">turning on passthrough</a>.)

## Features Data

**Industry Features Data Prep:**
[Generate Industry Features](https://colab.research.google.com/drive/1HJnuilyEFjBpZLrgxDa4S0diekwMeqnh?usp=sharing) (All years)  
GitHub Output: [community-timelines/training/all-years](https://github.com/ModelEarth/community-timelines/tree/main/training/all-years)  
Source: [Community-Timelines](https://github.com/ModelEarth/community-timelines/tree/main/training/naics2/US/counties)  
Backup and run locally @ input/industries/features/industries-features-bkup.ipynb

## Target Data

**External Targets (Google Data Commons)**

Tree Canopy improvements, Improvements in Emissions by state and country

**Industry Targets**

TO DO: Contribute to our [Industry target CoLab](https://colab.research.google.com/drive/1urO9phMMt0GyAXRsowf2dbLjQ6DlWTKf?usp=sharing)

TO DO: Create target datasets for Job Growth and Wage Growth. - Ronan

<!--
Blank [Industry target CoLab](https://colab.research.google.com/drive/19ReOauJDQHPU2a_Fln8-Kcgsd566IYtQ?usp=sharing)
-->
**Job Growth** - Increase in local jobs for states and counties.
Features: types of industries, education levels, employment levels, population density, environmental indicators

**Wage Growth** - Increases in local pay levels
Features: types of industries, education levels, employment levels, population density, environmental indicators

TO DO: Call -bkup.ipynb files from our Streamlit app.py files to build models and save reports.

## Merging Data in Pandas

Avoid saving large feature datasets in local files, use Pandas to merge features and targets while processing.

Send merged data through multiple models (rbf.py, etc.)

<br>

# Parallel Modeling Environments

x-axis Features (naics, voxels, nutrients)  
y-axis Locations (merged to targets on fips)

Merge features and targets on locations (fips, voxels, foods)

| Inflow | Basket of Goods| Outflow | Predicted Results |
| ----------- | ----------- | ----------- | ----------- |
| [Suppliers](/data-pipeline/research/economy/) | [Commodities](/localsite/info/) | [Products](https://github.com/ModelEarth/OpenFootprint/tree/main/products/US) | [Impact on Environment](/community/tools/) |
| [Stimulus ML](../blinks/) | Brain Waves | [Brain Voxels Firing](/RealityStream/models/random-bits-forest/) | [Eye Blinks](/RealityStream/output/blinks/) |
| [Local Industries](/localsite/info/) | Honey Bees | [Population Change](/data-pipeline/research/bees/) | [Healthy Bee Population](/RealityStream/output/bees) |
| [Local Industries](/localsite/info/) | [Tree Canopy](/data-commons/docs/conservation/) | Biodiversity Change | Healthy Forest Growth |
| [Ingredients](/data-commons/docs/food/) | [Healthy Meals](/OpenFootprint) | [Nutrients](/balance/) | [Impact on Body](/balance/label_checker.html) |

<br>

