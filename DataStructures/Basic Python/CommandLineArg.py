'''
@Author: Rashmi
@Date: 2021-09-26 1:00
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 1:20
@Title :. Write a Python program to get the command-line arguments (name of the script, the number
of arguments, arguments) passed to a script.
'''
import sys
if __name__ == '__main__': 
    '''Description :reads from command prompt and prints name and number of arguments, 
    all arguments using sys.argv  '''     
    print("This is the name/path of the script:"),sys.argv[0]
    print("Number of arguments:",len(sys.argv))
    print("Argument List:",str(sys.argv))