# ML4DQM-Visualizations
This repo contains the code necessary to produces all the histograms for each quantile and each run for given datasets.
Just copy the allplots.py file in three separate folder day good, bad, bad_dcs
then for each copy of this code change the directory of the dataset for good, bad , bad_dcs
use command
> nohup python allplots.py > good.log & # inside the good folder
> nohup python allplots.py > bad.log & # inside the bad folder
> nohup python allplots.py > bad.log & # inside the bad_dcs folder


## Jupyter notebook access
