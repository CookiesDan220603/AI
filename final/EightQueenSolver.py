from pysat.solvers import Glucose3

class EightQueenSolver:
    def __init__(self, N=8):
        self.N = N
        self.solver = Glucose3()

    def queen(self, x, y):
        return x * self.N + y + 1

    def row(self, c):
        return (c - 1) // self.N

    def col(self, c):
        return (c - 1) % self.N

    def diagonal_down(self, x, y):
        for i in range(x, self.N - 1):
            for j in range(y, self.N - 1):
                for k in range(i + 1, self.N):
                    l = j + k - i
                    if l < self.N:
                        self.solver.add_clause([-self.queen(i, j), -self.queen(k, l)])

    def diagonal_up(self, x, y):
        for i in range(x, 0, -1):
            for j in range(y, self.N - 1):
                for k in range(i - 1, -1, -1):
                    l = j + i - k
                    if l < self.N:
                        self.solver.add_clause([-self.queen(i, j), -self.queen(k, l)])

    def solve(self):
        for k in range(self.N):
            for i in range(self.N - 1):
                for j in range(i + 1, self.N):
                    self.solver.add_clause([-self.queen(k, i), -self.queen(k, j)])
                    self.solver.add_clause([-self.queen(i, k), -self.queen(j, k)])
            self.solver.add_clause([self.queen(k, i) for i in range(self.N)])

        for i in range(self.N - 1):
            self.diagonal_down(0, i)
            self.diagonal_down(i + 1, 0)
            self.diagonal_up(i + 1, 0)
            self.diagonal_up(self.N - 1, i)

        result = self.solver.solve()

        if result:
            model = self.solver.get_model()
            board = [['.' for _ in range(self.N)] for _ in range(self.N)]
            for q in model:
                if q > 0:
                    r = self.row(q)
                    c = self.col(q)
                    board[r][c] = 'Q'
            for row in board:
                print(' '.join(row))
        else:
            print("No solution")

# Giải quyết bài toán 8-Hậu với N=8
solver = EightQueenSolver()
solver.solve()