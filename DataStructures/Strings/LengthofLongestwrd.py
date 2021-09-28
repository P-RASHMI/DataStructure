'''
@Author: Rashmi
@Date: 2021-09-28 1:06
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 1:13
@Title :. Write a Python function that takes a list of words and returns the length of the longest
one'''
def longestLength(string1):
    '''Description :store length of first element in max1,element into temp using for loop 
    to store max element length in max1 and element in temp and print both'''
    max1 = len(string1[0])
    temp = string1[0]
    # for loop to traverse the list
    for element in string1:
        if(len(element) > max1):
            max1 = len(element)
            temp = element
    print("The word with the longest length is:", temp,
          " and length is ", max1)
if __name__ == '__main__': 
    string1 = ["hi","hello","rashmi"]
    print(string1)
    longestLength(string1)