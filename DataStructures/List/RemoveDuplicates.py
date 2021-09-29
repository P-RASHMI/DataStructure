'''
@Author: Rashmi
@Date: 2021-09-28 19:25
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 19:35
@Title :Write a Python program to remove duplicates from a list.'''

def remove(duplicate):
    '''Description:create an empty list and for each element loop if that element not present in
    created  list then append that element to newly created list and return the list '''
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
if __name__ == '__main__':
    duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
    print("given list",duplicate)
    print("list after removing duplicates using set",list(set(duplicate)))
    print("list after removing duplicates using loop",remove(duplicate))