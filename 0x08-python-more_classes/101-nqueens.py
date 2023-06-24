#!/usr/bin/python3

"""
module 101-nqueens
"""

import sys

if len(sys.argv) != 2:
    print("usage: nqueens N\n")
    sys.exit(1)

if not (sys.argv[1].isdigit()):
    print("N must be a number\n")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4\n")
    sys.exit(1)

n = int(sys.argv[1])

board = [[0] * n for _ in range(n)]

def attack(i, j):
    """
    check for queen in row or column
    """
    for x in range(0, n):
        if board[i][x] == 1 or board[x][j] == 1:
            return True

    for x in range(0, n):
        for y in range (0, n):
            if (x + y == i + j) or (x - y == i + j):
                if board[x][y] == 1:
                    return True

    return False

def queen(count):
    """
    count solutions found
    """
    if count == 0:
        return True
    for i in range(0, n):
        for j in range(0, n):
            if (not(attack(i, j))) and (board[i][j] != 1):
                board[i][j] = 1
                if queen(count - 1):
                    return True
                board[i][j] = 0

    return False

queen(n)
for i in board:
    print(i)
