array = [26,30,35,5,6,7,9,20,40,45,11,18,15,49,60]
num = len(array)
count = 0

# print("The total even numbers are :")
print(array)

# for i in range(num):
#     print(array[i])
#     if array[i] % 2 == 0:
#         count = count + 1
#         # print("In Array index value at", i, "is =" , count, "of array element is =", array[i])
        
# print(count)

number = int(input("Enter a number to search in array :"))
temp = None

for i in range(num):
    if array[i] == number:
        temp = array[i]
        n = i
        
if temp is not None:
    print(temp,"found at",n)
else:
    print("Not Found.")