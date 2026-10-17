arr = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

prime = []

for i in range(1, len(arr)):
    prime_num = True
    if arr[i] % i == 0:
        prime_num = False
        break
    if prime_num:
        prime.append(i)
        
for i in range(len(prime)):
    print("Prime is",prime[i])
    
# arr = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# prime = []

# for num in arr:

#     prime_num = True

#     for i in range(2, num):
#         if num % i == 0:
#             prime_num = False
#             break

#     if prime_num:
#         prime.append(num)

# for i in range(len(prime)):
#     print("Prime is", prime[i])