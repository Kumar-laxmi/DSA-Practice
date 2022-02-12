class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    #To tranverse a list
    def PrintList(self):
        ptr = self.head
        while ptr:
            print("{}".format(ptr.data),end="<->")
            ptr = ptr.next
    
    #To return the length of list
    def Length(self):
        ptr = self.head
        count = 1
        while ptr:
            ptr = ptr.next
            count = count + 1
        return count
    
    #To insert a node in list
    def InsertNode(self,newValue,position):
        if self.head==None:
            newNode = Node(newValue)
            self.head = newNode
            print("\nList is empty, making {} data node as head node".format(newValue))
        elif position<0 or position>self.Length():
            print("Sorry position out of bound! ==> Invalid position request")
        elif position==0:
            self.InsertElementBeginning(newValue)
        elif position==self.Length():
            self.InsertElementEnd(newValue)
        else:
            self.InsertElementAtPosition(newValue,position)
    
    #To insert to beginning of the list
    def InsertElementBeginning(self,newValue):
        newNode = Node(newValue)
        ptr = self.head
        newNode.next = ptr
        self.head = newNode
        print("{} inserted successfully to the beginning of the list".format(newValue))
    
    #To insert to end of list
    def InsertElementEnd(self,newValue):
        newNode = Node(newValue)
        ptr = self.head
        while ptr:
            ptr = ptr.next
        ptr.next = newNode
        newNode.prev = ptr
        print("{} inserted successfully to the end of the list".format(newValue))
    
    def InsertElementAtPosition(self,newValue,position):
        newNode = Node(newValue)
        ptr = self.head
        count = 0
        while ptr:
            if count==position-1:
                newNode.next = ptr.next
                ptr.next = newNode
                newNode.prev = ptr
                if newNode.next:
                    newNode.next.prev = newNode
            ptr = ptr.next
            count = count + 1
        print("{} inserted successfully to position no. {} of the list".format(newValue,position))

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
            self.DeleteNodeAtPosition(position)
    
    #To delete Node at the beginning of the list
    def DeleteNodeBeginning(self):
        temp = self.head
        self.head.next.prev = None
        self.head = temp.next
        print("\n{} deleted successfully at position: 0".format(temp.data))
        temp = None
    
    #To delete Node at the end of the list
    def DeleteNodeEnd(self):
        ptr = self.head
        while ptr.next is not None:
            prevNode = ptr
            ptr = ptr.next
        prevNode.next = None
        print("\n{} deleted successfully at position: {}".format(ptr.data,self.Length()-1))
        ptr = None
    
    def DeleteNodeAtPosition(self,position):
        temp = self.head.next
        prevNode = self.head
        for i in range(1,position-1):
            temp = temp.next
            prevNode = prevNode.next
        prevNode.next = temp.next
        temp.next.prev = prevNode
        print("\n{} deleted successfully at position: {}".format(temp.data,position))
        temp = None

dll = DoublyLinkedList()
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
        dll.InsertNode(newValue,position)
    elif choice==2:
        print("\n<<<  Choice 2 selected  >>>")
        position = int(input("Enter the position to be deleted: "))
        dll.DeleteNode(position)
    elif choice==3:
        print("\n<<<  Choice 3 selected  >>>")
        print("\nThe Doubly Linked-List is ==>")
        dll.PrintList()
    elif choice==4:
        print("\n <<<  Choice 4 selected , EXIT INITIATED...  >>>")
        break
    else:
        print("\nInvalid choice, Enter a correct choice!!!")
