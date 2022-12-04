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
    seen = set()
    for num in nums:
        for i, board in enumerate(boards):
            if i in seen:
                continue
            mark(board, num)
            # input()
            if bingo(board):
                last_board, win_num = board, num
                seen.add(i)
    return score(last_board) * win_num


# Goal: Find the last board to bingo and return it's score
print(play())
