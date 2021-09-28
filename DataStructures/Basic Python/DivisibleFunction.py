'''
@Author: Rashmi
@Date: 2021-09-26 17:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 17:45
@Title :Write a Python program to get numbers divisible by fifteen from a list using an anonymous
function.
'''
if __name__ == '__main__': 
    '''Description :to get take list of numbers, get divisible by fifteen from a list using an anonymous
    function '''
    num_list = [45, 55, 60, 37, 100, 105, 220]
    # use anonymous function to filter
    result = list(filter(lambda x: (x % 15 == 0), num_list))
    print("Numbers divisible by 15 are",result)