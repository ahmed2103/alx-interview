#!/usr/bin/python3
"""Module to solve nqueens problem using backtracking"""


from sys import argv, exit


def is_safe(board, size, row, col):
    """Checks if current position is safe."""
    for i in range(size):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, size), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """Solves Nqueens problem"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = list()

    def solve(col):
        """solves nqueens problem recurseve backtracking"""
        if col == n:
            solution = list()
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)

        for i in range(n):
            if is_safe(board, n, i, col):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    for solution in solve_nqueens(n):
        print(solution)
