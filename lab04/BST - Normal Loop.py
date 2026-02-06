class BST:
    def __init__(self, data: int | None = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def delete(self, data: int) -> int | None:
        if self.is_empty():
            print("Delete Error,", data, "is not found in Binary Search Tree.")
            return None

        parent = None
        current = self

        # Search for the node
        while current and current.data is not None:
            if current.data == data:
                break
            parent = current
            if data < current.data:
                current = current.leftChild
            else:
                current = current.rightChild

        # If node not found
        if current is None or current.data is None or current.data != data:
            print("Delete Error,", data, "is not found in Binary Search Tree.")
            return None

        deleted_val = current.data

        # Case 3: Node has two children
        if current.leftChild and current.rightChild:
            # Find predecessor (max in left subtree)
            p_parent = current
            predecessor = current.leftChild
            while predecessor.rightChild:
                p_parent = predecessor
                predecessor = predecessor.rightChild
            
            # Copy data from predecessor to current
            current.data = predecessor.data
            
            # Now we need to delete the predecessor
            # Predecessor will have at most one child (left child)
            current = predecessor
            parent = p_parent

        # Case 1 & 2: Node has 0 or 1 child
        child = current.leftChild if current.leftChild else current.rightChild

        if parent is None:
            # Deleting the root node (or the object 'delete' was called on)
            if child:
                self.data = child.data
                self.leftChild = child.leftChild
                self.rightChild = child.rightChild
            else:
                self.data = None
                self.leftChild = None
                self.rightChild = None
        else:
            if parent.leftChild == current:
                parent.leftChild = child
            else:
                parent.rightChild = child

        return deleted_val

    def insert(self, data: int) -> None:
        if self.is_empty():
            self.data = data
            return

        current = self
        while True:
            if data < current.data:
                if current.leftChild is None:
                    current.leftChild = BST(data)
                    break
                else:
                    current = current.leftChild
            elif data > current.data:
                if current.rightChild is None:
                    current.rightChild = BST(data)
                    break
                else:
                    current = current.rightChild
            else:
                break

    def traverse(self) -> None:
        if self.preorder():
            print("Preorder: ->", self.preorder() + " ")
            print("Inorder: ->", self.inorder() + " ")
            print("Postorder: ->", self.postorder() + " ")
        else:
            print("This is an empty binary search tree.")

    def preorder(self) -> str:
        node = self

        def _traverse(node):
            if node and not node.is_empty():
                yield node.data
                if node.leftChild: yield from _traverse(node.leftChild)
                if node.rightChild: yield from _traverse(node.rightChild)
        return " -> ".join(map(str, _traverse(node)))

    def inorder(self) -> str:
        node = self

        def _traverse(node):
            if node and not node.is_empty():
                if node.leftChild: yield from _traverse(node.leftChild)
                yield node.data
                if node.rightChild: yield from _traverse(node.rightChild)
        return " -> ".join(map(str, _traverse(node)))

    def postorder(self) -> str:
        node = self

        def _traverse(node):
            if node and not node.is_empty():
                if node.leftChild: yield from _traverse(node.leftChild)
                if node.rightChild: yield from _traverse(node.rightChild)
                yield node.data
        return " -> ".join(map(str, _traverse(node)))

    def is_empty(self) -> bool:
        return self.data is None

    def find_min(self) -> int:
        current = self
        min = None
        while current and current.data is not None:
            min = current.data
            current = current.leftChild
        return min

    def find_max(self) -> int:
        current = self
        max = None
        while current and current.data is not None:
            max = current.data
            current = current.rightChild
        return max

def main():
    my_bst = BST()
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
