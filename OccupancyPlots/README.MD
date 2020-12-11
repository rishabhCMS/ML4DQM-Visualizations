# Plot Occupancy plot for data visualization


### Link to slides:

1. Update [1.0](https://docs.google.com/presentation/d/1MphrvEPQ2q9zRDSToE6etqq5C2MzbRWP0xhw1-yWAmo/edit?usp=sharing)
(This was a preliminary presentation and the plots are plotted incorrectly here, the binning and overflow and underflow bins)

2. Update [2.0](https://docs.google.com/presentation/d/19U0MUbsW3J7Fnxp21Mkj-QTmAJXrof_T7eGGSDzGjWw/edit#slide=id.gac7122847d_0_2)
````console
ssh -XY username@lxplus.cern.ch
ssh ibmminsky-3
cd /afs/cern/ch/work/r/runiyal/occupancy_mldqm/
````
### Before you start plotting 

run the following commands to get individual hist for each layer (these commands may take time)

- [x]  `grep digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1 /eos/project/c/cmsml4dc/ML_2020/UL2017_Data/DF2017B_2D_Complete/*.csv > /afs/cern.ch/work/r/runiyal/occupancy_mldqm/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1.csv`

- [x] `grep digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1 /eos/project/c/cmsml4dc/ML_2020/UL2017_Data/DF2017B_2D_Complete/*.csv > /afs/cern.ch/work/r/runiyal/occupancy_mldqm/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2.csv`

- [x] `grep digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3 /eos/project/c/cmsml4dc/ML_2020/UL2017_Data/DF2017B_2D_Complete/*.csv > /afs/cern.ch/work/r/runiyal/occupancy_mldqm/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3.csv`

- [x] `grep digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4 /eos/project/c/cmsml4dc/ML_2020/UL2017_Data/DF2017B_2D_Complete/*.csv > /afs/cern.ch/work/r/runiyal/occupancy_mldqm/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4.csv`

- [x] `grep digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1 /eos/project/c/cmsml4dc/ML_2020/UL2017_Data/DF2017B_2D_Complete/*.csv > /afs/cern.ch/work/r/runiyal/occupancy_mldqm/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1.csv`

- [x] `grep digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2 /eos/project/c/cmsml4dc/ML_2020/UL2017_Data/DF2017B_2D_Complete/*.csv > /afs/cern.ch/work/r/runiyal/occupancy_mldqm/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2.csv`


**Now Follow the [Script](https://github.com/rishabhCMS/ML4DQM-Visualizations/blob/master/OccupancyPlots/plot_occupancy.py)**



### Layer 1 
![](https://github.com/rishabhCMS/ML4DQM-Visualizations/blob/master/OccupancyPlots/layer1.gif)

### Layer 2 
![](https://github.com/rishabhCMS/ML4DQM-Visualizations/blob/master/OccupancyPlots/layer2.gif)

### Layer 3 
![](https://github.com/rishabhCMS/ML4DQM-Visualizations/blob/master/OccupancyPlots/layer3.gif)

### Layer 4
![](https://github.com/rishabhCMS/ML4DQM-Visualizations/blob/master/OccupancyPlots/layer4.gif)
