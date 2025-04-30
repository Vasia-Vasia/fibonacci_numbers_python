def fib(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    elif n >= 2:
        result = fib(n-1) + fib(n-2)

    return result

# Проверка

n = 7
print(fib(n))