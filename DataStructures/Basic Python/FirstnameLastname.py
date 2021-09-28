'''
@Author: Rashmi
@Date: 2021-09-24 16:24
@Last Modified by: Rashmi
@Last Modified time: 2021-09-24 16:30
@Title : Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.

'''

if __name__ == '__main__':
    '''Description : to get string and reverse string '''
    #using slicing     
    given_string=input("Enter First and Lastname\n")                        # initial string
    string_length=len(given_string)                                      # calculate length of the list
    reversed_string=given_string[string_length::-1]                   # slicing 
    # syntax is stringname[stringlength::-1]
    # without stringlength also --> stringname[::-1]
    print("using slicing")
    print (reversed_string )                                     # print the reversed string

    #using join 
    reversed=''.join(reversed(given_string)) # .join() method merges all of the characters resulting 
    print("using .join()")                    #from the reversed iteration into a new string
    print(reversed) #print the reversed string

    #using loop
    reversedString=" "
    while string_length > 0: 
        reversedString += given_string[ string_length - 1 ] # save the value of str[index-1] in reverse String
        string_length = string_length - 1                # decrement index
    print("using loop")     
    print(reversedString)                       # reversed string

