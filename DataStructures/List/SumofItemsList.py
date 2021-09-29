'''
@Author: Rashmi
@Date: 2021-09-28 17:55
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 18:35
@Title :Write a Python program to sum all the items in a list.'''
if __name__ == '__main__': 
    '''Description :for each element of list adds element and prints total values'''
    total = 0
    list1 = [11, 5, 17, 18, 23]
    for ele in range(0, len(list1)):
        total = total + list1[ele]
    print("Sum of all elements in given list: ", total)