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
        self.tail = None

    #creating newnode and storing data into next address.
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

    #adding data at specific value.
    def add_at_specific(self,data,pos):
        newnode = Node(data)
        if pos is None:
            print("Out of range.")
            return
        if pos == 1:
            self.addfirst(data)
            return
        current = self.head
        count = 0
        if current is not None and count == pos - 1:
            current = current.next
            count = count + 1            

    #adding data at first address.
    def addfirst(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    #delete last value.
    def delete_at_last(self):
        if self.head is None:
            print("List is empty. Nothing to Delete.")
            return
        
        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            temp.data = 0
            temp.next = None
            temp = 0
            print("Single Node is deleted.")
            return
           
        current = self.head
        while current.next.next is not None:
            current = current.next
        self.tail.data = None
        current.next = None
        self.tail = current
        print("Last Node deleted.")
            
    #delete first value.
    def delete_at_first(self):
        if self.head is None:
            print("List is empty. Nothing to Delete.")
            return
        
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        temp.data = 0
        temp.next = None
        temp = None

    #displaying data.
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        else:        
            i = 1
            dis = self.head
            print("\nData in linkedlist :")
            while dis is not None:
                print(i," value is :",dis.data)
                dis = dis.next
                i = i + 1

#Create an object of classes.
link = Linkedlist()

n = int(input("\nEnter the number of data :"))
for i in range(n):
    data = input("Enter Data: ")
    link.create(data)

link.display()