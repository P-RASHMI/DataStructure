'''
@Author: Rashmi
@Date: 2021-09-27 16:23
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 16:40
@Title :Write a Python program to unpack a tuple in several variables.
'''

if __name__ == '__main__': 
    '''Description :program to unpack a tuple in several variables'''
    #create a tuple
    tuple_given = 77,300,12
    print(tuple_given)
    n1, n2, n3 = tuple_given
    #unpack a tuple in variables
    print(n1 + n2 + n3) 
    #the number of variables must be equal to the number of items of the tuple
    n1, n2, n3, n4= tuple_given

    a = ("MNNIT Allahabad", 5000, "Engineering") 
    
    # this lines UNPACKS values
    # of variable a
    (college, student, type_ofcollege) = a 
    
    # print college name
    print(college)
    
    # print no of student
    print(student)
    
    # print type of college
    print(type_ofcollege)