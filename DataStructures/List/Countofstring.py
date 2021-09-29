'''
@Author: Rashmi
@Date: 2021-09-28 18:53
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 18:59
@Title :Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''

def match_words(words):
    '''Description :to get number of words(strings) from list whose length >=2 
    and in that word first,last character is same'''
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr
if __name__ == '__main__': 
    print(match_words(['abc', 'xyz', 'aba', '1221','helloh'])) 







