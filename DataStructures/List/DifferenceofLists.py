'''
@Author: Rashmi
@Date: 2021-09-28 20:35
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 20:44
@Title :Write a Python program to get the difference between the two lists.'''
if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2=[1, 2, 4, 6, 7, 8]
    diff_list1_list2 = list(set(list1) - set(list2))
    print(diff_list1_list2)
    diff_list2_list1 = list(set(list2) - set(list1))
    print(diff_list2_list1)
    total_diff = diff_list1_list2 + diff_list2_list1
    print(total_diff)
