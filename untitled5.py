# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:46:28 2022

@author: priyanka.salunkhe
"""

# Import Library


import matplotlib.pyplot as plt
import numpy as np

# Define Data

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1, 3, 5, 7, 9, 11])

# Color

color = ['lightcoral', 'darkorange', 'olive', 'teal', 'violet', 
         'skyblue']

# Set different color

plt.scatter(x, y, c=color, s=400)

# Display

plt.show()