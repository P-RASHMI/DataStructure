'''
@Author: Rashmi
@Date: 2021-09-28 15:00
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 15:34
@Title :Write a Python script to sort (ascending and descending) a dictionary by
value.'''
import operator
if __name__ == '__main__': 
    '''Description : using operator.itemgetter() to get items from operand's method
    returns in tuple format,sorting values using sorted();another method is by using 
    functions to get values and keys,sorted based on values '''
    #using operator.itemgetter(n)
    dictn = {'two': 2, 'four': 4, 'three': 3, 'one': 1, 'zero': 0}
    print('Original dictionary : ',dictn)
    sorted_dictn = sorted(dictn.items(), key=operator.itemgetter(1)) #ascending order by using itemgetter()
    print('Dictionary in ascending order by value : ',sorted_dictn) #below descending order 
    sorted_dictn = dict(sorted(dictn.items(), key=operator.itemgetter(1),reverse=True))
    print('Dictionary in descending order by value : ',sorted_dictn)
    #using item functions ,sorted()
    my_dict = {5: 3,4:1,12:4,15:2}
    # Sorting dictionary
    sorted_dict = sorted([(value, key)
                    for (key, value) in my_dict.items()])
    # Print sorted dictionary
    print("Sorted dictionary of dictionary:",my_dict)
    print("ascending order by value in value key format :",sorted_dict)
    print("descending order by value",sorted(sorted_dict,reverse=True))