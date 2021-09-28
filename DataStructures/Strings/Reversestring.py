'''
@Author: Rashmi
@Date: 2021-09-28 2:32
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 2:53
@Title :Write a Python program to reverse a string.'''

def string_reverse(str1):
    '''Description :rstr1 as empty and for string length >0 loops to
    store the string from last and decrement length and return the reversed string '''
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
    
if __name__ == '__main__':
    print(string_reverse('Rashmi'))