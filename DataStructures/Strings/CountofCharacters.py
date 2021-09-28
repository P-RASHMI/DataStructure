'''
@Author: Rashmi
@Date: 2021-09-28 12:07
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 12:16
@Title :Write a Python program to count the number of characters (character frequency) in a
string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
def char_frequency(str1):
    '''Description :for each char in string takes char as key,initially each char counted as 1 
    and with repetition of char increase the number value of the char key of dictionary and finally 
    returns dictionary'''
    dict = {}
    for num in str1:            #for each char in string takes char as key
        keys = dict.keys()
        if num in keys:
            dict[num] += 1
        else:
            dict[num] = 1        #initially each char counted as 1 and with repetition of char increase the number
    return dict
    
if __name__ == '__main__': 
    print(char_frequency('google.com'))