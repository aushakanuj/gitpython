class countderangements_topdown(object):
    def __init__(self, size):

        self.size = size
        self.sol = [-1] * (self.size + 1)

    def count(self):

        return self.count_helper(self.size)

    def count_helper(self, n):

        if self.sol[n] != -1:
            return self.sol[n]

        if n == 1:
            return 0
        if n == 2:
            return 1

        self.sol[n] = (n - 1) * (self.count_helper(n - 1) + self.count_helper(n - 2))

        return self.sol[n]


for i in range(1, 64):
    a = countderangements_topdown(i)
    print(a.count())

