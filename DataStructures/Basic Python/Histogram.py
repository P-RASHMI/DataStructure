'''
@Author: Rashmi
@Date: 2021-09-24  22:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-24 22:40
@Title :Write a Python program to create a histogram from a given list of integers.
'''
   
def histogram(items):

    '''Description : to take values and print the histogram according to values'''
    for number in items:   # each element of item input
        output = ''
        times = number
        while( times > 0 ):
          output += '*'       #add * for every number
          times = times - 1    # decrement the number 
        print(output)

if __name__ == '__main__':
    histogram([1,2,4,5,1])    