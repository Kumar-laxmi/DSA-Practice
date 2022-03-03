class CircularQueueUsingArray():
 
    # constructor
    def __init__(self, size): # initializing the class
        self.size = size
         
        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def isFull(self):
        return ((self.rear + 1) % self.size == self.front)

    def isEmpty(self):
        return (self.front == -1)
 
    def enqueue(self, data):
        # condition if queue is full
        if ((self.rear + 1) % self.size == self.front):
            print(" Queue is Full\n")
             
        # condition for empty queue
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            print("The element = {} enqueued successfully at position = {}".format(data,self.rear))
        else:  
            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print("The element = {} enqueued successfully at position = {}".format(data,self.rear))
             
    def dequeue(self):
        if (self.front == -1): # condition for empty queue
            print ("Queue is Empty\n")
             
        # condition for only one element
        elif (self.front == self.rear):
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            print("The element = {} deleted successfully".format(temp))
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print("The element = {} deleted successfully".format(temp))

    def Front(self):
        if self.isEmpty():
            print("\n Empty Queue ")
        else:
            print("\n The Front Element of Circular Queue is: {}".format(self.queue[self.front]))

    def Rear(self):
        if self.isEmpty():
            print("\n Empty Queue ")
        else:
            print("\n The Front Element of Circular Queue is: {}".format(self.queue[self.rear]))

    def display(self):
     
        # condition for empty queue
        if(self.front == -1):
            print ("Queue is Empty")
 
        elif (self.rear >= self.front):
            print("Elements in the circular queue are:",
                                              end = " ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print ()
 
        else:
            print ("Elements in Circular Queue are:",end = " ")
            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
            print ()
 
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")

size = int(input('Enter the size of Circular Queue: '))
print("THE SIZE OF CIRCULAR QUEUE IS: {}".format(size))
cq = CircularQueueUsingArray(size)

print("Enter 1 to perform ENQUEUE operation")
print("Enter 2 to perform DEQUEUE operation")
print("Enter 3 to print the whole Queue")
print("Enter 4 to check if Queue is empty")
print("Enter 5 to check if Queue is full")
print("Enter 6 to print Front Element of Circular Queue")
print("Enter 7 to print Rear Element of Circular Queue")
print("Enter 8 to exit")

while True:
    choice = int(input("\nEnter your choice: "))
    print("THE CHOICE SELECTED: {}".format(choice))
    if choice==1:
        newValue = int(input("Enter the value to push: "))
        cq.enqueue(newValue)
    elif choice==2:
        cq.dequeue()
    elif choice==3:
        cq.display()
    elif choice==4:
        print("Status of isEmpty of Stack: {}".format(cq.isEmpty()))
    elif choice==5:
        print("Status of isEmpty of Stack: {}".format(cq.isFull()))
    elif choice==6:
        cq.Front()
    elif choice==7:
        cq.Rear()
    elif choice==8:
        break
    else:
        print("\nInvalid Choice!!")
