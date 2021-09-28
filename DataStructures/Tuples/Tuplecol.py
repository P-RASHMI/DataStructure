'''
@Author: Rashmi
@Date: 2021-09-27 16:48
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 16:52
@Title : Write a Python program to create the colon of a tuple
'''
from copy import deepcopy
if __name__ == '__main__': 
    '''Description :to create the colon of a tuple using deepcopy()'''
    #create a tuple
    tuple_given = ("HELLO", 800, [], True) 
    print(tuple_given)
    #make a copy of a tuple using deepcopy() function
    tuple_colon1 = deepcopy(tuple_given)
    tuple_colon1[2].append(50)
    print(tuple_colon1)
    print(tuple_given)

