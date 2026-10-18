#Create Node
class Node:

    def __init__(self,data,):
        self.data = data
        self.next = None

#Create a Linkedlist class to travel the linked list and display the data
class Linkedlist:

    #initializing head address
    def __init__(self):
        self.head = None
        self.tail = None

    #creating newnode and storing data into next address
    def create(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
            self.tail = newnode



    #insert methods are pending.


    #sum of data in linked list.
    def sumofdata(self):
        current = self.head
        sum = 0

        while current is not None:
            # value = current.data
            sum = sum + current.data
            current = current.next
        print("Sum of Data in Node is :",sum)

    #To find even numbers from Node
    def even_numbers(self):
        current = self.head
        while current is not None:
            if current.data % 2 == 0:
                print("Even Number :",current.data)                
            current = current.next

    #Delete last data
    def delete_last(self):
        if self.head is None:
            print("\nList is empty. Nothing to delete.")
            return

        #Only one node in linkedlist
        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            temp.data = 0
            temp.next = None
            temp = 0
            print("\nSingle Node is deleted successfully.")
            return

        #travel to second last node and delete last node
        current = self.head
        while current.next.next is not None:
            current = current.next
        self.tail.data = None
        current.next = None
        self.tail = current
        print("\nLast Node is deleted.")

    #display first data
    def delete_first(self):
        if self.head is None:
            print("\nList is empty. Nothing to delete.")
            return

        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        temp.data = 0
        temp.next = None
        temp = 0
        print("\nFirst Node is deleted.")
        

    #displaying data
    def display(self):
        if self.head is None:
            print("\nList is empty.")
            return
        
        dis = self.head
        print("\nData in linkedlist :")
        while dis is not None:
            print(dis.data)
            dis = dis.next


    #Sorting list data in ascending

#Create an object of classes
link = Linkedlist()

n = int(input("\nEnter the number of data :"))

data = []
for i in range(n):
    name = input("Enter Name: ")
    data.append(name)

    # link.create(data)
    # print(link.head.data, link.tail.data)

data.sort()
for i in data:
    link.create(i)

link.display()
# link.delete_last()
# link.display()
# link.delete_first()
# link.display()
# link.sumofdata()
# link.even_numbers()
