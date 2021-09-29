'''
@Author: Rashmi
@Date: 2021-09-28 18:35
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 18:44
@Title :Write a Python program to multiplies all the items in a list.'''
if __name__ == '__main__': 
    '''Description :for each element of list multiplies element with 
    initial and stores the mutlipied value prints values'''
    initial = 1
    list1 = [5,10,1,2]
    for element in list1:
        initial = element * initial
    print("multiplication of all elements in given list: ",initial)