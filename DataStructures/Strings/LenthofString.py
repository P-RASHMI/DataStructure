'''
@Author: Rashmi
@Date: 2021-09-28 12:07
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 12:16
@Title :Write a Python program to calculate the length of a string.
'''
if __name__ == '__main__': 
    '''Description :to calculate the length of a string using len() and loop(count)'''
    str = input("Enter a string: ")
    # counter variable to count the character in a string
    counter = 0
    for element in str:
        counter = counter+1
    print("Length of the input string is:", counter)
    print("Length of the input string is using len():", len(str))