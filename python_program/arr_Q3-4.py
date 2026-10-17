#Q.3 Insert new value using insert funtion
from array import *

# # Insert value at specific position in array
# def insert_value_array(num,arr):
#     insert_position = int(input("Enter index number to navigate the value first : "))
#     for i in range(len(arr)):
#         if i == insert_position:
#             arr[i] = int(input("Enter New value for that position : "))
#     print("Updated Array Elements :")
#     for i in range(len(arr)):
#             print(arr[i])



arr = array('i',[10,20,30,40,50,60,70,80,90])
num = len(arr)

print("Array Elements :")
for i in range(num):
        print(arr[i])

#Using user defined function
# insert_value_array(num,arr)


arr.insert(5,700)
print("Array Elements :")
for i in range(num):
        print(arr[i])
        
#Q.4 Print deleted value from arrray
# deleted_value = arr.pop(5)
# print("Deleted value from array is :",deleted_value)
# print("Updated Array Elements :")
# for i in range(len(arr)):
#         print(arr[i])