'''
@Author: Rashmi
@Date: 2021-09-26  10:57
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 11:30
@Title :Write a Python program to get the current username.
'''
import getpass
import os
if __name__ == '__main__': 
    '''Description : to get current username using getpass.getuser(), os.getlogin()'''
    username = getpass.getuser()
    print(username)
    current_user = os.getlogin()
    print(current_user)