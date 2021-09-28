'''
@Author: Rashmi
@Date: 2021-09-27 18:36
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 18:47
@Title :Write a Python program to reverse a tuple.
'''
if __name__ == '__main__': 
    '''Description :to reverse a tuple using reversed and convert to tuple  '''
    #create a tuple
    tuple1 = ('Hi','Rashmi')
    # Reversed the tuple
    tuple2 = reversed(tuple1)
    print("reversed:1st tuple",tuple(tuple2))
    tuple3 = ('Rashmi')
    tuple4 = reversed(tuple3)
    print("reversed: 2nd tuple ",tuple(tuple4))
    #create another tuple
    tuple_new = (200,80,11,20)
    # Reversed the tuple
    refer_obj = reversed(tuple_new)
    print("reversed integers",tuple(refer_obj))