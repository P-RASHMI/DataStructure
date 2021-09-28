'''
@Author: Rashmi
@Date: 2021-09-27 14:45
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 15:12
@Title :Write a Python program to get the number of occurrences of a specified element in an
array.
'''
from array import *
if __name__ == '__main__': 
    '''Description : number of occurrences of a specified element in an
    array  using count()'''
    array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
    print("Original array: ",(array_num))
    num_search = int(input("enter the element to be searched "))  #the given input should be in int
    print(f"Number of occurrences of the number {num_search} in the array: ",
                          (array_num.count(num_search)))
