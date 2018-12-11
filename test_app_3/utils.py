#!/usr/bin/env python2

import numpy as np
import pandas as pd


def random_array(size_tuple):
    """ return a random array
    """

    output = np.random.rand(
        size_tuple[0], size_tuple[1])

    return output 


def read_csv_data(csv_path):
    """read in a single csv file
    """

    return pd.read_csv(csv_path, sep=',', engine='python')
