# ML4DQM-Visualizations
This repo contains the code necessary to produces all the histograms for each quantile and each run for given datasets.
Just copy the allplots.py file in three separate folder day good, bad, bad_dcs
then for each copy of this code change the directory of the dataset for good, bad , bad_dcs
use command
1. nohup python allplots.py > good.log & # inside the good folder
2. nohup python allplots.py > bad.log & # inside the bad folder
3. nohup python allplots.py > bad.log & # inside the bad_dcs folder


## Jupyter notebook access on the minsky cluster
0. I used chrome for this to work
1. ssh -C -D 9999 youruser@lxplus.cern.ch
2. change the proxy settings
![Image description](https://raw.githubusercontent.com/rishabhCMS/ML4DQM-Visualizations/blob/master/DataViz2018/Presentations/image.png)
3.http://ibmminsky-head.cern.ch:8080/platform
4.login with your cern credentials
5. Workload> Spark > My apps and Notebooks [ this NB usually doesn't work when I wrote these insturctions]
6. So,go to http://ibmminsky-3.cern.ch:9970
7. Jupyter NB Tutorial - https://www.ibm.com/support/knowledgecenter/en/SSZU2E_2.3.0/tutorial/t_notebook.html
8. ref this pdf from the minsky knowledge tranfer event https://github.com/rishabhCMS/ML4DQM-Visualizations/blob/master/DataViz2018/Presentations/20190903-MinskyClusterTraining.pdf
9. once you are inside the notebook you can chnage the directory using !cd and !pwd etc
