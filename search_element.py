#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:53:40 2020

@author: conpucter
"""

import matplotlib.pyplot as plt
import numpy as np

#define data "from different files" 
y = np.random.random_integers(0,5,50)
x = np.random.random_integers(0,5,50)

#combine the data into a massive
massive = np.zeros(( len(x), 2))

for i in range(len(x)):
    massive[i] = [x[i] ,y[i]]

#a massive for number of similar values 

    

# compaing the elements with the same coordinates

def counting_function(massive):
    count = np.zeros(len(x))
    for i in range(len(massive)):
        for j in range(len(massive)):
            if massive[j,0] == massive[i,0] and massive[j,1] == massive[i,1]:
                count[i] += 1
    return(count)        


fig = plt.figure() 
ax = fig.add_subplot(111)

ax.scatter( massive[:,0], massive[:,1] , counting_function(massive) * 1000  )


ax.grid()