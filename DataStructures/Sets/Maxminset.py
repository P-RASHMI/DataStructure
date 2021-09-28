'''
@Author: Rashmi
@Date: 2021-09-27 23:15
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 23:25
@Title :Write a Python program to find maximum and the minimum value in a set
'''
if __name__ == '__main__': 
    '''Description :finding max and min value using max(),min()'''
    setnum = {5, 10, 3, 15, 2, 20}
    print("Original set elements:")
    print(setnum)
    print(type(setnum))
    print("Maximum value of the said set:")
    print(max(setnum))
    print("Minimum value of the said set:")
    print(min(setnum))