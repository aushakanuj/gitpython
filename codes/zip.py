L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

# lt=filter((zip(L1,L2)),lambda num: num[0]>10 and num[1]<5)
# print(list(lt))

L3 = [num[0] + num[1] for (num) in zip(L1, L2) if num[0] > 10 and num[1] < 5]
print(L3)


l3 = map(lambda num: num[0] + num[1], zip(L1, L2))
print(list(l3))


l4 = filter(lambda num: num[0] > 10 and num[1 < 5], zip(L1, L2))

l3 = map(lambda num: num[0] + num[1], l4)
print(list(l3))
