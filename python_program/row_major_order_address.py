row = int(input("Enter no. of row in array : "))
col = int(input("Enter no. of column in array : "))

i= int(input("Enter index no. of row : "))
j = int(input("Enter index no. of column : "))

base_add = int(input("Enter base address : "))
byt = int(input("Enter bytes for each element occupied : "))

#Find the memory address of element at p[i][j], using row major order address.
#Formula
memory_add = base_add + (i * col + j) * byt

print("Memory address at row :",i,"and column :",j,"is :",memory_add)