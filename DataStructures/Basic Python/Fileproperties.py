'''
@Author: Rashmi
@Date: 2021-09-26 17:23
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 17:25
@Title : Write a Python program to retrieve file properties
'''
import os.path
import time
if __name__ == '__main__': 
    '''Description :to get file properties like access time,modified time,change time,size
       '''
    print('File         :', __file__)
    print('Access time  :', time.ctime(os.path.getatime(__file__)))
    print('Modified time:', time.ctime(os.path.getmtime(__file__)))
    print('Change time  :', time.ctime(os.path.getctime(__file__)))
    print('Size         :', os.path.getsize(__file__))

