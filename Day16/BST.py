class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def addNode(self,data):
        if self.root==None:
            newnode = Node(data)
            self.root = newnode
        else:
            if self.root.data<data:
                if self.root.left==None:
                    self.root.left = Node(data)
                else:
                    self.addNode(self.root.left,data)
            else:
                if self.root.data>data:
                    if self.root.right==None:
                        self.root.right = Node(data)
                    else:
                        self.addNode(self.root.right,data)
    def inorder(self):
        if self.root==None:
            return
        else:
            self.inorder()

ob = BST()
ob.addNode(10)

