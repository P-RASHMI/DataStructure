'''
@Author: Rashmi
@Date: 2021-09-24 21:30
@Last Modified by: Rashmi
@Last Modified time: 2021-09-24 21:46
@Title : Write a Python program to print the calendar of a given month and year.using calender module
'''
import calendar

if __name__ == '__main__':
    '''Description : to print calender for given year and month'''
    year = int(input("enter the year : "))
    month = int(input("enter the month : "))
    print(calendar.month(year, month))              # prints month calender with year and month name