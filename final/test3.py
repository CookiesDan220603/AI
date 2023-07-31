from pysat.solvers import Glucose3

N = 8

def queen(x, y):
    return x * N + y + 1

def row(c):
    return (c - 1) // N

def col(c):
    return (c - 1) % N

def diagonal_down(solver, x, y):
    for i in range(x, N - 1):
        for j in range(y, N - 1):
            for k in range(i + 1, N):
                l = j + k - i
                if l < N:
                    solver.add_clause([-queen(i, j), -queen(k, l)])

def diagonal_up(solver, x, y):
    for i in range(x, 0, -1):
        for j in range(y, N - 1):
            for k in range(i - 1, -1, -1):
                l = j + i - k
                if l < N:
                    solver.add_clause([-queen(i, j), -queen(k, l)])

# Tạo bộ giải quyết
solver = Glucose3()

# Thêm các ràng buộc cho hàng và cột
for k in range(N):
    # Mỗi hàng và cột chỉ có thể có một quân hậu
    for i in range(N - 1):
        for j in range(i + 1, N):
            solver.add_clause([-queen(k, i), -queen(k, j)])
            solver.add_clause([-queen(i, k), -queen(j, k)])
    # Mỗi hàng phải có ít nhất một quân hậu
    solver.add_clause([queen(k, i) for i in range(N)])

# Thêm các ràng buộc cho đường chéo
for i in range(N - 1):
    diagonal_down(solver, 0, i)
    diagonal_down(solver, i + 1, 0)
    diagonal_up(solver, i + 1, 0)
    diagonal_up(solver, N - 1, i)

# Giải quyết bài toán
result = solver.solve()

# In kết quả
if result:
    model = solver.get_model()
    board = [['.' for _ in range(N)] for _ in range(N)]
    for q in model:
        if q > 0:
            r = row(q)
            c = col(q)
            board[r][c] = 'Q'
    for row in board:
        print(' '.join(row))
else:
    print("No solution")