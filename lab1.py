from functools import reduce

numbers = [2, -3, 5, -7, 11, -13, 17]

positive_numbers = list(filter(lambda x: x > 0, numbers))

product_of_positive_numbers = reduce(lambda x, y: x * y, positive_numbers, 1)


print(f"Ответ: {product_of_positive_numbers}")
