class queensProblem:
    def __init__(self, value):

        self.numOfQueens = value
        self.chessboard = [
            [None for i in range(self.numOfQueens)] for j in range(self.numOfQueens)
        ]

    def solveQueensProblem(self):

        if self.solve(0):
            self.printanswer()
        else:
            print("Not possible")

    def solve(self, col):

        if col == self.numOfQueens:
            return True

        for row in range(self.numOfQueens):

            if self.isPlaceValid(row, col):

                self.chessboard[row][col] = 1

                if self.solve(col + 1):
                    return True

                self.chessboard[row][col] = 0

        return False

    def isPlaceValid(self, row, col):

        for i in range(col):

            if self.chessboard[row][i] == 1:
                return False

        j = col
        for i in range(row, -1, -1):

            if j < 0:
                break

            if self.chessboard[i][j] == 1:

                return False
            j -= 1

        j = col
        for i in range(row, self.numOfQueens):

            if j < 0:
                break

            if self.chessboard[i][j] == 1:

                return False
            j -= 1

        return True

    def printanswer(self):
        for i in range(self.numOfQueens):

            for j in range(self.numOfQueens):

                if self.chessboard[i][j] == 1:

                    print("  *  ", end="")
                else:
                    print("  -  ", end="")

            print("\n")


if __name__ == "__main__":

    queensProblem = queensProblem(4)
    queensProblem.solveQueensProblem()

