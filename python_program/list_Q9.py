numbers = [1,2,3,4,5,6,7,8,9,10]
# count = len(numbers)

print("Original List : ",numbers)

index = int(input("Enter an index number to change value : "))

for i in range(len(numbers)):
    if i == index:
        numbers[i] = int(input("Enter new elements : "))

print("New list :", numbers)
remove = int(input("Enter a value to remove from list : "))
numbers.remove(remove)

print("Updated List :",numbers)