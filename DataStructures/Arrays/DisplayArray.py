'''
@Author: Rashmi
@Date: 2021-09-27 14:14
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 14:24
@Title : Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
'''
from array import *
if __name__ == '__main__': 
    '''Description : to create an array of 5 integers and display the array items.'''
    array_num = array('i', [1,3,5,7,9])
    for i in array_num:
        print(i)
    print("Access first three items individually using indexes")
    print(array_num[0])
    print(array_num[1])
    print(array_num[2])