def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # Check if the number already exists in the row
        for c in range(9):
            if board[row][c] == num:
                return False
        
        # Check if the number already exists in the column
        for r in range(9):
            if board[r][col] == num:
                return False
        
        # Check if the number already exists in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == num:
                    return False
        
        return True

    def find_empty(board):
        # Find the first empty spot (0)
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return -1, -1  # No empty cell left

    def solve(board):
        row, col = find_empty(board)
        if row == -1 and col == -1:
            return True  # No empty cells left, puzzle is solved
        
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num  # Try placing the number
                if solve(board):  # Recurse
                    return True
                board[row][col] = 0  # Backtrack
        
        return False  # If no number works, backtrack

    solve(board)
    return board  # Return the solved board

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved_board = solve_sudoku(board)
for row in solved_board:
    print(row)