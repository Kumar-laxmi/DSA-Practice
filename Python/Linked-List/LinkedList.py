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
            ptr = ptr.next
            count = count + 1
        return count

    # To insert new data in beginning
    def InsertElementBeginning(self,newData):
        newNode = Node(newData)
        ptr = self.head
        newNode.next = ptr
        self.head = newNode
        print("{} entered successfully at position 0".format(newData))

    # To insert new data in end
    def InsertElementEnd(self,newData):
        newNode = Node(newData)
        ptr = self.head
        while (ptr):
            ptr = ptr.next
        ptr.next = newNode
        print("{} entered successfully at position last".format(newData))

    # To insert new node
    def InsertElement(self,newData,position):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            print("{} inserted as first element in linked list".format(newData))
        else:
            count = 0
            ptr = self.head
            while (ptr):
                if position<0 or position>self.getLength():
                    print("Position Out of Bound")
                    break
                if position==0:
                    self.InsertElementBeginning(newData)
                    break
                elif position==self.getLength()-1:
                    self.InsertElementEnd(newData)
                elif count==position-1:
                    temp = ptr
                    newNode.next = temp.next
                    ptr.next = newNode
                    print("{} entered successfully at position {}".format(newData,position))
                    break
                ptr = ptr.next
                count = count + 1
    
    # To delete a node
    def DeleteNode(self, key):
        temp = self.head
 
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        if(temp == None):
            return
 
        prev.next = temp.next
        print("\n{} deleted successfully".format(key))
        temp = None

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
        key = int(input("\nEnter the key value to delete: "))
        ll.DeleteNode(key)
    elif choice==3:
        print("\nThe Linked List is: ")
        ll.PrintList()
    elif choice==4:
        break
    else:
        print("Invalid choice")
