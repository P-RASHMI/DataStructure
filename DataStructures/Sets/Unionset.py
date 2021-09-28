'''
@Author: Rashmi
@Date: 2021-09-27 20:33
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 20:41
@Title :Write a Python program to create a union of sets.
'''
if __name__ == '__main__': 
    '''Description :to create a union of sets using union combination of both sets'''
    set1 = set(["hi", "pinky"])
    set2 = set(["how", "pinky"])
    print("Original sets:")
    print(set1)
    print(set2)
    set3 = set1.union(set2)
    print("Union of above sets:")
    print(set3)
    setn1 = set([1, 1, 2, 3, 4, 5])
    setn2 = set([1, 5, 6, 7, 8, 9])
    print("Original sets:")
    print(setn1)
    print(setn2)
    print("Union of above sets:")
    setn = setn1.union(setn2)
    print(setn)