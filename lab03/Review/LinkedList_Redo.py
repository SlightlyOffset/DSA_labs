from DataNode import DataNode

class SinglyLinkedList:

    def __init__(self, data=None):
        self.head = data
        self.tail = None
        self.count = 0

    def traverse(self) -> None:
        current = self.head
        while current is not None:
            if current.next is None:
                print(current.data)
            else:
                print(current.data, end=" -> ")
            current = current.next

    def insert_last(self, data) -> None:
        new_node = DataNode(data)
        current = self.head

        if current is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # type: ignore
            self.tail = new_node

        self.count += 1

    def insert_front(self, data):
        new_node = DataNode(data)
        current = self.head

        if current is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # type: ignore
            self.head = new_node

        self.count += 1

    def insert_before(self, data, new_data):
        new_node = DataNode(new_data)
        prev = None
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
        prev = None
        current = self.head

        while current is not None:
            if current.data == data:
                if current.data == self.head.data:
                    self.head = current.next # type: ignore
                else:
                    prev.next = current.next # type: ignore

                if current.data == self.tail.data:
                    self.tail = prev
                self.count -= 1
                return
            prev = current
            current = current.next
        print("Cannot delete, " + data + " does not exist.")

