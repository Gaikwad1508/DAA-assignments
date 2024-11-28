N = 4  # Size of the board (N x N)

# Function to print the solution board
def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()  # Newline after each row

# Function to check if a queen can be safely placed at board[row][col]
def is_safe(board, row, col):
    # Check the current row on the left side
    for i in range(col):
        if board[row][i]:  # If another queen is found
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:  # If another queen is found
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:  # If another queen is found
            return False

    return True  # Position is safe

# Utility function to solve the N-Queens problem using backtracking
def solve_nq_util(board, col):
    # Base case: If all queens are placed
    if col >= N:
        return True

    # Try placing a queen in each row of the current column
    for i in range(N):
        # Check if placing queen at board[i][col] is safe
        if is_safe(board, i, col):
            board[i][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            if solve_nq_util(board, col + 1):
                return True  # Solution found

            board[i][col] = 0  # Backtrack if placing queen leads to no solution

    return False  # No solution found for this configuration

# Function to solve the N-Queens problem
def solve_nq():
    # Initialize the board with zeros
    board = [[0] * N for _ in range(N)]

    # Start solving from the first column
    if not solve_nq_util(board, 0):
        print("Solution does not exist")  # If no solution exists
        return False

    print_solution(board)  # Print the solution if found
    return True

# Main function to run the program
if __name__ == "__main__":
    solve_nq()  # Call the function to solve N-Queens
