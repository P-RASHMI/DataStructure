'''
@Author: Rashmi
@Date: 2021-09-26 1:54
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 2:10
@Title : Write a Python program to find the available built-in modules
'''
import sys
import textwrap
if __name__ == '__main__': 
    '''Description :finding available built in modules '''  
    module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))