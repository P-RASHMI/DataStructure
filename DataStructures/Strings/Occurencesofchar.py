'''
@Author: Rashmi
@Date: 2021-09-28 12:17
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 12:46
@Title :Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t
'''
def change_char(str1):
    '''Description :stores 0 index into char and replaces char(where r is present)
    with $ in the given string and concatenates char(r) with index1 to end of string
    returns resta$t  '''
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    return str1

if __name__ == '__main__': 
    print(change_char('restart'))