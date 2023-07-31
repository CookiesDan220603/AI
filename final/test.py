def solve_n_queens(n):
    def dfs(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                dfs(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
    result = []
    dfs([], [], [])
    return result

def print_board(board):
    for row in board:
        print(' '.join(row))

n = 4
solutions = solve_n_queens(n)
if solutions:
    for i, solution in enumerate(solutions):
        print("Solution {}:".format(i+1))
        board = [['.' for _ in range(n)] for _ in range(n)]
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        print_board(board)
else:
    print("No solution found.")