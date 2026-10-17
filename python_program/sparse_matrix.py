matrix = [[8,4,0,0,0],[0,0,6,0,0],[9,0,0,18,0],[0,1,0,0,0]]

arr = []

print("2D Matrix : ", matrix)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != 0:
            arr.append(matrix[i][j])
            
print("Single list : ",arr)