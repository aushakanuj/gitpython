# factorial
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


result = 1


def factorial1(n, result):

    if n == 1:
        return result

    return factorial1(n - 1, n * result)


print(factorial1(5, 1))
