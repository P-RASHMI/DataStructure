'''
@Author: Rashmi
@Date: 2021-09-28 21:11
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 21:17
@Title :Write a Python program to split a list based on first character of word.'''
from itertools import groupby
from operator import itemgetter
if __name__ == '__main__':
    word_list = ['hai','hello','about','as','below','be','good']
    for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(word)
