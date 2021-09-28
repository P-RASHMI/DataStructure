'''
@Author: Rashmi
@Date: 2021-09-26 12:16
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 1:00
@Title :. Write a Python program to sort files by date
'''
import glob
import os
if __name__ == '__main__': 
    '''Description :program to sort files by date using ,glob(),sort method and getmtime '''  
    files = glob.glob("*.py")      #glob() to return all files/pathnames matching specific pattern
    files.sort(key=os.path.getmtime)   #sorting based on modified time,gives  ascending order
    print("\n".join(files))    # using join with \n to print files in new lines
