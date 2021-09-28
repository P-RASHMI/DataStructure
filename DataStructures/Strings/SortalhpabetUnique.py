'''
@Author: Rashmi
@Date: 2021-09-28 1:24
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 1:29
@Title :Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white'''

if __name__ == '__main__':
    items = input("Input comma separated sequence of words")
    words = [word for word in items.split(",")]
    print(",".join(sorted(list(set(words)))))

