from OnceLinkedList import OnceLinkedList
class Stack:
    def __init__(self):
        self.list = OnceLinkedList()

    def pop(self):
        return self.list.remove_first()

    def push(self, val):
        self.list.add_first(val)

    def print(self):
        self.list.print_list()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.print()
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())