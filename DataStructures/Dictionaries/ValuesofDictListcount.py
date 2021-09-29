'''
@Author: Rashmi
@Date: 2021-09-28 17:45
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 17:50
@Title :Write a Python program to count number of items in a dictionary value
that is a list.'''
if __name__ == '__main__': 
    '''Description :takes length of each values from dictionary and 
    adds values and prints the count of number  '''
    dict =  {'Alex': ['subj1', 'subj2', 'subj3',], 'David': ['subj1', 'subj2']}
    counter = sum(map(len, dict.values()))
    print(counter)