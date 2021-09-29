'''
@Author: Rashmi
@Date: 2021-09-28 16:47
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 16:57
@Title :Write a Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True'''

if __name__ == '__main__': 
    student = [{'id': 1, 'success': True, 'name': 'Lary'},
                {'id': 2, 'success': False, 'name': 'Rabi'},
                {'id': 3, 'success': True, 'name': 'Alex'}]
    print(sum(dic['id'] for dic in student))
    print(sum(dic['success'] for dic in student))
    