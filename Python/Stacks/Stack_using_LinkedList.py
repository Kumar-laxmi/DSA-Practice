class Node:
   def __init__(self,data):
       self.data = data
       self.next = None
 
class StackUsingLinkedList:
   def __init__(self):
       self.top = None
  
   # To check if stack is empty
   def isEmpty(self):
       return self.top is None
 
   # To transverse and print the data
   def PrintStack(self):
       if not self.isEmpty():
           print("\nThe stack is: ")
           ptr = self.top
           while (ptr):
               print("{}".format(ptr.data))
               ptr = ptr.next
       else:
           print("Empty Stack")
 
   # To find length of Linked List
   def getLength(self):
       count = 1
       ptr = self.top
       while (ptr):
           count = count + 1
           ptr = ptr.next
       return count
  
   # To push the element
   def push(self,newData):
       newNode = Node(newData)
       ptr = self.top
       newNode.next = ptr
       self.top = newNode
       print("\n{} pushed successfully to the stack".format(newData))
  
   # To pop the element
   def pop(self):
       if not self.isEmpty():
           temp = self.top
           self.top = temp.next
           print("\n{} popped successfully from the stack".format(temp.data))
           temp = None
       else:
           print("Invalid pop operation! REASON: Empty Stack")
  
   # To print the peek of stack
   def peek(self):
       if not self.isEmpty():
           print("\nThe peek of stack is {}".format(self.top))
       else:
           print("The Stack is empty")
 
stll = StackUsingLinkedList()
print("Enter 1 to Push an element")
print("Enter 2 to pop an element")
print("Enter 3 to print the peek of Stack")
print("Enter 4 to print the whole Stack")
print("Enter 5 to check if Stack is empty")
print("Enter 6 to exit")
 
while True:
   choice = int(input("\nEnter your choice: "))
   if choice==1:
       newValue = int(input("Enter the value to push: "))
       stll.push(newValue)
   elif choice==2:
       stll.pop()
   elif choice==3:
       stll.peek()
   elif choice==4:
       stll.PrintStack()
   elif choice==5:
       stll.isEmpty()
   elif choice==6:
       break
   else:
       print("\nInvalid Choice!!")
