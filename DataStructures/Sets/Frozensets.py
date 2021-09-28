'''
@Author: Rashmi
@Date: 2021-09-27 23:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 23:14
@Title :Write a Python program to use of frozensets.
'''
if __name__ == '__main__': 
    '''Description :Frozensets being immutable it does not have method that add or remove elements.
    supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), 
    issuperset(), symmetric_difference() and union().'''
    set1 = frozenset([1, 2, 3, 4, 5])
    set2 = frozenset([3, 4, 5, 6, 7])
    #use isdisjoint(). Return True if the set has no elements in common with other. 
    print(set1.isdisjoint(set2))
    #use difference(). Return a new set with elements in the set that are not in the others.
    print(set1.difference(set2))
    #new set with elements from both x and y
    print(set1 | set2)