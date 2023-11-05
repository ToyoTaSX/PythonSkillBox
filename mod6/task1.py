class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get(self, index):
        if self.head is None:
            raise IndexError("Empty")

        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data

            current = current.next
            count += 1

        raise IndexError("Incorrect index")

    def remove(self, index):
        if self.head is None:
            raise IndexError("Empty")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Incorrect index")

        prev.next = current.next


    def insert(self, index, data):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        count = 0

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Incorrect Index")

        new_node.next = current
        prev.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next