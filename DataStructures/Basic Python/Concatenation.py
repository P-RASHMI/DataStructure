'''
@Author: Rashmi
@Date: 2021-09-25  23:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-25 23:43
@Title :. Write a Python program to concatenate all elements in a list into a string and return it
'''
def concatenate_list_data(list):

    '''Description : takes input list and for each element takes string and concatenates
       returns string  '''
    # using + operator ; str(element)--> convert int to string
    result= ''
    for element in list:
        result += str(element)
    return result

if __name__ == '__main__':

    '''Description : takes input concatenate to string by join() '''
    #concatenating using join ()
    given_list = ['hello', 'geek', 'have','a', '1', 'day']
    # this will join all the 
    # elements of the list with ' '
    given_list = ' '.join(given_list) 
    print(given_list)
    print(concatenate_list_data([1, 5, 12, 2])) #second method calling