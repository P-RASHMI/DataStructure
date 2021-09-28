'''
@Author: Rashmi
@Date: 2021-09-26 18:23
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 18:37
@Title : Write a Python program to add leading zeroes to a string
'''
if __name__ == '__main__': 
    '''Description : program to add leading zeroes to a string using rjust(),zfill()'''
    test_string = 'TESTING DATA ' 
    # printing original string 
    print("The original string : " + str(test_string))  
    # No. of zeros required
    N = 4  
    # using rjust()
    # adding leading zero
    res = test_string.rjust(N + len(test_string), '0') 
    # print result
    print("The string after adding leading zeros using rjust(): " + str(res))
    res = test_string.zfill(N + len(test_string))
    # print result
    print("The string after adding leading zeros using zfill() : " + str(res))