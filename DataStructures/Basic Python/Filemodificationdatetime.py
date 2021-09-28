'''
@Author: Rashmi
@Date: 2021-09-26  12:12
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 12:16
@Title : Write a Python program to get file creation and modification date/times
'''
import os.path, time

if __name__ == '__main__': 
    '''Description : to get file creation and modification date/times .getmtime(), . getctime()'''      
    print("Last modified: %s" % time.ctime(os.path.getmtime("Filemodificationdatetime.py")))
    print("Created: %s" % time.ctime(os.path.getctime("Filemodificationdatetime.py")))
    