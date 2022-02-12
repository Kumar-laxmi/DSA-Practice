class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # To transverse and print the data
    def PrintList(self):
        ptr = self.head
        while (ptr):
            print("-> {}".format(ptr.data),end=" ")
            ptr = ptr.next
    
    # To find length of Linked List
    def getLength(self):
        count = 1
        ptr = self.head
        while (ptr):
            count = count + 1
            ptr = ptr.next
        return count

    # To insert new data in beginning
    def InsertElementBeginning(self,newData):
        newNode = Node(newData)
        ptr = self.head
        newNode.next = ptr
        self.head = newNode
        print("\n{} entered successfully at position 0".format(newData))

    # To insert new data in end
    def InsertElementEnd(self,newData):
        newNode = Node(newData)
        ptr = self.head
        while (ptr):
            ptr = ptr.next
        ptr.next = newNode
        print("\n{} entered successfully at position last".format(newData))
    
    def InsertElementAtPosition(self,newData,position):
        ptr = self.head
        newNode = Node(newData)
        count = 1
        while ptr:
            if count==position:
                newNode.next = ptr.next
                ptr.next = newNode
                print("\n{} entered successfully at position {}".format(newData,position))
                break
            ptr = ptr.next
            count = count + 1

    # To insert new node
    def InsertElement(self,newData,position):
        if self.head is None:
            newNode = Node(newData)
            self.head = newNode
            print("\n{} inserted as first element in linked list".format(newData))
        else:
            if position<0 or position>self.getLength():
                print("\nPosition Out of Bound")
            elif position==0:
                self.InsertElementBeginning(newData)
            elif position==self.getLength():
                self.InsertElementEnd(newData)
            else:
                self.InsertElementAtPosition(newData,position)
    
    # To delete a node
    def DeleteNode(self, position):
        if self.head==None:
            print("\nSorry the list is empty")
        elif position<0 or position>=self.getLength():
            print("\nInvalid Deletion! REASON:Invalid position entered")
        elif position==0:
            self.DeleteNodeBeginning()
        elif position==self.getLength()-1:
            self.DeleteNodeEnd()
        else:
            self.DeleteNodeAtPosition(position)
    
    def DeleteNodeBeginning(self):
        temp = self.head
        self.head = temp.next
        print("\n{} deleted in Linked List, Position: BEGINNING".format(temp.data))
        temp = None
    
    def DeleteNodeEnd(self):
        prevNode = self.head
        temp = self.head.next
        while temp:
            prevNode = prevNode.next
            temp = temp.next
        prevNode.next = None
        print("\n{} deleted in Linked List, Position: END".format(temp.data))
        temp = None
    
    def DeleteNodeAtPosition(self,position):
        prevNode = self.head
        temp = self.head.next
        count = 1
        while temp:
            if count==position:
                prevNode.next = temp.next
                print("\n{} deleted in Linked List, Position: {}".format(temp.data,position))
                temp = None
                break
            prevNode = prevNode.next
            temp = temp.next
            count = count + 1

        
ll = LinkedList()
choice = 1
print("Enter 1 to Insert")
print("Enter 2 to delete")
print("Enter 3 to tranverse")
print("Enter 4 to exit\n")
while choice!=4:
    choice = int(input('Enter a choice: '))
    if choice==1:
        newData = int(input("\nEnter the new data: "))
        position = int(input("Enter the position: "))
        ll.InsertElement(newData,position)
    elif choice==2:
        key = int(input("\nEnter the position value to delete: "))
        ll.DeleteNode(key)
    elif choice==3:
        print("\nThe Linked List is: ")
        ll.PrintList()
    elif choice==4:
        break
    else:
        print("\nInvalid choice")
