[RealityStream](../../)

## Random Forests for Bees

Using county industry changes to predict honey bee populations.

- [Our Input CoLab (Preprocessing)](https://colab.research.google.com/drive/1a8lbM7ceGGnaDe0kc1X0QqrZELsJINpb?usp=sharing)
- [Our Output CoLab](https://colab.research.google.com/drive/1y2A_XOFQrfu0HfXDPt2erg43Kn7Tc7xz?usp=sharing)
- [Upcoming - "Run Models" with Bees](../industries/)

- [Colab for creating 2-columns targets](https://colab.research.google.com/drive/11R3nSxPn91yTUBWhANBgdKCX0-YV1Dtk#scrollTo=Y9Un4FVwnxth)

NOTE: bees-targets.csv is a copy of bees-targets-increase2022.csv
bees-targets.csv would be the default when the target path is simply "bees"

Backup and run locally in [models/location-forest](../../models/location-forest/):

	python location-forest-input-bkup.ipynb bees
	python location-forest-output-bkup.ipynb bees


[2-column Target tables](https://github.com/ModelEarth/RealityStream/tree/main/input/bees/targets) containing county Fips.


We're updating our [Run Models colab](../industries/) to pull in 2-column bee target data for counties.



### Bee Pollinators

<div style="overflow:auto; margin-top:0px; padding-right:50px">

  <div style="font-size:16px">
  <b><span class="yeartext"></span>[Prior change] predicting [future] change at locations or in industry mix</b><br>
  For model training, a "y" column value of 1 indicate locations where [Attribute(s)] that changed in a [prior year] predict a later year.<br><br>
  </div>

  <div style="background:#fff; padding:20px; max-width:600px">
	  <img src="https://model.earth/community-forecasting/about/img/random-forest.webp" style="width:100%;"><br>
	</div>

  <div style="display:none;font-size:12pt;line-height:16pt;padding-top:20px">
    Best Params: 
    max depth: 8; <!-- max number of levels in each decision tree -->
    n-estimators: 100 <!-- number of trees in the foreset --><br>

    Accuracy before tuning: 69%.&nbsp;
    Accuracy after tuning: 71%.
  </div>
  
</div>

[Prior Bees Output](../../output/bees/)


## Datasets

Bee Pollinators USDA
<!-- - [Bee Pollinator Decline](https://sustainableagriculture.net/blog/pnas-wild-bee-study/) -->


<!--
[Old CoLab](https://colab.research.google.com/drive/1o7HXhOl_NWhVm4Nn6L-sjDHsn0bokgeI?usp=sharing) 
-->