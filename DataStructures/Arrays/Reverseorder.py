'''
@Author: Rashmi
@Date: 2021-09-27 14:25
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 14:45
@Title :Write a Python program to reverse the order of the items in the array.
'''
from array import *
if __name__ == '__main__': 
    '''Description : to reverse the order of the items in the array using reverse(), slicing'''
    array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
    print("Original array: ",array_num)
    array_num2 = array_num[::-1]
    print("reverse of array using slicing",array_num2)
    print("Original array: ",array_num)
    array_num.reverse()
    print("Reversed order of the items using reverse() is :")
    print(array_num)
