class DoubleElement:
    def __init__(self, *lst):
        self.lst = list(lst)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration

        self.index += 2
        if self.index + 1 < len(self.lst):
            return self.lst[self.index], self.lst[self.index + 1]
        return self.lst[self.index], None


    def __iter__(self):
        return self
