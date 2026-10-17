def fact_number(element):
    print("Funtion Element :",element)
    fact = 1
    for i in range(1,element+1):
        fact = i * fact
        # print("Factor Value :",fact)
    return fact
    
numbers = [5,7,9,6,8]
factor_num = []

for i in range(len(numbers)):
    temp = numbers[i]
    # print("\n Tempory Number :",temp)
    fact = fact_number(temp)
    factor_num.append(fact)

print("\nOutput :")
for i in range(len(numbers)):
    print("Factor of",numbers[i],"is :",factor_num[i])