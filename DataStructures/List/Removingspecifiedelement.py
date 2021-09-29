'''
@Author: Rashmi
@Date: 2021-09-28 20:21
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 20:27
@Title :Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']'''
if __name__ == '__main__':

    '''Description: remove elements of indexes given(0,4,5) using loop for index and element 
    in color list prints only elements removing 0,4,5 indexes  '''

    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
    print("list after removing 0th 4th 5th element")
    print(color)
