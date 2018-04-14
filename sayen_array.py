#Joie Sayen
#JoyOfYahweh
#Array - Exercise No. 1
#Data Structures and Algorithm Analysis

from array import*
my_array = array('i',[1,2,3,4,5,6,7])

for i in my_array:
    print (i)

print ("\n **List first three items individually** \n")
print (my_array[0])
print (my_array[2])
print (my_array[4])

print("Original array: \n "+str(my_array))

print("\n Append 11 at the end of the array:")

my_array.append(11)
my_array.append(22)
my_array.append(33)
my_array.append(44)
print("\nNew array: \n"+str(my_array))