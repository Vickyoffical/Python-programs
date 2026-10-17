#Create class to create Node.
class Node:

    def __init__(self,data,):
        self.data = data
        self.next = None

#Create a Linkedlist class to travel the linked list.
class Linkedlist:

    #initializing head address
    def __init__(self):
        self.head = None

    #creating newnode and storing data into next address.
    def create(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode

    #adding data at specific value.
    def add_at_specific(self,data):
        newnode = Node(data)

    #adding data at first address.
        def addfirst(self,data):
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    #displaying data.
    def display(self):
        i = 1
        dis = self.head
        print("\nData in linkedlist :")
        while dis is not None:
            print(i," value is :",dis.data)
            dis = dis.next
            i = i + 1

#Create an object of classes.
link = Linkedlist()

#Add numerical data to linked list.
# n = int(input("\nEnter the number of data :"))
# for i in range(n):
#     data = int(input("Enter Data: "))
#     link.create(data)
# link.display()

#Add string data to linked list.
n = int(input("\nEnter the number of data :"))
for i in range(n):
    data = input("Enter Name: ")
    link.create(data)
link.display()

#Add data at first address.
addData = input("\nEnter a value to add first :")
link.addfirst(addData)

#Add data at specific postion.
pos = int(input("Enter position to add new value :"))


link.display()
