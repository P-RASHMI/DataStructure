'''
@Author: Rashmi
@Date: 2021-09-26 4:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 4:20
@Title : Write a Python program to access and print a URL's content to the console
'''

from http.client import HTTPConnection
'''Description :to access and print a URL's content to the console ''' 
conn = HTTPConnection("www.google.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)
