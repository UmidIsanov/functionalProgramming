def apply_callback(callback, lst):
    result = []
    for item in lst:
        result.append(callback(item))
    return result


def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
result = apply_callback(square, numbers)
print(result)
