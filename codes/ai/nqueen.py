def is_safe(board, row, col, n): 
    for i in range(row):
        # Check same column
        if board[i] == col:
            return False
        # Check left diagonal
        if board[i] - i == col - row:
            return False
        # Check right diagonal
        if board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])  # Found a solution, add it to solutions list
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack

def print_solution(board, n):
    for row in range(n):
        row_str = ['Q' if col == board[row] else '.' for col in range(n)]
        print(" ".join(row_str))
    print()

def n_queens(n):
    board = [-1] * n  # One-dimensional board, -1 indicates empty row
    solutions = []
    solve_n_queens(board, 0, n, solutions)

    if not solutions:
        print("No solution exists.")
    else:
        print(f"Total solutions: {len(solutions)}\n")
        for idx, solution in enumerate(solutions):
            print(f"Solution {idx + 1}:")
            print_solution(solution, n)

# -------- Main --------
n = int(input("Enter the number of queens (n): "))
n_queens(n)