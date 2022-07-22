class dictionary_iter:
    def __init__(self, dictionary_obj):
        self.dictionary_obj = list(dictionary_obj.items())
        self.i = 0
        self.end = len(dictionary_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.end <= self.i:
            raise StopIteration
        current = self.dictionary_obj[self.i]
        self.i += 1
        return current


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
