from pysat.solvers import Glucose3
import itertools

# Đọc input
with open('input.txt', 'r') as f:
    m, n = map(int, f.readline().split())
    matrix = []
    for i in range(m):
        row = f.readline().strip().split()
        if len(row) < n:
            row += ['0'] * (n - len(row))
        matrix.append([int(x) if x != '.' else 0 for x in row])

print(matrix)
# Khởi tạo biến

num_variables = m * n
variables = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            variables[i][j] = list(range(i * n + j + 1, (i + 1) * n + j + 1))
        else:
            variables[i][j] = [matrix[i][j]]

# Tạo mệnh đề SAT
cnf = []

# Thêm mệnh đề ràng buộc số ô liền kề
for i in range(m):
    for j in range(n):
        neighbors = []
        for di, dj in itertools.product([-1, 0, 1], repeat=2):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                neighbors.append(variables[ni][nj][0])
        if matrix[i][j] > 0:
            cnf.append([variables[i][j][0]] + [-x for x in neighbors])
            for combination in itertools.combinations(neighbors, matrix[i][j]):
                cnf.append([-variables[i][j][0]] + list(combination))
        else:
            for combination in itertools.combinations(neighbors, 9):
                cnf.append([-variables[i][j][k] for k in range(9) if k + 1 not in combination])

# Giải bài toán bằng Glucose3
solver = Glucose3()
for clause in cnf:
    solver.add_clause(clause)
satisfiable = solver.solve()

# In kết quả nếu có
if satisfiable:
    model = solver.get_model()
    matrix = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if model[variables[i][j][0]-1] > 0:
                matrix[i][j] = str(model[variables[i][j][0]-1])
            else:
                matrix[i][j] = '.'
    for row in matrix:
        print(' '.join(row))
else:
    print('No solution')
