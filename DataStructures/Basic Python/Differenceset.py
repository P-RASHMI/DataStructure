'''
@Author: Rashmi
@Date: 2021-09-26  1:53
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 2:05
@Title :Write a Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"]
Expected Output :
{'Black', 'White'}
'''
if __name__ == '__main__':

    '''Description : to print only from one set by removing the common elements from another set using
    difference() method '''
    #The returned set contains items that exist only in the first set, and not in both sets.
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print("Original set elements:")
    print(color_list_1)
    print(color_list_2)
    print("\nDifferenct of color_list_1 and color_list_2:")
    print(color_list_1.difference(color_list_2))
    