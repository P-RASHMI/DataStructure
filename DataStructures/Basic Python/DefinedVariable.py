'''
@Author: Rashmi
@Date: 2021-09-26 18:00
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 18:10
@Title :Write a Python program to determine if variable is defined or not.
'''
if __name__ == '__main__': 
    '''Description : to determine if variable is defined or not using try and except.
 '''
    try:
        x = 1
    except NameError:
        print("Variable is not defined....!")
    else:
        print("Variable is defined.")
    try:
        y
    except NameError:
        print("Variable is not defined....!")
    else:
        print("Variable is defined.")
    