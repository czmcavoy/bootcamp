import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

def ecdf(data):

    """
    Calculate the empirical cumulative distribution function (ECDF) from
    a set of data.
    """

    ecdfx = np.sort(data)
    ecdfy = np.arange(1, len(data)+1)/len(data)


    return ecdfx,ecdfy
