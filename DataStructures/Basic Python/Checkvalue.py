'''
@Author: Rashmi
@Date: 2021-09-24  21:58
@Last Modified by: Rashmi
@Last Modified time: 2021-09-24 22:30
@Title :Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

'''
   
def is_group_member(group_data, element):

    '''Description : to take list and find whether given input key is present or not'''

    for value in group_data:                     #takes each element from list 
        if element == value:                            #compares element with given key
           return True
    return False  
      
if __name__ == '__main__':

    print(is_group_member([1, 5, 8, 3], 3))
    print(is_group_member([5, 8, 3], -1))
    
