class BSTNode:
    def __init__(self, data: int | None = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data: int) -> None:
        if self.is_empty():
            self.data = data
        else:
            if data < self.data:
                if self.leftChild is None:
                    self.leftChild = BSTNode(data)
                else:
                    self.leftChild.insert(data)
            else:
                if self.rightChild is None:
                    self.rightChild = BSTNode(data)
                else:
                    self.rightChild.insert(data)

    def delete(self, data: int) -> int | None:
        if self.is_empty():
            print("Delete Error, ", data, " is not found in Binary Search Tree.")
            return None

        # search left
        if data < self.data:
            if self.leftChild:
                deleted = self.leftChild.delete(data)
                # remove empty child
                if self.leftChild.is_empty():
                    self.leftChild = None
                return deleted
            else:
                print("Delete Error, ", data, " is not found in Binary Search Tree.")
                return None

        # search right
        elif data > self.data:
            if self.rightChild:
                deleted = self.rightChild.delete(data)
                # remove empty child
                if self.rightChild.is_empty():
                    self.rightChild = None
                return deleted
            else:
                print("Delete Error, ", data, " is not found in Binary Search Tree.")
                return None

        # ===== node found =====
        deleted_value = self.data

        # case 1: leaf node
        if self.leftChild is None and self.rightChild is None:
            self.data = None
            return deleted_value

        # case 2: only left subtree
        if self.leftChild and self.rightChild is None:
            child = self.leftChild
            self.data = child.data
            self.leftChild = child.leftChild
            self.rightChild = child.rightChild
            return deleted_value

        # case 3: only right subtree
        if self.rightChild and self.leftChild is None:
            child = self.rightChild
            self.data = child.data
            self.leftChild = child.leftChild
            self.rightChild = child.rightChild
            return deleted_value

        # case 4: two subtrees
        max_val = self.leftChild.find_max()
        self.data = max_val
        self.leftChild.delete(max_val)
        if self.leftChild.is_empty():
            self.leftChild = None
        return deleted_value

    def find_min(self) -> int:
        if self.leftChild is None:
            return self.data
        else:
            return self.leftChild.find_min()

    def find_max(self) -> int:
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.find_max()

    def traverse(self):
        print(self.preorder() + " ")
        print(self.inorder() + " ")
        print(self.postorder() + " ")

    def preorder(self):

        def _traverse(node):
            if node and not node.is_empty():
                yield str(node.data)
                if node.leftChild:
                    yield from _traverse(node.leftChild)
                if node.rightChild:
                    yield from _traverse(node.rightChild)

        return "Preorder: -> " + " -> ".join(_traverse(self))

    def inorder(self):

        def _traverse(node):
            if node and not node.is_empty():
                if node.leftChild:
                    yield from _traverse(node.leftChild)
                yield str(node.data)
                if node.rightChild:
                    yield from _traverse(node.rightChild)

        return "Inorder: -> " + " -> ".join(_traverse(self))

    def postorder(self):

        def _traverse(node):
            if node and not node.is_empty():
                if node.leftChild:
                    yield from _traverse(node.leftChild)
                if node.rightChild:
                    yield from _traverse(node.rightChild)
                yield str(node.data)

        return "Postorder: -> " + " -> ".join(_traverse(self))

    def is_empty(self):
        return self.data is None

def main():
    my_bst = BSTNode()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

if __name__ == "__main__":
    main()
