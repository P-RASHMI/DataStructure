'''
@Author: Rashmi
@Date: 2021-09-26 3:35
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 3:37
@Title : Write a Python program to get the current value of the recursion limit
'''
import sys     
if __name__ == '__main__': 
    '''Description :to get current value of the recursion limit using getrecursionlimit() '''  
    print("Current value of the recursion limit:")
    print(sys.getrecursionlimit())