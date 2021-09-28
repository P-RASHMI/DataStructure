'''
@Author: Rashmi
@Date: 2021-09-26 18:45
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 19:09
@Title : Write a Python program to convert an integer to binary keep leading zeros.
Sample data : 12
Expected output : 00001100, 0000001100
'''

if __name__ == '__main__': 
    '''Description :to convert an integer to binary keep leading zeros.format(num, name) 
    function with name as "0nb" to convert an integer num to a binary string with 
    leading zeros up to length n'''
    number = 12           
    print(format(number, '08b')) # 0nb--> adds zero
    print(format(number, '06b'))
