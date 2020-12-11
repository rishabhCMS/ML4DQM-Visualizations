
import numpy as np
from numpy import array
import pandas as pd


import matplotlib.image as mpimg
import matplotlib.cm as cm
from ast import literal_eval

import matplotlib.pyplot as plt
#import seaborn as sns

from numpy import array
from scipy.linalg import svd
from scipy import linalg

from matplotlib.pyplot import figure


import sys
import os 
from mpl_toolkits.axes_grid1 import make_axes_locatable


def occupancy_extract_plot(df, path):
    '''
    This function takes as input the dataframe containing a 2d hist as one of the columns
    also, takes in the location where images are to be saved
    this plots the 2d hists dropping the overflow and underflow bins
    '''

#     df_occupancy  = df[df['hname'].str.contains("occupancy")]
    df.set_index(['run','LS'], inplace=True, drop=False)
    df.sort_index(inplace=True)
    
    for layer in df.hname.unique():
        layer_name = layer.split('_')[-2]
        layer_num = layer.split('_')[-1]
        df_sample = df  
#        if layer_num != '1':continue
        
        for index, row in df_sample.iterrows():
            histo = row['histo']
            n_xbins = row['Xbins']
            n_ybins = row['Ybins']
#             print(index)
            cache_line = eval(histo)
            

            histo= np.split(np.asarray(cache_line), (n_ybins+2))

                
            binsize_x = (row['Xmax']  - row['Xmin'])/ n_xbins
            binsize_y = (row['Ymax']  - row['Ymin'])/ n_ybins
            
            x_bins = np.arange(row['Xmin'],row['Xmax']+binsize_x,binsize_x)
            y_bins = np.arange(row['Ymin'],row['Ymax']+binsize_y ,binsize_y)
            
            
            fig = plt.figure(figsize=(14.8,10))
            ax = fig.add_subplot(111)
            nrows, ncols = len(x_bins), len(y_bins)
            # grid = temp.reshape((nrows, ncols))
            run, lumi = index
            max_ = np.array(histo).flatten().max()

            
            title = str(layer)+'_'+str(run)+'_'+str(lumi)
            plt.title(title)
            
            # annotating the number of x bins and y bins on the plot
            plt.annotate("xbins={}".format(n_xbins), xy=(1.005, 0), xycoords='axes fraction')
            plt.annotate("ybins={}".format(n_ybins), xy=(1.005, .1), xycoords='axes fraction')

            # drawing grid lines on the minor axis for the modules
            ax.set_yticks(y_bins[1::2])
            ax.set_yticks(y_bins[0::2], minor=True)

            ax.set_xticks(x_bins[4::8])
            ax.set_xticks(x_bins[8::8], minor=True)
            ax.grid(which='minor',color='black', linestyle='--',linewidth=1)

            
            plt.xlabel("Signed Module Coord")
            plt.ylabel("Signed Ladder Coord")

            #dropping the overflow and underflow bins
            histo = np.delete(histo, 0, axis=1)
            histo = np.delete(histo, -1, axis=1 )
            histo_norm = histo[1:-1]/max_
            
            cmap = cm.rainbow
            cmap.set_under(color='white')
            im = plt.imshow(histo_norm, extent=(x_bins.min(), x_bins.max(), y_bins.min(), y_bins.max()),interpolation='none', cmap=cmap, aspect='auto', vmin=0.1, origin='lower')
            
            #colorbar position and padding
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="7%", pad=0.8)
            plt.colorbar(im, cax=cax)

            pathimg = path+'/'+layer_name+'/'+layer_num+'/'
            if not os.path.isdir(pathimg):
                os.makedirs(pathimg)

            plt.savefig(pathimg+str(run)+'_'+(str(lumi)).zfill(3)+'_'+layer, dpi=60)
            plt.close('all')
        print(layer_name,'DONE')

if __name__ == '__main__':

    path_to_csv_file = "digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1.csv"
    path_to_save_plots = "/afs/cern.ch/work/r/runiyal/occupancy_mldqm/occupancy_plots/zerobias2017B"
    df = pd.read_csv(path_to_csv_file, header=None)
    cols = ['dataset','run', 'LS', 'hname', 'histo', 'entries', 'Xmax', 'Xmin',
       'Xbins', 'Ymax', 'Ymin', 'Ybins']
    df.columns = cols
    
    if not os.path.isdir(path_to_save_plots):
        os.makedirs(path_to_save_plots)

    occupancy_extract_plot(df, path_to_save_plots)
