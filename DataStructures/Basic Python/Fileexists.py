'''
@Author: Rashmi
@Date: 2021-09-26  2:05
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 2:30
@Title :Write a Python program to check whether a file exists.
'''
import os.path
if __name__ == '__main__':

    '''Description : to check whether a file exists using os.path.isfile() ,os.path.exists()
       returns boolean '''
print(os.path.isfile('Docstring.py'))
print(os.path.isfile('main.py'))
print(os.path.exists('Fileexists.py'))
print(os.path.exists('main.py'))

