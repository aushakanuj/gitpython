# head recurrsion


def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    fib1 = fibonacci(n - 1)
    fib2 = fibonacci(n - 2)

    return fib1 + fib2


# tail recurrsion


def fibo(n, a=0, b=1):

    if n == 1:
        return b

    return fibo(n - 1, b, a + b)

