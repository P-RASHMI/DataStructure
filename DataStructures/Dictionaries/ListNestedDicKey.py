'''
@Author: Rashmi
@Date: 2021-09-28 17:00
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 17:24
@Title :Write a Python program to convert a list into a nested dictionary of keys.'''
if __name__ == '__main__': 
    num_list = [1, 2, 3, 4]
    new_dict = current = {}  #two empty dictionaries
    for element in num_list:
        current[element] = {}  #creating another empty dictionary for each element
        current = current[element] #appending that dictionary into first empty dictionary
    print(new_dict)