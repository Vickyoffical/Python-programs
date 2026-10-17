# from array import *

# #Print array elements
# def array_elements(num,arr):
#     print("Array Elements :")
#     for i in range(num):
#         print(arr[i])
        

# #Q.1 Print array
# arr = array('i',[10,20,30,40,50,60,70,80,90])
# num = len(arr)
# array_elements(num,arr)

# #Q.2 Add new value using append value
# arr.append(int(input("Enter new value to add : ")))



# Declare an array
A = []

# Read the number of elements
n = int(input("Enter number of elements: "))

# Read n elements into the array
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    A.append(element)

# Read the new element
x = int(input("Enter new element: "))

# Increase the number of elements
n = n + 1

# Add the new element to the array
A.append(x)

# Print the updated array
print("Updated Array:", A)
