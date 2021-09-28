'''
@Author: Rashmi
@Date: 2021-09-26  11:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 11:40
@Title :Write a program to get execution time for a Python method.
'''
import time

if __name__ == '__main__': 
    '''Description : to get execution time we using time module'''      #can also use timeit() 
    begin = time.time()                          # store starting time
    # program body starts
    print("first five digits starting with zero : ")
    for number in range(5):                      # program body ends
        print(number)
        time.sleep(1)                                          
    end = time.time()                             # store end time 
    print(f"Total runtime of the program is {end - begin}")  # total time taken
