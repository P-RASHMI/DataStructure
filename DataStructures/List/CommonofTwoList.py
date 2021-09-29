'''
@Author: Rashmi
@Date: 2021-09-28 20:04
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 20:11
@Title :Write a Python function that takes two lists and returns True if they have at
least one common member.'''
def test_includes_any(list1, list2):
    '''Description: checks each element of list1 present in list1 and checks the same 
    element present in list2 then returns true if present;finally if both lists has common elements 
    returns true '''
    for num in list1:
        if num in list2:
            return True
    return False   
if __name__ == '__main__': 
    print(test_includes_any([10, 20, 30, 40, 50, 60], [22, 42]))
    print(test_includes_any([10, 20, 30, 40, 50, 60], [20, 80]))
