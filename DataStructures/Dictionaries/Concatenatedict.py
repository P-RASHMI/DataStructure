'''
@Author: Rashmi
@Date: 2021-09-28 15:41
@Last Modified by: Rashmi
@Last Modified time: 2021-09-28 15:51
@Title :Write a Python script to concatenate following dictionaries to create a new
one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''
if __name__ == '__main__': 
    '''Description : concatenating dictionaries using update() '''
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    dic4 = {}   #empty dictionary
    for dictionary in (dic1, dic2, dic3): 
        dic4.update(dictionary)
    print("concatenated dictionary",dic4)