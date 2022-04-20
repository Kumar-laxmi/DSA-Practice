class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
 
class AVL_Tree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
 
        balance = self.getBalance(root)
 
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def delete(self, root, key):
 
        # Step 1 - Perform standard BST delete
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,temp.val)
 
 
        if root is None:
            return root
 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
 
        balance = self.getBalance(root)
 
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, root):
 
        y = root.right
        T2 = y.left
 
        # Perform rotation
        y.left = root
        root.right = T2
 
        # Update heights
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, root):
 
        y = root.left
        T3 = y.right
 
        # Perform rotation
        y.right = root
        root.left = T3
 
        # Update heights
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
   
    def Search(self,root,data):
        if not root:
            return -1
        if root.val==data:
            return 1
        if data < root.val:
            self.Search(root.left,data)
        else:
            self.Search(root.right,data)
   
    def Print(self,root):
        print("Inorder Transversal of Binary Search Tree: ")
        self.Print_Inorder(root)
        print("\nPre-order Transversal of Binary Search Tree: ")
        self.Print_Preorder(root)
        print("\nPost-order Transversal of Binary Search Tree: ")
        self.Print_Postorder(root)
 
    def Print_Inorder(self,root):
        if root is not None:
            # Transverse Left
            self.Print_Inorder(root.left)
 
            # Transverse Root
            print("{} -> ".format(root.val),end=' ')
 
            # Transverse Right
            self.Print_Inorder(root.right)
 
    def Print_Preorder(self,root):
        if root is not None:
            # Transverse Root
            print("{} -> ".format(root.val),end=' ')
 
            # Transverse Left Sub-Tree
            self.Print_Preorder(root.left)
 
            # Transverse Right Sub-Tree
            self.Print_Preorder(root.right)
 
    def Print_Postorder(self,root):
        if root is not None:
            # Transverse Left Sub-Tree
            self.Print_Postorder(root.left)
 
            # Transverse Right Sub-Tree
            self.Print_Postorder(root.right)
 
            # Transverse Root
            print("{} -> ".format(root.val),end=' ')
 
print("\t\t\t AVL TREE")
print("Enter 1 to Insert Data")
print("Enter 2 to Delete Data")
print("Enter 3 to Print Binary Search Tree")
print("Enter 4 to Search data")
print("Enter 5 to Exit")
 
tree = AVL_Tree()
root = None
 
while True:
    choice = int(input("\nEnter your choice: "))
 
    if choice==1:
        data = int(input("\nEnter the Data to Input: "))
        root = tree.insert(root,data)
    elif choice==2:
        data = int(input("\nEnter the Data to Delete"))
        root = tree.delete(root,data)
    elif choice==3:
        print("\nThe Binary Search Tree is: ")
        tree.Print(root)
    elif choice==4:
        key = int(input("\nEnter the Data-Element to be Searched: "))
        index = tree.Search(root,key)
        if index==-1:
            print("\nData-Element = {} is not found in Binary Search Tree".format(data))
        else:
            print("\nData-Element = {} found at Index-Location = {}".format(data,index))
    elif choice==5:
        break
    else:
        print("Invalid choice enetered")

