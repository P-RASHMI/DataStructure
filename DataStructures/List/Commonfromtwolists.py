'''
@Author: Rashmi
@Date: 2021-09-28 21:06
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 21:11
@Title :Write a Python program to find common items from two lists.'''
if __name__ == '__main__':
    '''Description: converting to set and & operator for common elements printing'''
    color1 = ["Red", "Green", "Orange", "White"]
    color2 = ["Black", "Green", "White", "Pink"]
    print(set(color1) & set(color2))
