class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < self.number:
            text = self.sequence[self.i % len(self.sequence)]
            self.i += 1
            return text
        else:
            raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
