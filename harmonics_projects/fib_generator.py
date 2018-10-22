def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

def fib2(max):
    numbers = []
    a, b = 0, 1
    while a < max:
        numbers.append(a)
        a, b = b, a + b
    return numbers

numbs = fib(10)
for num in numbs:
    print(num)