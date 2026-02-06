class DataNode:
    """
    Represents a node in a linked list.

    Attributes:
        data: The value stored in the node.
        next: Reference to the next node in the list.
        prev: Reference to the previous node (unused in SinglyLinkedList, typically for DoublyLinkedList).
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    """
    Implements a singly linked list.
    """
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def traverse(self):
        """
        Traverses the list and prints the data of each node.

        Concept:
        - Starts from 'head' and moves to 'current.next' until 'current' is None.
        """
        if self.count == 0:
            print("This is an empty list.")
            return

        current = self.head
        while current is not None:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end=" -> ")
            current = current.next

    def insert_last(self, data):
        """
        Inserts a new node with the specified data at the end of the list.

        Concept:
        - If the list is empty, the new node becomes both 'head' and 'tail'.
        - Otherwise, we append the new node to the current 'tail.next' and update 'tail' reference to this new node.
        - This operation is O(1) because we maintain a 'tail' pointer.

        Args:
            data: The data to be inserted.
        """
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # type: ignore
            self.tail = new_node
        self.count += 1

    def insert_front(self, data):
        """
        Inserts a new node with the specified data at the front of the list.

        Concept:
        - The new node's 'next' pointer is set to the current 'head'.
        - The 'head' reference is then updated to point to this new node.
        - If the list was empty, 'tail' is also updated to the new node.

        Args:
            data: The data to be inserted.
        """
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # type: ignore
            self.head = new_node
        self.count += 1

    def insert_before(self, data, new_data):
        """
        Inserts a new node containing new_data before the first occurrence of the node containing data.

        Concept:
        - We traverse the list to find the target node ('data').
        - We maintain a 'prev' pointer to keep track of the node preceding 'current'.
        - Once found:
            1. If it's the head, we update 'head' to the new node.
            2. Otherwise, we link 'prev.next' to the new node, and the new node's 'next' to 'current'.

        Args:
            data: The data to search for.
            new_data: The new data to insert.
        """
        new_node = DataNode(new_data)
        prev = None # Initialize prev
        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.head:
                    new_node.next = self.head # type: ignore
                    self.head = new_node
                else:
                    new_node.next = current # type: ignore
                    prev.next = new_node # type: ignore
                self.count += 1
                return
            prev = current
            current = current.next
        print("Cannot insert, " + data + " does not exist.")

    def delete(self, data):
        """
        Deletes the first occurrence of the node containing the specified data.

        Concept:
        - We traverse the list searching for the node with 'data'.
        - We keep track of the 'prev' node.
        - When the node is found:
            1. If it's the head, simply move 'head' to 'head.next'.
            2. If it's an internal node, bypass it by setting 'prev.next' to 'current.next'.
        - This effectively removes the node from the traversal path.

        Args:
            data: The data to be deleted.
        """
        prev = None # Initialize prev
        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next # type: ignore
                else:
                    prev.next = current.next # type: ignore
                self.count -= 1
                return
            prev = current
            current = current.next
        print("Cannot delete, " + data + " does not exist.")

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input().strip()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

if __name__ == "__main__":
    main()
