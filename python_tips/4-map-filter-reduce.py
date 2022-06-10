items = [1, 2, 3, 4, 5]
squared = []

# for i in items:
#     squared.append(i**2)
squared = list(map(lambda x: x ** 2, items))


def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]
print("# TEST MAP")
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Filter
print("# TEST FILTER")
num_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, num_list))
print(less_than_zero)

# Reduce
from functools import reduce
print("# TEST REDUCE")
product = 1
number_list = [1, 2, 3, 4]
# for num in list:
#     product = product * num
product = reduce(lambda x, y: x * y, number_list)
print(product)
