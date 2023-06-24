#!/usr/bin/python3

"""
module 101-nqueen
"""


def safe(board, row, col):
    for x in range(col):
        if board[x] is row or abs(board[x] - row) is abs(x - col):
            return False
    return True


def the_board(board, col):
    n = len(board)
    if col is n:
        print(str([[c, board[c]] for c in range(n)]))
        return

    for row in range(n):
        if safe(board, row, col):
            board[col] = row
            the_board(board, col + 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not (sys.argv[1].isdigit()):
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    board = [0 for col in range(n)]
    the_board(board, 0)
