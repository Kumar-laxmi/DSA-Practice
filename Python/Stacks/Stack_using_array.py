class StackUsingArray:
   def __init__(self):
       self.stack = []
       self.top = -1
  
   # To check if stack is empty
   def isEmpty(self):
       return self.top==-1
  
   # To push an element
   def push(self,newValue):
       self.stack.append(newValue)
       self.top = self.top + 1
       print("\n{} pushed into the Stack".format(newValue))
  
   # To pop an element
   def pop(self):
       if not self.isEmpty():
           print("\nThe element {} is popped from stack".format(self.stack.pop()))
           self.top = self.top - 1
       else:
           print("\nInvalid Deletion!!, REASON: Empty List")
  
   # To print the peek element of stack
   def peek(self):
       if not self.isEmpty():
           print("\nThe top element of stack is: {}".format(self.stack[self.top]))
       else:
           print("\nThe list is empty")
 
   def PrintStack(self):
       if not self.isEmpty():
           print("\nThe stack is: ")
           for i in range(self.top,-1,-1):
               print(self.stack[i])
       else:
           print("\nEmpty Stack")
 
st = StackUsingArray()
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
       st.push(newValue)
   elif choice==2:
       st.pop()
   elif choice==3:
       st.peek()
   elif choice==4:
       st.PrintStack()
   elif choice==5:
       st.isEmpty()
   elif choice==6:
       break
   else:
       print("\nInvalid Choice!!")
