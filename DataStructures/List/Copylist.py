'''
@Author: Rashmi
@Date: 2021-09-28 19:35
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 19:44
@Title :Write a Python program to clone or copy a list'''
if __name__ == '__main__':
    original_list = [10, 22, 44, 23, 4]
    new_list = list(original_list)
    print("original list ",original_list)
    print("copied list ",new_list)