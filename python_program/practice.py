class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    
    def show(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

details = []
NoOfStudent = int(input("Enter Number of student : "))

for i in range(NoOfStudent):
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    s1 = Student(name,age)
    details.append(s1)
    
for i in details:
    i.show()


# Number = [10,20,30,40,50]

# N = len(Number)
# i = N
# # print(i)

# for i in range(N):
#     print(i)
#     print(Number[i])
#     i = i - 1