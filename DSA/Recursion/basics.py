# head recursion
def numbers(n):

    if n == 0:
        return
    numbers(n - 1)
    print(n)


numbers(10)


# tail recursion
def numbers2(n):

    if n == 0:
        return
    print(n)
    numbers2(n - 1)


numbers2(10)

