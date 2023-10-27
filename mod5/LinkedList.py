class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None or self.tail is None

    def get_length(self):
        if self.is_empty():
            return 0

        c = 1
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            c += 1
        return c

    def add_first(self, data):
        new = Node(data)
        if self.is_empty():
            self.head = new
            self.tail = new
        else:
            first = self.head
            first.prev = new
            self.head = new
            new.next = first

    def add_last(self, data):
        if self.is_empty():
            self.add_first(data)
            return

        new = Node(data)
        last = self.tail
        self.tail = new
        new.prev = last
        last.next = new

    def insert(self, data, index):
        if index == 0:
            self.add_first(data)
            return

        l = self.get_length()
        if index == l:
            self.add_last(data)
            return

        if index > l or index < 0:
            raise IndexError()

        # 1 <= index < length
        new_node = Node(data)
        insert_after_node = self.head
        for i in range(index - 1):
            insert_after_node = insert_after_node.next
        after_new = insert_after_node.next
        prev_new = insert_after_node
        new_node.prev = prev_new
        new_node.next = after_new
        prev_new.next = new_node
        after_new.prev = new_node

    def remove_first(self):
        if self.is_empty():
            return None

        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def remove_last(self):
        if self.is_empty():
            return None

        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        return data

    def remove(self, index):
        if index == 0:
            return self.remove_first()

        l = self.get_length()
        if index == l:
            return self.remove_last()

        if index >= l or index < 0:
            raise IndexError()

        to_delete = self.head.next
        for i in range(2, index + 1):
            to_delete = to_delete.next

        if to_delete.prev:
            to_delete.prev.next = to_delete.next
        if to_delete.next:
            to_delete.next.prev = to_delete.prev

        return to_delete.data

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()