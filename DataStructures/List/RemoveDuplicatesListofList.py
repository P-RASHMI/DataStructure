'''
@Author: Rashmi
@Date: 2021-09-28 21:17
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 21:21
@Title :Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]'''
import itertools
if __name__ == '__main__':
    num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print("Original List", num)
    num.sort()
    new_num = list(num for num,_ in itertools.groupby(num))
    print("New List", new_num)
