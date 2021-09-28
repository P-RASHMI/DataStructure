'''
@Author: Rashmi
@Date: 2021-09-26 4:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-26 4:20
@Title : Write a Python program to get the name of the host on which the routine is running.
'''
import platform
import socket
if __name__ == '__main__': 
    '''Description : to get the name of the host on which the routine is running using 
    socket.gethostname(),platform.uname()[1]''' 
    host_name = socket.gethostname()
    print("Host name:", host_name)
    host_name = platform.uname()[1]
    print("Host name:", host_name )
