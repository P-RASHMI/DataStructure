'''
@Author: Rashmi
@Date: 2021-09-28 19:44
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 19:56
@Title :Write a Python program to find the list of words that are longer than n from a
given list of words.'''

def long_words(n, str):
    '''Description: takes for much long words to be printed,string;takes empty list and 
    words greater than specified length appends words into list and returns list'''
    word_len = []
    txt = str.split(" ")
    for word in txt:
        if len(word) > n:
            word_len.append(word)
    return word_len	
if __name__ == '__main__':
    string1 = "hi hello welcome to python"
    print("given string : ",string1)
    print("the list of words greater the 3 from string")
    print(long_words(3,string1))
    