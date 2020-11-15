#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:21:52 2020
"""

import pandas as pd
import numpy as np

"""
#this part of code is for testing execution time

import time

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
"""



''' TODO: let the program look for files in the folder with .dat extention
    ask for user to find DA WAE to the folder? :V
'''
#filenames input
filenames = ['lifehappiness.dat', 'lifehappiness2.dat']


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
    filename = 'default_blank'
    data = []
    columns = 0
    rows = 0
    '''
    def __init__(self, filename, data, columns, rows ):
        self.filename = filename
        self.data = data
        self.columns = columns
        self.rows = rows
    '''
    def showself(self):
        print(
                "the file", self.filename, "has", self.columns,
                "columns and", self.row, "rows.", sep = ' '
                )
''' QUESTION: how to upload data into class parameter?
    Is it needed?
'''


#create a function that creates objects and their atributes from data?
happiness = DataFrame()
minutes = DataFrame()


#standart procedure for working with data from table
def table_reader(filenames, inclass):
    ''' inclass has atribute .data and it needed to add this data 
        into class' atribute  
    '''
    columns = []
    rows = []
    for name in filenames:
        inclass.data = pd.read_table(filenames, header = None, sep = r"\s+")
        columns.append= len(inclass.data.iloc[:, 0])
        rows.append = len(inclass.data.iloc[0,: ])

table_reader(filenames, happiness)
table_reader(filenames, minutes)

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

def counting_function(massive1, massive2):
    ''' This function counts the number of days with same values
        TODO: refactoring instead of one, make two massives comparing
        massive2 should be optional
    '''
    arr_length = len(massive1)
    count = np.zeros(arr_length)
    for i in range(arr_length):
        for j in range(arr_length):
            if massive1[j] == massive1[i] and massive2[j] == massive2[i]:
                count[i] += 1
    return(count)

print(counting_function(happiness.data, minutes.data))