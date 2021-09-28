'''
@Author: Rashmi
@Date: 2021-09-26 18:07
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 18:13
@Title :Write a Python program to empty a variable without destroying it.
'''
if __name__ == '__main__': 
    '''Description : to take the given input and empty variables by using type()
       type() returns the type of an object, which when called produces an 'empty' new value.
 '''
    number = 20
    dict_given = {"x":200}
    list_given = [1,3,5]
    tuple_given= (5,7,8)
    print(type(number)())
    print(type(dict_given)())
    print(type(list_given)())
    print(type(tuple_given)())