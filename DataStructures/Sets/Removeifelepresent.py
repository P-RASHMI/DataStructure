'''
@Author: Rashmi
@Date: 2021-09-27 19:51
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 19:55
@Title :Write a Python program to remove an item from a set if it is present in the set.
'''
if __name__ == '__main__': 
    '''Description :remove element if its present otherwise prints same set using discard()'''
    num_set = set([32,88,1,4,18])
    print("Original set elements:")
    print(num_set)
    print("Remove 32 from the said set:")
    num_set.discard(32)
    print(num_set)
    print("Remove 100 from the said set:")
    num_set.discard(100)
    print(num_set)