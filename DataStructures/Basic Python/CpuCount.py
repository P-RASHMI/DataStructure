'''
@Author: Rashmi
@Date: 2021-09-26  10:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 10:20
@Title : Write a Python program to find out the number of CPUs using.

'''
import os
import multiprocessing

if __name__ == '__main__':

    '''Description : to print number of cpus using inbuilt cpu_count() of os and multiprocessing  '''
    print(multiprocessing.cpu_count())
    print(os.cpu_count())
