'''
@Author: Rashmi
@Date: 2021-09-26 18:23
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 18:37
@Title : Write a Python program to find files and skip directories of a given directory
'''
import os
if __name__ == '__main__': 
    '''Description : to find files and skip directories of a given directory'''
    user_path = 'C:\\Users\\Charishma\\Desktop\\rashmi\\PYTHONWORK\\DataStructures'
    for fname in os.listdir(user_path):
        path = os.path.join(user_path, fname)
        if os.path.isdir(path):
        # skip directories
            continue
    # print the file names
        print(fname)