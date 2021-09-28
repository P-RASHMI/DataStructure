'''
@Author: Rashmi
@Date: 2021-09-28 2:32
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 2:53
@Title :. Write a Python program to lowercase first n characters in a string'''

if __name__ == '__main__':

    str1 = "PULMAMIDI RASHMI"
    num = int(input("Enter the how many letter you want in lower case: "))
    print(str1[:num].lower() + str1[num:])  # concatenating to print whole string 