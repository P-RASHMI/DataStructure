'''
@Author: Rashmi
@Date: 2021-09-27 19:26
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 19:36
@Title :Write a Python program to remove item(s) from set
'''
if __name__ == '__main__': 
    '''Description :Write a Python program to remove item(s) from set using pop()-->first element,
    remove()-->particular element '''
    num_set = set([22, 12, 31, 4, 18])
    print("Original set:")
    print(num_set)
    num_set.pop()
    print("After removing the first element from the said set:")
    print(num_set)
    num_set.remove(18)
    print("After removing the 18 element from the said set:")
    print(num_set)