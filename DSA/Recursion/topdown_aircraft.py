class airportmayham(object):
    def __init__(self, arr):

        self.a = arr
        self.sol = 0
        self.dy = [-1] * len(arr)

    def maxpassengers(self):

        return self.helpermax(0)

    def helpermax(self, i):

        if i >= len(self.a):
            return 0

        if self.dy[i] != -1:
            return self.dy[i]

        case1 = self.a[i] + self.helpermax(i + 2)
        case2 = self.helpermax(i + 1)

        self.sol = max(case1, case2)

        self.dy[i] = self.sol

        return self.sol


spacing = airportmayham([155, 55, 2, 96, 67, 203])
print(spacing.maxpassengers())

