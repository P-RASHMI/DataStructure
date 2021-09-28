'''
@Author: Rashmi
@Date: 2021-09-26  2:55
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 2:
@Title :Write a python program to call an external command in Python.
'''
import os
from subprocess import call
if __name__ == '__main__':

    '''Description : to call an external command in Python. '''
#print(os.system('ipconfig')) # using os
call(["ipconfig"])            # using subprocess call
