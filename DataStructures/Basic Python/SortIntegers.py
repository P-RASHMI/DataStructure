'''
@Author: Rashmi
@Date: 2021-09-26 12:16
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 1:00
@Title :Write a Python program to sort three integers without using conditional statements and
loops.
'''
if __name__ == '__main__': 
    '''Description : to take all the three integers and find max, min, and by subtracting max,min from
    total to get middle number and print numbers ,
    using sort(),sorted()'''  
    first_num = int(input("Input first number: "))
    second_num = int(input("Input second number: "))
    third_num = int(input("Input third number: "))
    #finding max min numbers using min() max()
    minimum_number = min( first_num,second_num,third_num)
    maximum_number = max( first_num,second_num,third_num)
    middle_number = (first_num + second_num + third_num) - minimum_number - maximum_number
    print("Numbers in sorted order: ",minimum_number,middle_number,maximum_number)
    #storing values in list
    list_numbers =[first_num,second_num,third_num] 
    print("using sorted(): the sorted list is:",sorted(list_numbers)) #using sorted()
    list_numbers.sort()     # using sort to sort values
    print("using sort(): the sorted list is:",list_numbers) #printing sorted list but should use listname
