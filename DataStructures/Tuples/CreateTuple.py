'''
@Author: Rashmi
@Date: 2021-09-27 15:43
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 15:55
@Title :Write a Python program to create a tuple.
'''

if __name__ == '__main__': 
    '''Description : to create a tuple '''
    #one way of creating tuple
    my_tuple = ('apple', 'banana', 'cherry')
    print("given tuple",my_tuple)
    print(type(my_tuple))
    #another way is by using tuple key word
    thistuple = tuple(('hi', 'hello', 'cherry')) # note the double round-brackets
    print(thistuple)
    print(type(thistuple))  
    tuple_given = tuple((1,2,3))
    print("given tuple",tuple_given,type(tuple_given))
    
