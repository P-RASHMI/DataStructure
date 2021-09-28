'''
@Author: Rashmi
@Date: 2021-09-27 17:49
@Last Modified by: Rashmi
@Last Modified time: 2021-09-27 18:15
@Title : Write a Python program to slice a tuple
'''
if __name__ == '__main__': 
    '''Description : slice a tuple with different ways'''
    #create a tuple
    tup = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
    #used tuple[start:stop] the start index is inclusive and the stop index
    slice = tup[3:5]   #(starts index from zero and excludes upper limit)
    #is exclusive
    print(slice)
    #if the start index isn't defined, is taken from the beg inning of the tuple
    slice = tup[:6]
    print(slice)
    #if the end index isn't defined, is taken until the end of the tuple
    slice = tup[5:]
    print(slice)
    #if neither is defined, returns the full tuple
    slice = tup[:]
    print(slice)
    #The indexes can be defined with negative values
    slice = tup[-8:-4]
    print(slice)
    #create another tuple
    tup1 = tuple("HELLO WORLD")
    print(tup1)
    #step specify an increment between the elements to cut of the tuple
    #tuple[start:stop:step]
    slice1 = tup1[2:9:2]  #(step = in middle leave(n-1)==>2-1)
    print(slice1)
    #returns a tuple with a jump every 3 items
    slice1 = tup1[::4]
    print(slice1)
    #when step is negative the jump is made back
    slice1 = tup1[9:2:-4]
    print(slice1)