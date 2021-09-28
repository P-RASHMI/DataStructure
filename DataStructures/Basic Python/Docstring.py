'''
@Author: Rashmi
@Date: 2021-09-24 20:40
@Last Modified by: Rashmi
@Last Modified time: 2021-09-24 21:30
@Title : Write a Python program to print the documents (syntax, description etc.) of Python built-in
function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''
def absolute_value(number):

    '''Description : to print the absolute value of number using abs()
    
       parameter : int argument,number
       returns : absolute value'''  
    positive_number = abs(number)                #inbuilt abs() to convert to positive value
    print(positive_number)
    return positive_number 

if __name__ == '__main__':
    number = int(input("enter value of negative number"))
    cal = absolute_value(number)
    print(absolute_value.__doc__)              #prints description
    help(absolute_value)                       # has same function of doc

  