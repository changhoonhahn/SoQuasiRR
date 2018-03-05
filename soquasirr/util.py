'''

General utility functions 

'''
import os
import numpy as np
import scipy.stats as Stat
from scipy.stats import nbinom as nbinom
from scipy import interpolate


def code_dir(): 
    ''' Directory where all the code is located (the directory that this file is in!)
    '''
    return os.path.dirname(os.path.realpath(__file__))


def dat_dir(): 
    ''' dat directory is symlinked to a local path where the data files are located
    '''
    return os.path.dirname(os.path.realpath(__file__)).split('soquasirr')[0]+'dat/'


def fig_dir(): 
    ''' dat directory is symlinked to a local path where the data files are located
    '''
    return os.path.dirname(os.path.realpath(__file__)).split('letstalkaboutquench')[0]+'figs/'


def bar_plot(bin_edges, values): 
    ''' Take outputs from numpy histogram and return pretty bar plot
    '''
    xx = [] 
    yy = [] 

    for i_val, val in enumerate(values): 
        xx.append(bin_edges[i_val]) 
        yy.append(val)
        xx.append(bin_edges[i_val+1]) 
        yy.append(val)

    return [np.array(xx), np.array(yy)]
