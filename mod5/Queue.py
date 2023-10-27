from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def pop(self):
        return self.list.remove_first()

    def push(self, val):
        self.list.add_last(val)

    def insert(self, n, val):
        self.list.insert(val, n)

    def print(self):
        self.list.print_list()

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.insert(1, "ins")
q.print()
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())