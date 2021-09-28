'''
@Author: Rashmi
@Date: 2021-09-26  11:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 11:40
@Title :Write a Python program to get an absolute file path.
'''
import os

if __name__ == '__main__': 
    '''Description : to get an absolute file path using os.path.abspath(path)'''    
    abs_pathname = os.path.abspath("Checkvalue.py")
    print(abs_pathname)