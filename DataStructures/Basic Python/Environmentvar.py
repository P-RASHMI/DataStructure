'''
@Author: Rashmi
@Date: 2021-09-26  10:57
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 10:
@Title : Write a python program to access environment variables.
'''
import os
if __name__ == '__main__': 
    '''Description : to get access environment variable using environ method'''
# printing environment variables
    print(os.environ)
    print()
    print()
    print(os.environ['TEMP'])    #access particular environment variable
    print()
    print()
    for key, value in os.environ.items(): #printing variable and its value using loop
       print(f'{key}={value}')