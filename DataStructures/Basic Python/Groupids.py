'''
@Author: Rashmi
@Date: 2021-09-26 4:45
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 4:57
@Title : Write a Python program to get system command output.
'''
import os
if __name__ == '__main__': 
    '''Description :to get system command output using subprocess'''
    print("\nEffective group id: ",os.getegid())
    print("Effective user id: ",os.geteuid())
    print("Real group id: ",os.getgid())
    print("List of supplemental group ids: ",os.getgroups())
    print()
