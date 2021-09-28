'''
@Author: Rashmi
@Date: 2021-09-26 19:09
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 19:22
@Title : Write a Python program to determine if the python shell is executing in 32bit or 64bit mode
on operating system.
'''
import struct
if __name__ == '__main__': 
    '''Description :to determine if the python shell is executing in 32bit or 64bit mode
    on operating system using .calcsize()'''
    print(struct.calcsize("P") * 8)
