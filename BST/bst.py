class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root

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

    def search(self, data):
        return self.search_recursive(self.root, data)

    def search_recursive(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.search_recursive(root.left, data)
        return self.search_recursive(root.right, data)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return self._inorder(node)

    def _inorder(self, node):
        if node is None:
            return []
        result = []
        result.extend(self._inorder(node.left))
        result.append(node.item)
        result.extend(self._inorder(node.right))
        return result

    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return self._preorder(node)

    def _preorder(self, node):
        if node is None:
            return []
        result = [node.item]
        result.extend(self._preorder(node.left))
        result.extend(self._preorder(node.right))
        return result

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        return self._postorder(node)

    def _postorder(self, node):
        if node is None:
            return []
        result = []
        result.extend(self._postorder(node.left))
        result.extend(self._postorder(node.right))
        result.append(node.item)
        return result


if __name__ == "__main__":
    bst = BST()
    for value in [5, 15, 4]:
        bst.insert(value)
    print(bst.preorder())
    print(bst.inorder())
    print(bst.postorder())
    node = bst.search(15)
    print(node.item if node is not None else None)

