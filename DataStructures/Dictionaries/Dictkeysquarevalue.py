'''
@Author: Rashmi
@Date: 2021-09-28 16:00
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 16:11
@Title :Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''
if __name__ == '__main__': 
    '''Description : to get dictionary of key,(square of key as)values from 1 to given input
    here using for loop for each integer starting from 1  '''
    num=int(input("Enter the number till which key to get dictionary"))
    dictn = dict()
    for element in range(1,num+1):
        dictn[element]=element*element
    print("squared dictionary values",dictn) 