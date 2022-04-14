class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def Print(root):
    print("Inorder Transversal of Binary Search Tree: ")
    Print_Inorder(root)
    print("\nPre-order Transversal of Binary Search Tree: ")
    Print_Preorder(root)
    print("\nPost-order Transversal of Binary Search Tree: ")
    Print_Postorder(root)

def Print_Inorder(root):
    if root is not None:
        # Transverse Left
        Print_Inorder(root.left)

        # Transverse Root
        print("{} -> ".format(root.data),end=' ')

        # Transverse Right
        Print_Inorder(root.right)

def Print_Preorder(root):
    if root is not None:
        # Transverse Root
        print("{} -> ".format(root.data),end=' ')

        # Transverse Left Sub-Tree
        Print_Preorder(root.left)

        # Transverse Right Sub-Tree
        Print_Preorder(root.right)

def Print_Postorder(root):
    if root is not None:
        # Transverse Left Sub-Tree
        Print_Postorder(root.left)

        # Transverse Right Sub-Tree
        Print_Postorder(root.right)

        # Transverse Root
        print("{} -> ".format(root.data),end=' ')

def Insert(node,data):
    if node is None:
        print("\nNew-Node-Data = {} inserted successfully".format(data))
        return Node(data)
    
    if data < node.data:
        node.left = Insert(node.left,data)
    else:
        node.right = Insert(node.right,data)
    
    return node

def Delete(root,key):
    if root is None:
        return root
    
    # To find the node to be Deleted
    if key < root.data:
        root.left = Delete(root.left,key)
    elif key > root.data:
        root.right = Delete(root.right,key)
    else:
        # If the node has only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        # If the node has two children
        temp = root.right.MinValueNode()
        root.data = temp.data

        # Delete the Inorder Successor
        root.right = Delete(root.right,temp.data)
    return root

def MinValueNode(node):
    current = node

    # Find left-most leaf
    while (current.left is not None):
        current = current.left
    
    return current

def Search(root,data,i=0):
    if root is None:
        return -1
    elif root.data==data:
        return i
    else:
        if data < root.data:
            Search(root.left,data,2*i+1)
        else:
            Search(root.right,data,2*i+2)

print("\t\t\t BINARY SEARCH TREE")
print("Enter 1 to Insert Data")
print("Enter 2 to Delete Data")
print("Enter 3 to Print Binary Search Tree")
print("Enter 4 to Search data")
print("Enter 5 to Exit")

root = None

while True:
    choice = int(input("\nEnter your choice: "))

    if choice==1:
        data = int(input("\nEnter the Data to Input: "))
        root = Insert(root,data)
    elif choice==2:
        data = int(input("\nEnter the Data to Delete"))
        root = Delete(root,data)
    elif choice==3:
        print("\nThe Binary Search Tree is: ")
        Print(root)
    elif choice==4:
        key = int(input("\nEnter the Data-Element to be Searched: "))
        index = Search(root,key)
        if index==-1:
            print("\nData-Element = {} is not found in Binary Search Tree".format(data))
        else:
            print("\nData-Element = {} found at Index-Location = {}".format(data,index))
    elif choice==5:
        break
    else:
        print("Invalid choice enetered")
