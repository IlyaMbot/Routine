#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:21:52 2020
"""

#import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

'''
#this part of code is for testing execution time

import time

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
'''


''' TODO: let the program look for files in the folder with .dat extention
    ask for user to find DA WAE to the folder? :V
'''
#filenames input
filenames = ['lifehappiness.dat', 'lifehappiness2.dat' ]


def comma_point_replacer(filenames):
    ''' Reads files and replace all "," with "."
        Numbers inside files assumed to be float numbers
    '''
    for name in filenames:
        with open(name, 'r+') as file:
            out = file.read().replace(',', '.')
            file.seek(0)
            file.truncate()
            file.write(out)

#A class for objects-frames
class DataFrame:
    filename = 'blank'
    table = []
    columns = 0
    rows = 0
    def __init__(self, filename, table, columns, rows ):
        self.filename = filename 
        self.table = table          #data itself
        self.columns = columns
        self.rows = rows
    def showself(self):
        print(
                "the file", self.filename, "has", self.columns,
                "columns and", self.row, "rows.", sep = ' '
                )
''' QUESTION: how to upload data into class parameter? 
    Is it needed?
'''
        
#standart procedure for working with data from table
def table_reader(filenames):
    columns = []
    rows = []
    for name in filenames:
        df = pd.read_table(filenames, header = None, sep = r"\s+")    
        columns.append= len(df.iloc[:, 0])
        rows.append = len(df.iloc[0,: ])


happiness = DataFrame()
minutes = DataFrame() 

#TODO: refac the function
def vectorizator(columns, rows, table):
    # Turns table data into line 
    arrange = [] #????
    for i in range(columns):
        for j in range(rows):
            arrange[i * 7 + j] = table[i, j] # arrenge.append?
          
        
        
#TODO: delete this and make it better
'''
num_of_elements = np.zeros((row_num[0] * columns_num[0],2)) # Is it nescessary?

for i in range(len(num_of_elements)):
    num_of_elements[i] = [ happiness[i], minutes[i]] 
'''    

def counting_function(massive):
    ''' This function counts the number of days with same values
        TODO: refactoring instead of one, make two massives comparing
    '''
    arr_length = len(massive)
    count = np.zeros(arr_length)
    for i in range(arr_length):
        for j in range(arr_length):
            if massive[j,0] == massive[i,0] and massive[j,1] == massive[i,1]:
                count[i] += 1
    return(count)

''' TODO: remove this part of code below from here into another file 
    that will be responsible for plotting
'''

'''
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
'''