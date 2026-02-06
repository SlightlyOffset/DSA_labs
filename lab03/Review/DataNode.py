class DataNode:
    """
    Represents a node in a linked list.

    Attributes:
        data: The value stored in the node.
        next: Reference to the next node in the list.
        prev: Reference to the previous node (unused in SinglyLinkedList, typically for DoublyLinkedList).
    """
    def __init__(self, data: str | None = None):
        self.data = data
        self.next = None
        self.prev = None
