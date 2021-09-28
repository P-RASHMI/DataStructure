'''
@Author: Rashmi
@Date: 2021-09-27 19:26
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 19:36
@Title :Write a Python program to add member(s) in a set.
'''
if __name__ == '__main__': 
    '''Description :add member(s) in a set using add(),checks whether adding element present in set or 
    not if it is present won't add element otherwise adds element '''
    elements = {6, 0, 4}
    print("the list of set elements",elements)
    # adding 1
    elements.add(5)
    print("after adding 5 element in set",elements)
    # adding 6
    elements.add(6)
    print("trying to add 6 but set has no duplicates",elements)
   