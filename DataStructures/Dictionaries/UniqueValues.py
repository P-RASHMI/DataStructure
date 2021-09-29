'''
@Author: Rashmi
@Date: 2021-09-28 16:29
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 16:39
@Title :Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}'''

if __name__ == '__main__': 
    '''Description :returning values which are unique by using set and for loop'''
    List1 = [{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},
               {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]            #list
    print("Original List: ",List1)
    u_value = set( val for dic in List1 for val in dic.values())
    print("Unique Values: ",u_value)