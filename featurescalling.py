#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: geekquad
"""
import numpy as np

def featurescale(input_list, new_min, new_max):
    old_min = np.min(input_list)
    old_max = np.max(input_list)
    old_range = (old_max - old_min)
    new_range = (new_max - new_min)
    
    new_list = []
    for i in input_list:
        newi = (((i - old_min) * new_range) / old_range) + new_min
        new_list.append(newi)
        
    return new_list