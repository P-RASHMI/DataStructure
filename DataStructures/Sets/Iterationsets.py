'''
@Author: Rashmi
@Date: 2021-09-27 18:56
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 19:25
@Title :Write a Python program to iteration over sets
'''
if __name__ == '__main__': 
    '''Description :iteration over sets using loop;sets unordered so values printing order changes '''
    # Creating a set using string
    test_set = set(("hi","hello","how","what"))
    # Iterating using for loop
    print("printing set values using loop")
    for val in test_set:
        print(val)
    #Create a another integer set 
    num_set = set([0, 1, 2, 3, 4, 5])
    for num in num_set:
        print(num, end=' ')