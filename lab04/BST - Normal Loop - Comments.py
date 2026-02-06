class BST:
    """
    Binary Search Tree (BST) implementation using iterative methods for insertion and deletion.
    """
    def __init__(self, data: int | None = None):
        """
        Initialize the BST node.

        Args:
            data: The integer value to store in the node. Defaults to None for an empty tree.
        """
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def delete(self, data: int) -> int | None:
        """
        Iteratively deletes a node with the specified data from the BST.

        Args:
            data: The value to delete.

        Returns:
            The deleted value if found, otherwise None.
        """
        if self.is_empty():
            print("Delete Error, ", data, " is not found in Binary Search Tree.")
            return None

        parent = None
        current = self

        # Search for the node to delete and its parent
        while current and current.data is not None:
            if current.data == data:
                break
            parent = current
            if data < current.data:
                current = current.leftChild
            else:
                current = current.rightChild

        # If node not found (hit None or data mismatch)
        if current is None or current.data is None or current.data != data:
            print("Delete Error, ", data, " is not found in Binary Search Tree.")
            return None

        deleted_val = current.data

        # Case 3: Node has two children
        # Strategy: Replace current node's value with its predecessor's value (max in left subtree),
        # then delete the predecessor node (which will have at most one child).
        if current.leftChild and current.rightChild:
            # Find predecessor (rightmost node in the left subtree)
            p_parent = current
            predecessor = current.leftChild
            while predecessor.rightChild:
                p_parent = predecessor
                predecessor = predecessor.rightChild

            # Copy data from predecessor to the current node
            current.data = predecessor.data

            # Now target the predecessor for deletion
            current = predecessor
            parent = p_parent

        # Case 1 & 2: Node has 0 or 1 child
        # Identify the single child (if any) to link to the parent
        child = current.leftChild if current.leftChild else current.rightChild

        if parent is None:
            # Deleting the root node itself
            if child:
                # Replace root data and structure with the child's
                self.data = child.data
                self.leftChild = child.leftChild
                self.rightChild = child.rightChild
            else:
                # Tree becomes empty
                self.data = None
                self.leftChild = None
                self.rightChild = None
        else:
            # Link the parent directly to the child, bypassing the current node
            if parent.leftChild == current:
                parent.leftChild = child
            else:
                parent.rightChild = child

        return deleted_val

    def insert(self, data: int) -> None:
        """
        Iteratively inserts a new integer into the BST.

        Args:
            data: The integer value to insert.
        """
        if self.is_empty():
            self.data = data
            return

        current = self
        while True:
            if data < current.data:
                # Go left
                if current.leftChild is None:
                    # Found insertion spot
                    current.leftChild = BST(data)
                    break
                else:
                    current = current.leftChild
            elif data > current.data:
                # Go right
                if current.rightChild is None:
                    # Found insertion spot
                    current.rightChild = BST(data)
                    break
                else:
                    current = current.rightChild
            else:
                # Duplicate value; do nothing (or handle as needed)
                break

    def traverse(self) -> None:
        """
        Prints the Preorder, Inorder, and Postorder traversals of the tree.
        """
        print("Preorder: ->", self.preorder() + " ")
        print("Inorder: ->", self.inorder() + " ")
        print("Postorder: ->", self.postorder() + " ")

    def preorder(self) -> str:
        """
        Performs a preorder traversal (Root -> Left -> Right).

        Returns:
            A string representation of the traversal.
        """
        node = self

        def _traverse(node):
            if node and not node.is_empty():
                yield node.data
                if node.leftChild: yield from _traverse(node.leftChild)
                if node.rightChild: yield from _traverse(node.rightChild)
        return " -> ".join(map(str, _traverse(node)))

    def inorder(self) -> str:
        """
        Performs an inorder traversal (Left -> Root -> Right).
        Sorted order for BSTs.

        Returns:
            A string representation of the traversal.
        """
        node = self

        def _traverse(node):
            if node and not node.is_empty():
                if node.leftChild: yield from _traverse(node.leftChild)
                yield node.data
                if node.rightChild: yield from _traverse(node.rightChild)
        return " -> ".join(map(str, _traverse(node)))

    def postorder(self) -> str:
        """
        Performs a postorder traversal (Left -> Right -> Root).

        Returns:
            A string representation of the traversal.
        """
        node = self

        def _traverse(node):
            if node and not node.is_empty():
                if node.leftChild: yield from _traverse(node.leftChild)
                if node.rightChild: yield from _traverse(node.rightChild)
                yield node.data
        return " -> ".join(map(str, _traverse(node)))

    def is_empty(self) -> bool:
        """
        Check if the current node (usually root) is empty.
        """
        return self.data is None

    def find_min(self) -> int:
        """
        Finds the minimum value in the BST (leftmost node).
        """
        current = self
        min_val = None
        while current and current.data is not None:
            min_val = current.data
            current = current.leftChild
        return min_val

    def find_max(self) -> int:
        """
        Finds the maximum value in the BST (rightmost node).
        """
        current = self
        max_val = None
        while current and current.data is not None:
            max_val = current.data
            current = current.rightChild
        return max_val

def main():
    """
    Main function to interact with the BST via console input.
    Accepts commands:
    I: <number> -> Insert
    D: <number> -> Delete
    Done -> Exit and print traversals
    """
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