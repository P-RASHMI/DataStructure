'''
@Author: Rashmi
@Date: 2021-09-28 19:07
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 19:20
@Title :Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''

def last(num):
    '''Description :takes each tuple and get the last element of tuple and return last element'''
    return num[-1]  
   
def sort(tuples):
    '''Description : takes each tuple from list and
    sort based on last element of each tuple(key=last),returns sorted tuple'''
    return sorted(tuples, key=last)

if __name__ == '__main__': 
    '''Description : takes list of tuples and sort based on the last value of each tuple by using
    two functions last,sort'''   
    list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(list1)
    print("Sorted:")
    print(sort(list1))  