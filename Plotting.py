#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:31:55 2020
"""

import matplotlib.pyplot as plt



lsize = 30

# TODO: arrange in a separate file?
fig = plt.figure() 
ax = fig.add_subplot(111)


ax.axis([ -5 , 170 ,-0.5, 10.5 ])
plt.yticks(range(11))

        
ax.scatter( minutes, happiness , counting_function(num_of_elements) *100 )

ax.set_xlabel('Piano playing time, minutes', size = lsize)
ax.set_ylabel('Subjective "mark" of happiness', size = lsize)

ax.grid()
