'''
@Author: Rashmi
@Date: 2021-09-27 17:26
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 17:49
@Title :. Write a Python program to remove an item from a tuple.
'''
if __name__ == '__main__': 
    '''Description : to remove an item from a tuple by coverting into list,
    another by merging tuples by slicing excluding element'''
    tuple1= (4,3,5,13,80,25,100)   #create a tuple
    print(tuple1)          #tuples are immutable, so you can not remove elements
    tuplex = tuple1[:2] + tuple1[3:] #merge with + operator #upperlimit-1(excludes one)
    print("tuple after removing element")
    print(tuplex)                    #you can remove an item and it will create a new tuple
    #another way by converting the tuple to list
    listx = list(tuplex) 
    listx.remove(25) 
    tuplex = tuple(listx)
    print("after removing 25 ", tuplex)




