[Random Bits Forest](../../models/random-bits-forest/)

# Industries&nbsp;

[Our Data Pipeline](../../../data-pipeline/) and [NAICS Features Data](../../../data-pipeline/timelines/training/naics/)

TO DO: Create input-industries.py that pulls data for factors columns without saving locally.

Pull factors data from [community-timelines repo](../../../community-timelines)

Avoid saving factors in local files, use Pandas to send data directly to processing.

Send factors and targets through other models (rbf.py, etc.)

### Python to add

	python input-industries.py [factor dataset] [target dataset] [model]

### Factor Datasets

TO DO: Add these and other factor datset loads into Pandas

**Prosperity** - Which factors forecast prosperity?
Factors: types of industries, education levels, employment levels, population density, environmental indicators

**JobGrowth** - Which factors forecast growth of quality jobs?
Factors: types of industries, education levels, employment levels, population density, environmental indicators