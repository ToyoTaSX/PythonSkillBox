class ArmstrongIterator:
    def __init__(self):
        self.current = 10

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            num = self.current
            order = len(str(num))
            number = [int(d) ** order for d in str(num)]
            summa = sum(number)
            self.current += 1
            if num == summa:
                return num