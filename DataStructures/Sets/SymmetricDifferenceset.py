'''
@Author: Rashmi
@Date: 2021-09-27 20:33
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 20:41
@Title :Write a Python program to create a symmetric difference
'''
if __name__ == '__main__': 
    '''Description :to create a symmetric difference using symmetric_difference(),
    using ^ operator; gives elements of both sets subtracting the common elements'''
    set1 = set(["hi", "pinky"])
    set2 = set(["how", "pinky"])
    print("Original sets:")
    print(set1)
    print(set2)
    set3 = set1.symmetric_difference(set2)
    print("difference of set1 and set2:")
    print(set3)
    setnum1 = set([1, 1, 2, 3, 4, 5])
    setnum2 = set([1, 5, 6, 7, 8, 9])
    print("Original sets:")
    print(setnum1)
    print(setnum2)
    print("difference of setnum1 and setnum2:")
    setnum = setnum1^setnum2
    print(setnum)