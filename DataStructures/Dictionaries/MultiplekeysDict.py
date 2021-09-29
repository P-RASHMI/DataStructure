'''
@Author: Rashmi
@Date: 2021-09-28 17:27
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 17:42
@Title :Write a Python program to check multiple keys exists in a dictionary.'''
if __name__ == '__main__': 
    '''Description : to check multiple keys present or not '''
    student = {'name': 'Rashmi','course': 'python','roll_id':2}
    print(student.keys() >= {'course', 'name'})
    print(student.keys() >= {'name', 'Rashmi'})
    print(student.keys() >= {'roll_id', 'name'})
