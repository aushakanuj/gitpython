for _ in range(int(input())):

    n = int(input())

    arr = list(map(int, input().split()))

    left = [0]*(n + 1)

    for i in range(n):

        left[i + 1] = left[i] ^ arr[i]

    for __ in range(int(input())):

        l, r = map(int, input().split())

        print(left[l] ^ left[r+1])
