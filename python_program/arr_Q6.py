#Q.6 Reversing array elements using reverse function
from array import *

arr = array('i',[10,20,30,40,50,60,70,80,90])

print("Array Elements :")
for i in range(len(arr)):
    print(arr[i])

reverse = arr.reverse()
print("Reverse Array Elements :")
for i in range(len(arr)):
    print(arr[i])