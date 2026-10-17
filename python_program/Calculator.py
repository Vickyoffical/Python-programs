def calculator (a,b,ch):
    
    match(ch):
        case 1:
            return a + b
        
        case 2:
            return a - b
        
        case 3:
            return a * b
        
        case 4:
            return a / b
        
        case _:
            print("Invaild Choice!")


a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("\nWhat do you want to do ?")
ch = int(input("1. Addition\n2. Substraction\n3. Multification\n4. Division\n"))

result = calculator(a,b,ch)
print(result)
