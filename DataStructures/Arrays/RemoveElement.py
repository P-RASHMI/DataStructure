'''
@Author: Rashmi
@Date: 2021-09-27 14:45
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 15:12
@Title :Write a Python program to remove the first occurrence of a specified element from an
array.
'''
from array import *
if __name__ == '__main__': 
    '''Description : to remove the first occurrence of a specified element from an
    array using remove()'''
    array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
    print("Original array: ",(array_num))
    num_search = int(input("enter the element to be removed "))  #the given input should be in int
    print(f"removed the first occurence of {num_search} from array: ")
    array_num.remove(num_search)
    print("New array: ",(array_num))