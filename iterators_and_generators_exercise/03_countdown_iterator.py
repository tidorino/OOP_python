class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.count:
            result = self.count
            self.count -= 1
            return result
        else:
            raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
