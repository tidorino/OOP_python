def fibonacci():
    num = 0
    current = 1
    yield num
    yield current
    while True:
        result = num + current
        num, current = current, result
        yield result


generator = fibonacci()
for i in range(5):
    print(next(generator))
