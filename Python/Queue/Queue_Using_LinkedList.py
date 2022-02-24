class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return (self.front is None) and (self.rear is None)

    def Enqueue(self,newValue):
        if self.isEmpty():
            print("\nENQUEUE operation successful for value {}".format(newValue))
            newNode = Node(newValue)
            self.front = newNode
            self.rear = newNode
        else:
            newNode = Node(newValue)
            self.rear.next = newNode
            self.rear = newNode
            print("\nENQUEUE operation successful for value {}".format(newValue))
    
    def Dequeue(self):
        if self.isEmpty():
            print("Invalid Deletion!! REASON: Empty Queue")
        else:
            temp = self.front
            self.front = temp.next
            print("\nDEQUEUE operation successful for value {}".format(temp.data))
            temp = None
    
    def Front(self):
        if self.isEmpty():
            print("\nEmpty Queue")
        else:
            print("\nThe Front Element in the Queue is: {}".format(self.front.data))
    
    def Display(self):
        if self.isEmpty():
            print("\nEmpty Queue")
        else:
            print("\nThe Queue is: ")
            ptr = self.front
            print("\nfront->",end="")
            while ptr:
                print(ptr.data,end=" ")
                ptr = ptr.next
            print("<-rear")


qull = QueueUsingLinkedList()
print("Enter 1 to perform ENQUEUE operation")
print("Enter 2 to perform DEQUEUE operation")
print("Enter 3 to print FRONT element")
print("Enter 4 to print the whole Queue")
print("Enter 5 to check if Queue is empty")
print("Enter 6 to exit")

while True:
    choice = int(input("\nEnter your choice: "))
    if choice==1:
        newValue = int(input("Enter the value to enter: "))
        qull.Enqueue(newValue)
    elif choice==2:
        qull.Dequeue()
    elif choice==3:
        qull.Front()
    elif choice==4:
        qull.Display()
    elif choice==5:
        print("Status of isEmpty of Stack: {}".format(qull.isEmpty()))
    elif choice==6:
        break
    else:
        print("\nInvalid Choice!!")
