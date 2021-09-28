'''
@Author: Rashmi
@Date: 2021-09-26  10:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 10:20
@Title : Write a Python program to list all files in a directory in Python.
'''

from os import listdir
from os.path import isfile, join
files_list = [file for file in listdir('C:\\\Users\\Charishma\\Desktop\\rashmi\\PYTHONWORK\\DataStructures\\Basic Python') 
              if isfile(join('C:\\Users\\Charishma\\Desktop\\rashmi\\PYTHONWORK\\DataStructures\\Basic Python', file))]
print(files_list);