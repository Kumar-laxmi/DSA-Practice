class QueueUsingArray:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0
    
    # To check if queue is empty
    def isEmpty(self):
        return self.front==self.rear
    
    # To perform ENQUEUE operation on queue
    def Enqueue(self,newValue):
        self.queue.append(newValue)
        print("\n{} enqueued to queue successfully at {}".format(newValue,self.rear))
        self.rear = self.rear + 1

    # To perform DEQUEUE operation on queue
    def Dequeue(self):
        if not self.isEmpty():
            print("\n{} dequeued from queue successfully".format(self.queue.pop(0)))
            self.rear = self.rear - 1
        else:
            print("\nInvalid Deletion!! REASON: Empty queue")
    
    # To perform FRONT operation on queue
    def Front(self):
        if not self.isEmpty():
            print("\nThe Front Element is: {}".format(self.queue[self.front]))
        else:
            print("\nEmpty Queue")
    
    # To perform DISPLAY operation on queue
    def Display(self):
        if not self.isEmpty():
            print("front->",end="")
            for i in range(self.front,self.rear):
                print(self.queue[i],end=" ")
            print("<-rear")

qua = QueueUsingArray()
print("Enter 1 to perform ENQUEUE operation")
print("Enter 2 to perform DEQUEUE operation")
print("Enter 3 to print FRONT element")
print("Enter 4 to print the whole Queue")
print("Enter 5 to check if Queue is empty")
print("Enter 6 to exit")

while True:
    choice = int(input("\nEnter your choice: "))
    if choice==1:
        newValue = int(input("Enter the value to push: "))
        qua.Enqueue(newValue)
    elif choice==2:
        qua.Dequeue()
    elif choice==3:
        qua.Front()
    elif choice==4:
        qua.Display()
    elif choice==5:
        print("Status of isEmpty of Stack: {}".format(qua.isEmpty()))
    elif choice==6:
        break
    else:
        print("\nInvalid Choice!!")
