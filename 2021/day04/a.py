with open("a.txt", "r") as f:
    nums = [int(n) for n in f.readline().strip().split(',')]
    lines = f.read().splitlines()

boards = []
for line in lines:
    if line == '':
        boards.append([])
    else:
        boards[-1].append([int(c) for c in line.split()])


def bingo(board):
    # any row all -1s?
    for row in board:
        if all(n == -1 for n in row):
            return True

    # any column all -1s?
    for c in range(5):
        column = []
        for r in range(5):
            column.append(board[r][c])
        if all(n == -1 for n in column):
            return True

    return False


def mark(board, n):
    for row in range(5):
        for col in range(5):
            if board[row][col] == n:
                board[row][col] = -1


def score(board):
    return sum(n for row in board for n in row if n != -1)


def play():
    for num in nums:
        for board in boards:
            mark(board, num)
            # input()
            if bingo(board):
                return score(board) * num


print(play())

# board1 = [[42, 9, 63, 56, 93],
#           [79, 59, 38, 36, 7],
#           [-1, -1, -1, -1, -1],
#           [82, 45, 13, 27, 83],
#           [1, 32, 8, 40, 46]]

# board2 = [[42, 9, -1, 56, 93],
#           [79, 59, -1, 36, 7],
#           [6, 23, -1, 0, 55],
#           [82, 45, -1, 27, 83],
#           [1, 32, -1, 40, 46]]

# print(bingo(board1))
# print(bingo(board2))
