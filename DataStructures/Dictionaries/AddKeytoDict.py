'''
@Author: Rashmi
@Date: 2021-09-28 15:38
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 15:41
@Title :Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''
import operator
if __name__ == '__main__': 
    '''Description : add key value to dictionary using update() '''
    dictn = {0:10, 1:20}
    print("original dictionar",dictn)
    dictn.update({2:30})
    print("after adding ",dictn)