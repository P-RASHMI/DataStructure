'''
@Author: Rashmi
@Date: 2021-09-28 16:16
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 16:26
@Title :Write a Python program to remove a key from a dictionary'''
if __name__ == '__main__': 
    '''Description : deletion using if  statement , by using pop()'''
    myDict = {'a':1,'b':2,'c':3,'d':4}
    print(myDict)
    if 'c' in myDict: 
        del myDict['c']
    print("dictionary after deleting given key",myDict)
    myDict.pop('b')
    print("dictionary after deleting using pop()",myDict)
