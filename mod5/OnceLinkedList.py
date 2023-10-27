class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class OnceLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        if self.is_empty():
            return 0

        c = 1
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            c += 1
        return c

    def is_empty(self):
        return self.head is None

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def add_first(self, data):
        new_node = Node(data)
        first_node = self.head
        self.head = new_node
        if first_node:
            self.head.next = first_node

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
        insert_before_node = insert_after_node.next
        insert_after_node.next = new_node
        new_node.next = insert_before_node



    def remove_first(self):
        if self.is_empty():
            return None

        data = self.head.data
        self.head = self.head.next
        return data


    def remove_last(self):
        if self.is_empty():
            return None

        if self.head.next is None:
            self.head = None
            return None

        prev_node = self.head
        node_to_delete = prev_node.next
        while node_to_delete.next:
            prev_node = node_to_delete
            node_to_delete = node_to_delete.next

        prev_node.next = None
        return node_to_delete.data


    def remove_by_index(self, index):
        if index == 0:
            return self.remove_first()

        l = self.get_length()
        if index == l:
            return self.remove_last()

        if index >= l or index < 0:
            raise IndexError()

        # 1 <= index < l
        prev = self.head
        to_delete = prev.next
        for i in range(2, index + 1):
            prev = to_delete
            to_delete = to_delete.next

        after_delete = to_delete.next
        prev.next = after_delete
        return to_delete.data

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()
