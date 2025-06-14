class Node:
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root
# def insert(self, data):
    #     n = Node(item=data)
    #     if self.root is None:
    #         self.root = n
    #     else:
    #         temp = self.root
    #         parent = None
    #         while temp is not None:  
    #             parent = temp 
    #             if data < temp.item:
    #                 temp = temp.left
    #             else:
    #                 temp = temp.right

    #         if parent.item < data:
    #             parent.right = n
    #         else:
    #             parent.left = n
    # WITH RECURSION
    def insert(self, data):
        self.root = self.insert_recursive(self.root, data)

    def insert_recursive(self, root, data):
        if root is None:
            return Node(item=data)  
        if data < root.item:
            root.left = self.insert_recursive(root.left, data)
        elif data > root.item:
            root.right = self.insert_recursive(root.right, data)
        return root
    def search(self,data):
        return self.search_recursive(self.root,data)
    def search_recursive(self,root,data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.search_recursive(root.left , data)
        else:
            return self.search_recursive(root.right ,data)

    def inorder(self, node=None):
        if node is None:  
            return
        if node is not None:
            self.inorder(node.left)
            print(node.item, end=' ')
            self.inorder(node.right)
    def preorder(self, node=None):
        if node is None:  
            return
        if node is not None:
            print(node.item, end=' ')
            self.inorder(node.left)
            self.inorder(node.right)
    def postorder(self, node=None):
        if node is None:  
            return
        if node is not None:
            self.inorder(node.left)
            self.inorder(node.right)
            print(node.item, end=' ')

        

bst = BST()
bst.insert(5)
bst.insert(15)
bst.insert(4)
bst.preorder(bst.root)
print()
bst.inorder(bst.root)
print()
bst.postorder(bst.root)  
node = bst.search(15)
print()
print(node.item)

