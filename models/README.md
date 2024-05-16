[RealityStream](../)
# Models

RealityStream is being designed to merge feature and target datasets in Pandas on-the-fly.

- [Run Models (Industries CoLab)](../input/industries)
- [Location Forest (Bees)](location-forest)
- [Random Bits Forest (Blinks)](random-bits-forest)
- [Logistic Regression (Reality or Fiction Jobs)](reality-or-fiction)
- [Random Forest (Reality or Fiction Jobs)](reality-or-fiction)
- [Support Vector Machines (Reality or Fiction Jobs)](reality-or-fiction)

Prior to including data, models are referred to as skeletons or blueprints. Skeletons define the structure and logic of how the model should work prior to loading data. Model skeletons are like having the blueprint of a house without the materials to build it.

**ML Framework:** A framework typically refers to a structured set of tools, libraries, and conventions that provide a foundation for building something. In the case of machine learning, frameworks like TensorFlow, PyTorch, or scikit-learn provide the infrastructure and tools necessary to implement machine learning algorithms. If you have a Python script implementing a Random Forest algorithm but without data, it could be seen as a part of a machine learning framework.


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


# Big Data Questions

We're working with big data to find trend across time.
[Our BlueSky Projects](https://bsky.app/profile/modelearth.bsky.social) and [Feed Player Displays](https://model.earth/feed/view/) merge industry and environmental data to explore outcomes.

Do Google search algorithms direct people toward training that results in a better world?  Bushes and trees grow based on supporting networks of fungi based on biological algorithms. Are the locations where people relocate driven by the software they use, and the skills they offer? Does using Facebook, Microsoft, X, Douyin and BlueSky foster similar outcomes?

[Does expanding access to Starlink actually help increase tree canopy?](https://www.yahoo.com/news/elon-musk-diplomacy-woo-wing-155604090.html) In Brazil, Starlink was slated to provide internet connectivity to 19,000 rural schools, along with environmental monitoring of the Amazon. Let's explore changes to [world forest coverage over time](/data-commons/docs/conservation/).

[Run Models (Industries CoLab)](../input/industries)
