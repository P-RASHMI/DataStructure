'''
@Author: Rashmi
@Date: 2021-09-27 17:15
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 17:19
@Title : Write a Python program to check whether an element exists within a tuple.
'''
from copy import deepcopy
if __name__ == '__main__': 
    '''Description : to check whether an element exists within a tuple us in operator 
    returns boolean value '''
    given_tuple = (4,3,5,13,"s",25,100)
    print("s" in given_tuple)
    print(25 in given_tuple)
    print(22 in given_tuple)
