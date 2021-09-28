'''
@Author: Rashmi
@Date: 2021-09-27 19:57
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 20:
@Title :Write a Python program to create an intersection of sets.
'''
if __name__ == '__main__': 
    '''Description :to create an intersection of sets using & operator and intersection 
    common elements of both sets'''
    set1 = set(["hi", "pinky"])
    set2 = set(["how", "pinky"])
    print("Original set elements:")
    print(set1)
    print(set2)
    print("Intersection of two said sets:")
    set_intersect = set1 & set2
    print(set_intersect)
    #another way
    result = set1.intersection(set2)
    print("using intersection",result)