'''
@Author: Rashmi
@Date: 2021-09-27 20:41
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 20:50
@Title :Write a Python program to create set difference.
'''
if __name__ == '__main__': 
    '''Description :to create set difference using difference prints first set 
    elements removing common elements of two sets'''
    set1 = set(["hi", "pinky"])
    set2 = set(["how", "pinky"])
    print("Original sets:")
    print(set1)
    print(set2)
    set3 = set1.difference(set2)
    print("difference of set1 and set2:")
    print(set3)
    setnum1 = set([1, 1, 2, 3, 4, 5])
    setnum2 = set([1, 5, 6, 7, 8, 9])
    print("Original sets:")
    print(setnum1)
    print(setnum2)
    print("difference of setnum1 and setnum2:")
    setnum = setnum1.difference(setnum2)
    print(setnum)