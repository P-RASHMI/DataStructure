'''
@Author: Rashmi
@Date: 2021-09-27 20:33
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 20:41
@Title :Write a Python program to clear a set.
'''
if __name__ == '__main__': 
    '''Description :to clear a set using clear() it removes all elemnets'''
    set_element = {"Red", "Green", "Black", "White"}
    print("Original set elements:")
    print(set_element)        
    print("After removing all elements of the said set.")
    set_element.clear()
    print(set_element)