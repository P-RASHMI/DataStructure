'''
@Author: Rashmi
@Date: 2021-09-24 16:24
@Last Modified by: Rashmi
@Last Modified time: 2021-09-24 16:30
@Title : Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

if __name__ == '__main__':

    '''Description : takes input seperated by comma and print tuples and list'''
   #split function helps in getting multiple inputs from the user. 
   # It breaks the given input by the specified separator. 
    values = input("enter Input with comma seperated numbers : ").split(",")  #takes input and generates list
    print('the generated List: ',values)
    tuple = tuple(values)                   #generated list passed and gets tuples
    print('generated Tuple : ',tuple)