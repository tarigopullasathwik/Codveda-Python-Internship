def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            solve_n_queens(board, row + 1, n)
            board[row][col] = "."

    return False


def main():
    n = int(input("Enter number of queens: "))
    board = [["." for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)


if __name__ == "__main__":
    main()
