'''
@Author: Rashmi
@Date: 2021-09-26 4:45
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 4:57
@Title : Write a Python program to get system command output.
'''
import subprocess
if __name__ == '__main__': 
    '''Description :to get system command output using subprocess'''
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)