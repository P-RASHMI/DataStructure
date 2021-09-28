'''
@Author: Rashmi
@Date: 2021-09-27 16:56
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 17:03
@Title : Write a Python program to find the repeated items of a tuple.
'''
from copy import deepcopy
if __name__ == '__main__': 
    '''Description :the count of repeatition of the element in tuple by using count() '''
    #create a tuple
    given_tuple = 15,22,78,1,2,4,15,22,78,5,5,5,5
    print(given_tuple)
    number = int(input("enter the number to get its repetition count"))
    #return the number of times it appears in the tuple.
    count = given_tuple.count(number)
    print(f"count of {number} repeated in tuple is")
    print(count)