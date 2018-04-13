#Joie Sayen
#JoyOfYahweh
#Function - Exercise No. 4
#Data Structures and Algorithm Analysis



def string_reverse():
    str1 = input("\n Enter a string: ")
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    print rstr1
   
string_reverse()
    