line = input("Enter string. :")
# line = 'On & On'
n = len(line)

for i in range(0,n+1):
    for j in range(i):
        print("",line[j], end = '')
    print()