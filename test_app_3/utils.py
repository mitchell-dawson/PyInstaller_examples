#!/usr/bin/env python2

import numpy as np


def random_array(size_tuple):
    """ return a random array
    """

    output = np.random.rand(
        size_tuple[0], size_tuple[1])

    return output 
