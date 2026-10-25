#Create class to create Node.
class Node:

    def __init__(self,data,):
        self.data = data
        self.next = None

#Create a Linkedlist class to travel the linked list.
class Linkedlist:

    #initializing head and tail address
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
        
        if pos == 1:
            self.addfirst(data)
            return
        current = self.head
        count = 1
        if current is not None and count < pos - 1:
            current = current.next
            count = count + 1            
            
        if current is None:
            print("Out of range.")
            return
        
        newnode.next = current.next
        current.next = newnode
        
        if newnode.next is None:
            self.tail = newnode

    #adding data at first address.
    def addfirst(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    #adding data at last address.
    def addlast(self,data):
        print("For adding value at last method is pending to implement.")

    def delete_at_specific(self):
        print("For deleting value at specific position method is pending to implement.")

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

while True:
    print("\nSelect one option.")
    print("\n1. Add value at first position\n2. Add value at last position\n3. Add value at specific position\n4. Delete first Node\n5. Delete last Node\n6. Delete specific Node\n7. Add new into linked list\n8. Display linked list\n9. Exit")
    ch = int(input("\nEnter choice :"))

    match ch:
        case 1:
            data = input("\nEnter new value to add first :")
            link.addfirst(data)
            link.display()
        case 2:
            data = input("\nEnter new value to add last :")
            link.addlast(data)
            link.display()
        case 3:
            data = input("\nEnter new value :")
            pos = int(input("Enter position to add value :"))
            link.add_at_specific(data,pos)
            link.display()
        case 4:
            print("\nDeleting first value...")
            link.delete_at_first()
            link.display()
        case 5:
            print("\nDeleting last value...")
            link.delete_at_last()
            link.display()
        case 6:
            pos = int(input("\nEnter position to delete value :"))
            data = input("Verifing postion.")
            link.delete_at_specific()
            link.display()
        case 7:
            n = int(input("\nEnter the number of data :"))
            for i in range(n):
                data = input("Enter Data: ")
                link.create(data)
            link.display()
        case 8:
            link.display()
        case 9:
            break
        case _:
            print("Invaild choice.")