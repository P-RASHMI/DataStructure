'''
@Author: Rashmi
@Date: 2021-09-28 20:44
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 20:57
@Title :Write a Python program to append a list to the second list.'''
if __name__ == '__main__':
    '''Description : appending two lists using append, + ,extend'''
    list1 = [1, 2, 3, 0]
    list2 = ['Red', 'Green', 'Black']
    final_list = list1 + list2  #using + operator
    print(final_list)
    list1.append(list2)     # appending adds the second list as single object at end of list
    print(list1)
    list1.extend(list2)    #extending adding each element of list2 as element into 
    print(list1)                       #list1 and extending the list1
    