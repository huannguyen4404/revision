def generator_func():
    for i in range(10):
        yield i


for item in generator_func():
    print(item)


def fibo_gen(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# fewer resources :)
# for x in fibo_gen(1000000):
#     print(x)

# highly resources :(
# for x in fibon(1000000):
#     print(x)

int_v = 100797
# iter(int_v)  # Error

str_v = "Henry"
# next(str_v) # Error. Can not iterate directly
str_iter = iter(str_v)
print(next(str_iter))  # >> H
