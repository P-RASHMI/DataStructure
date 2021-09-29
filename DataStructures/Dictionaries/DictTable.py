'''
@Author: Rashmi
@Date: 2021-09-28 16:47
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 16:57
@Title :. Write a Python program to print a dictionary in table format.'''
if __name__ == '__main__': 
    '''Description :printing using loop'''
    # Insert data into dictionary
    dict1 = {1: ["Samuel", 21, 'Data Structures'],
        2: ["Richie", 20, 'Machine Learning'],
        3: ["Lauren", 21, 'OOPS with java'],
        }
    # Print the names of the columns.
    print ("{} {} {}".format('NAME', 'AGE', 'COURSE'))
    # print each data item.
    for key, value in dict1.items():
        name, age, course = value
        print ("{} {} {}".format(name, age, course))