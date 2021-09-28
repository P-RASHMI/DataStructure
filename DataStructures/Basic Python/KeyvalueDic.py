'''
@Author: Rashmi
@Date: 2021-09-26 18:45
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 18:57
@Title : Write a Python program to extract single key-value pair of a dictionary in variables.
'''

if __name__ == '__main__': 
    '''Description : to extract single key-value pair of a dictionary in variables 
    indexing values printing key and its value'''
    dict = {'key1': 'hi', 'key2': 'hello', 'key3': 'world', 'key4': 'vs'}
    print("Extract specific key, value")
    x, y = list(dict.items())[3]
    print(x, y)