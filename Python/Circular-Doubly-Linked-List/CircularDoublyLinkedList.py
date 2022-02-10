class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # To print the list
    def PrintList(self):
        if self.head is None:
            print("The list is empty")
        else:
            ptr = self.head
            print("--IN ASCENDING ORDER--")
            while True:
                print(ptr.data,end="<->")
                ptr = ptr.next
                if ptr==self.head:
                    break
            temp = self.tail
            print("\n--IN DESCENDING ORDER--")
            while True:
                print(temp.data,end="<->")
                temp = temp.prev
                if temp==self.tail:
                    break

    # To return the length of the list
    def Length(self):
        if self.head==None:
            return 0
        else:
            count = 1
            ptr = self.head
            while True:
                ptr = ptr.next
                if ptr==self.head:
                    break
                count = count + 1
            return count
    
    #To insert a node in list
    def InsertNode(self,newValue,position):
        if self.head==None:
            self.InsertElementAtEmpty(newValue)
        elif position<0 or position>self.Length():
            print("Sorry position out of bound! ==> Invalid position request")
        elif position==0:
            self.InsertElementBeginning(newValue)
        elif position==self.Length():
            self.InsertElementEnd(newValue)
        else:
            self.InsertAtPosition(newValue,position)
    
    # To insert to empty list
    def InsertElementAtEmpty(self,newValue):
        newNode = Node(newValue)
        self.head = newNode
        self.tail = newNode
        self.tail.next = self.head
        self.head.prev = self.tail
        print("\nList is empty, making {} data node as head node".format(newValue))

    #To insert to beginning of the list
    def InsertElementBeginning(self,newValue):
        newNode = Node(newValue)
        self.tail.next = newNode
        newNode.prev = self.tail
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        print("{} inserted successfully to the beginning of the list".format(newValue))
    
    #To insert to end of list
    def InsertElementEnd(self,newValue):
        newNode = Node(newValue)
        self.tail.next = newNode
        newNode.prev = self.tail
        newNode.next = self.head
        self.head.prev = newNode
        self.tail = newNode
        print("{} inserted successfully to the end of the list".format(newValue))
    
    # To insert at a particular position
    def InsertAtPosition(self,newValue,position):
        newNode = Node(newValue)
        ptr = self.head
        nextptr = self.head.next
        count = 0
        while ptr is not self.tail:
            if count==position-1:
                ptr.next = newNode
                newNode.prev = ptr
                newNode.next = nextptr
                nextptr.prev = newNode
                print("{} inserted successfully to position no. {} of the list".format(newValue,position))
                break
            ptr = ptr.next
            nextptr = nextptr.next
            count = count + 1

    #To delete Node
    def DeleteNode(self,position):
        if self.head is None:
            print("Invalid Deletion!, REASON: Empty List")
        elif position<0 or position>=self.Length():
            print("Invalid Deletion!, REASON: position requested out of bounds")
        elif position==0:
            self.DeleteNodeBeginning()
        elif position==self.Length()-1:
            self.DeleteNodeEnd()
        else:
            self.DeleteAtPosition(position)
    
    #To delete Node at the beginning of the list
    def DeleteNodeBeginning(self):
        temp = self.head
        self.head = self.head.next
        self.tail.next = self.head
        self.head.prev = self.tail
        print("\n{} deleted successfully at position: 0".format(temp.data))
        temp = None
    
    #To delete Node at the end of the list
    def DeleteNodeEnd(self):
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        print("\n{} deleted successfully at position: {}".format(temp.data,self.Length()-1))
        temp = None
    
    # To delete a node at particular position
    def DeleteAtPosition(self,position):
        temp = self.head.next
        prevNode = self.head
        for i in range(1,position-1):
            temp = temp.next
            prevNode = prevNode.next
        nextNode = temp.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        print("\n{} deleted successfully at position: {}".format(temp.data,position))
        temp = None


dcll = DoublyCircularLinkedList()
print("Enter 1 to Insert")
print("Enter 2 to delete")
print("Enter 3 to transverse")
print("Enter 4 to Exit")

while True:
    choice = int(input("\nEnter a choice: "))
    if choice==1:
        print("\n<<<  Choice 1 selected  >>>")
        newValue = int(input("Enter the data: "))
        position = int(input("Enter the position: "))
        dcll.InsertNode(newValue,position)
    elif choice==2:
        print("\n<<<  Choice 2 selected  >>>")
        position = int(input("Enter the position to be deleted: "))
        dcll.DeleteNode(position)
    elif choice==3:
        print("\n<<<  Choice 3 selected  >>>")
        print("\nThe Doubly Linked-List is ==>")
        dcll.PrintList()
    elif choice==4:
        print("\n <<<  Choice 4 selected , EXIT INITIATED...  >>>")
        break
    else:
        print("\nInvalid choice, Enter a correct choice!!!")
