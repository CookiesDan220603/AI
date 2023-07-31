from pysat.solvers import Glucose3

class EightQueenSolver:
    def __init__(self):
        self.solver = Glucose3()
    
    def add_clause(self, clause):
        self.solver.add_clause(clause)
    
    def solve(self):
        for i in range(1, 9):
            for j in range(1, 9):
                # Cột j không được có quân hậu nào khác
                column = [(i, k) for k in range(1, 9) if k != j]
                column_clause = [[-self.get_var(row, col)] for row, col in column]
                self.add_clause(column_clause)
                
                # Hàng i không được có quân hậu nào khác
                row = [(k, j) for k in range(1, 9) if k != i]
                row_clause = [[-self.get_var(row, col)] for row, col in row]
                self.add_clause(row_clause)
                
                # Đường chéo chính không được có quân hậu nào khác
                diagonal1 = [(k, l) for k in range(1, 9) for l in range(1, 9) if abs(k - i) == abs(l - j) and (k, l) != (i, j)]
                diagonal1_clause = [[-self.get_var(row, col), -self.get_var(i, j)] for row, col in diagonal1]
                self.add_clause(diagonal1_clause)
                
                # Đường chéo phụ không được có quân hậu nào khác
                diagonal2 = [(k, l) for k in range(1, 9) for l in range(1, 9) if k + l == i + j and (k, l) != (i, j)]
                diagonal2_clause = [[-self.get_var(row, col), -self.get_var(i, j)] for row, col in diagonal2]
                self.add_clause(diagonal2_clause)
        
        # Giải quyết bài toán
        result = self.solver.solve()
        
        # In kết quả
        if result:
            for i in range(1, 9):
                row = ""
                for j in range(1, 9):
                    if self.get_var(i, j) in self.solver.get_model():
                        row += "Q "
                    else:
                        row += ". "
                print(row)
        else:
            print("No solution")
    
    def get_var(self, i, j):
        return (i - 1) * 8 + j
# Tạo đối tượng EightQueenSolver
solver = EightQueenSolver()

# Giải quyết bài toán và in kết quả ra màn hình
solver.solve()