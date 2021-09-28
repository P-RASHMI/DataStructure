'''
@Author: Rashmi
@Date: 2021-09-28 12:46
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 12:50
@Title :Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''
def add_string(str1):
    '''Description :getting lenth of string(str1) and if length < 3 string unchanged;string 
    ends with ing using slicing to know and add ly otherwise add ing ; returns string   '''
    length = len(str1)
    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1
if __name__ == '__main__': 
    print(add_string('ab'))
    print(add_string('abc'))
    print(add_string('string'))
