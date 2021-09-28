'''
@Author: Rashmi
@Date: 2021-09-26 19:09
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 19:22
@Title : Write a Python function to find the maximum and minimum numbers from a sequence of
numbers.
Note: Do not use built-in functions.
'''
def max_min(data):
    max = data[0]
    min = data[0]
    for num in data:
        if num> max:
            max = num
        elif num< min:
            min = num
    return min, max
    
if __name__ == '__main__': 
    '''Description :to find the maximum and minimum numbers from a sequence of
numbers.'''
    print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))

