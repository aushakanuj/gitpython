
def find3(n):
    div = 0
    ndiv = 0
    for i in n:
        if i % 3 == 0:
            div += 1
        else:
            ndiv += 1

    print(div, ndiv)
    if div-ndiv <= 1:
        print("Yes")
    else:
        print("No")


n = int(input())

inputs = []

for i in range(n):

    j = int(input())
    a = list(map(int, input().split()))
    inputs.append(a)

for test in inputs:

    find3(test)
