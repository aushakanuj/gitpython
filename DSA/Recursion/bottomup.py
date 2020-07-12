class countderangements(object):
    def __init__(self, size):

        self.size = size
        self.sol = [-1] * (self.size + 1)

        for n in range(1, self.size + 1):
            if n == 1:
                self.sol[n] = 0
            elif n == 2:
                self.sol[n] = 1
            else:
                self.sol[n] = (n - 1) * (self.sol[n - 1] + self.sol[n - 2])

    def count(self):

        return self.count_helper(self.size)

    def count_helper(self, n):

        return self.sol[n]


for i in range(1, 20):
    a = countderangements(i)
    print("{} has the value {}".format(i, a.count()))

