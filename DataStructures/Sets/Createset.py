'''
@Author: Rashmi
@Date: 2021-09-27 18:56
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 19:11
@Title :Write a Python program to create a set.
'''
if __name__ == '__main__': 
    '''Description :to create a set of empty,non empty and literal elements using set() '''
    print("Create a new set:")
    given_element = set()
    print(given_element)
    print(type(given_element))
    print("\nCreate a non empty set:")
    number_elements = set([12, 35, 2, 3, 4])
    print(number_elements)
    print(type(number_elements))
    print("\nUsing a literal:")
    literal_elements = {1,2,3,'foo','bar'}
    print(type(literal_elements))
    print(literal_elements)