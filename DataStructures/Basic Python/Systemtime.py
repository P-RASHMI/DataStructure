'''
@Author: Rashmi
@Date: 2021-09-26 3:40
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 3:53
@Title : Write a Python program to get the system time.
'''
import time
import datetime
if __name__ == '__main__': 
    '''Description : to get the system time using ctime() or can use datetime.now()''' 
    print(time.ctime())
    print(datetime.datetime.now()) 
    