class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # To print the list
    def PrintList(self):
        if self.head is None:
            print("The list is empty")
        else:
            ptr = self.head
            while True:
                print(ptr.data,end=" ")
                ptr = ptr.next
                if ptr==self.head:
                    print("\n")
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
            self.InsertElementInEmpty(newValue)
        elif position<0 or position>self.Length():
            print("Sorry position out of bound! ==> Invalid position request")
        elif position==0:
            self.InsertElementBeginning(newValue)
        elif position==self.Length():
            self.InsertElementEnd(newValue)
        else:
            self.InsertElementAtPosition(newValue,position)

    # To insert to empty list
    def InsertElementInEmpty(self,newValue):
        newNode = Node(newValue)
        self.head = newNode
        self.tail = newNode
        self.tail.next = self.head
        print("\n{} added as first node! REASON: List is empty".format(newValue))

    #To insert to beginning of the list
    def InsertElementBeginning(self,newValue):
        newNode = Node(newValue)
        self.tail.next = newNode
        newNode.next = self.head
        self.head = newNode
        print("{} inserted successfully to the beginning of the list".format(newValue))
    
    #To insert to the end of the list
    def InsertElementEnd(self,newValue):
        newNode = Node(newValue)
        ptr = self.head
        while ptr.next is not self.head:
            ptr = ptr.next
        ptr.next = newNode
        self.tail = newNode
        self.tail.next = self.head
        print("{} inserted successfully to the end of the list".format(newValue))
    
    #To insert to the particular position of Circular Linked List
    def InsertElementAtPosition(self,newValue,position):
        newNode = Node(newValue)
        ptr = self.head
        count = 0
        while ptr is not self.tail:
            if count==position-1:
                temp = ptr
                newNode.next = temp.next
                ptr.next = newNode
                print("{} inserted successfully to position no. {} of the list".format(newValue,position))
            ptr = ptr.next
            count = count + 1
    
    # To delete node in Circular Linked List
    def DeleteNode(self,position):
        if position<0 or position>self.Length():
            print("Sorry position out of bound! ==> Invalid deletion")
        elif position==0:
            self.DeleteElementBeginning()
        elif position==self.Length()-1:
            self.DeleteElementEnd()
        else:
            self.DeleteElementAtPosition(position)
    
    # To delete node in the beginning of the list
    def DeleteElementBeginning(self):
        temp = self.head
        self.head = temp.next
        self.tail.next = self.head
        print("\n{} deleted successfully at position: 0".format(temp.data))
        temp = None
    
    # To delete node at the end of list
    def DeleteElementEnd(self):
        ptr = self.head
        temp = self.head.next
        while temp is not self.tail:
            ptr = ptr.next
            temp = temp.next
        ptr.next = self.head
        self.tail = ptr
        self.tail.next = self.head
        print("\n{} deleted successfully at position: {} <-END".format(temp.data,self.Length()-1))
        temp = None
    
    # To delete node at a given position
    def DeleteElementAtPosition(self,position):
        count = 1
        ptr = self.head
        temp = self.head.next
        while ptr is not self.tail:
            if count==position:
                ptr.next = temp.next
                print("\n{} deleted successfully at position: {}".format(temp.data,position))
                temp = None
                break
            ptr = ptr.next
            temp = temp.next
            count = count + 1
        
cll = CircularLinkedList()
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
        cll.InsertNode(newValue,position)
    elif choice==2:
        print("\n<<<  Choice 2 selected  >>>")
        position = int(input("Enter the position to be deleted: "))
        cll.DeleteNode(position)
    elif choice==3:
        print("\n<<<  Choice 3 selected  >>>")
        print("\nThe Doubly Linked-List is ==>")
        cll.PrintList()
    elif choice==4:
        print("\n <<<  Choice 4 selected , EXIT INITIATED...  >>>")
        break
    else:
        print("\n\nInvalid choice, Enter a correct choice!!!") 
