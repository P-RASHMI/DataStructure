'''
@Author: Rashmi
@Date: 2021-09-24  21:46
@Last Modified by: Rashmi
@Last Modified time: 2021-09-24 21:54
@Title : Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
from datetime import date

if __name__ == '__main__':

     '''Description : to take two dates,does difference of two dates and returns number of days'''
    
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
numberofdays = last_date - first_date
print("number of days : ")
print(numberofdays.days)


 