#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:21:52 2020

@author: conpucter
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
#this part of code is for testing execution time
import time

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
'''

#filenames input
# TODO: let the program look for files in the folder with .dat extention
filenames = ['lifehappiness.dat', 'lifehappiness2.dat' ]


#read files and get data from them
for name in filenames:
    with open( name, 'r+' ) as file:
        out = file.read().replace( ',', '.' )
        file.seek(0)
        file.truncate()
        file.write(out)


#standart procedure for working with data from table
df = pd.read_table(filenames[0], header = None, sep = r"\s+")
df2 = pd.read_table(filenames[1], header = None, sep = r"\s+")

columns_num = [len(df.iloc[:, 0]), len(df2.iloc[:, 0])]
row_num = [len(df.iloc[0,: ]), len(df2.iloc[0,: ])]

# TODO: arrange in class?
happiness = np.zeros(row_num[0] * columns_num[0])
minutes =np.zeros(row_num[0] * columns_num[0]) 

#TODO: arrange in a function
for i in range(columns_num[0]):
    for j in range(row_num[0]):
        happiness[i * 7 + j] = df.iloc[i, j]
        minutes[i * 7 + j] = df2.iloc[i, j]
        
        

num_of_elements = np.zeros((row_num[0] * columns_num[0],2))


for i in range(len(num_of_elements)):
    num_of_elements[i] = [ happiness[i], minutes[i]] 


def counting_function(massive):
    ''' This function counts the number of days with same values
        TODO: refactoring
    '''
    arr_length = len(massive)
    count = np.zeros(arr_length)
    for i in range(arr_length):
        for j in range(arr_length):
            if massive[j,0] == massive[i,0] and massive[j,1] == massive[i,1]:
                count[i] += 1
    return(count)

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
