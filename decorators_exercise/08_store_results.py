from functools import wraps


def store_results(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        with open('./results.txt', 'a') as file:
            file.write(f"Function '{function.__name__}' was called. Result: {result}")
            file.write('\n')
        return result

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
