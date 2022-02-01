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

    #To delete Node
    def DeleteNode(self,key):
        ptr = self.head

        if self.head is None:
            print("\nSorry the list is empty!!!\n")
            return
        
        #First node is to deleted
        if self.head.data==key:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            print("\n{} deleted successfully".format(key))
            temp = None
            return
        
        while ptr:
            if ptr.data is key and ptr.next is not None:
                prevNode.next = nextNode
                nextNode.prev = prevNode
                print("{} deleted successfully".format(key))
                ptr = None
                return 
            else:
                prevNode.next = None
                ptr = None
                print("{} deleted successfully".format(key))
            prevNode = ptr
            ptr = ptr.next
            if ptr.next is not None:
                nextNode = ptr.next
            


dll = DoublyLinkedList()
print("Enter 1 to Insert")
print("Enter 2 to delete")
print("Enter 3 to transverse")
print("Enter 4 to Exit")

while True:
    choice = int(input("\nEnter a choice: "))
    if choice==1:
        print("<<<  Choice 1 selected  >>>")
        newValue = int(input("Enter the data: "))
        position = int(input("Enter the position: "))
        dll.InsertNode(newValue,position)
    elif choice==2:
        print("<<<  Choice 2 selected  >>>")
        key = int(input("Enter the key to be deleted: "))
        dll.DeleteNode(key)
    elif choice==3:
        print("<<<  Choice 3 selected  >>>")
        print("\nThe Doubly Linked-List is ==>")
        dll.PrintList()
    elif choice==4:
        print("<<<  Choice 4 selected , EXIT INITIATED...  >>>")
        break
    else:
        print("\nInvalid choice, Enter a correct choice!!!")
