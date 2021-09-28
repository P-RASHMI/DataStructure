'''
@Author: Rashmi
@Date: 2021-09-26 3:20
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 3:28
@Title : Write a Python program to get the size of an object in bytes.
'''
import sys     
if __name__ == '__main__': 
    '''Description :to get the size of an object in bytes using getsizeof() '''  
    number=sys.getsizeof(12) 
    print(number)   
    string=sys.getsizeof('rashmi')
    print(string) 
    tuple=sys.getsizeof(('r','a','s','h','m'))
    print(tuple)   
    list=sys.getsizeof(['r','a','s','h','m'])
    print(list)
    set=sys.getsizeof({1,2,3,4})
    print(set)
    dic=sys.getsizeof({1:'a',2:'b',3:'c',4:'d'})
    print(dic)