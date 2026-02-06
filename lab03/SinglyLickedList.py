class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def traverse(self):
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
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

def main():
    sll = SinglyLinkedList()
    for _ in range(int(input())):
        sll.insert_last(input().strip())
    sll.traverse()

if __name__ == "__main__":
    main()
