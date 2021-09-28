'''
@Author: Rashmi
@Date: 2021-09-28 1:44
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 1:54
@Title :Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python'''

if __name__ == '__main__':
    str1 = 'https://www.w3resource.com/python-exercises/string'
    print(str1.rsplit('/', 1)[0])
    print(str1.rsplit('-', 1)[0])