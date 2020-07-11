class countderangements(object):
    def __init__(self, size):

        self.size = size

    def count(self):

        return self.count_helper(self.size)

    def count_helper(self, n):

        if n == 1:
            return 0
        if n == 2:
            return 1

        return (n - 1) * (self.count_helper(n - 1) + self.count_helper(n - 2))


for i in range(1, 11):
    a = countderangements(i)
    print(a.count())

