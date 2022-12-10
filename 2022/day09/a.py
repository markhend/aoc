with open("in.txt", "r") as f:
    moves = []
    for line in f:
        dir, n = line.split()
        moves.append((dir, int(n)))
    # print(moves)

T_visited = {(0, 0)}

# If the head is ever two steps directly up, down, left, or right
# from the tail, the tail must also move one step in that direction
# so it remains close enough:
# Otherwise, if the head and tail aren't touching and aren't in the
# same row or column, the tail always moves one step diagonally
# to keep up: update state while keeping track of T location

# move directions = R, L, U, D, followed by dist n
H = [0, 0]  # [x, y]
T = [0, 0]
visited = {(0, 0)}  # T locations


def update():
    global T
    x1, y1, x2, y2 = H[0], H[1], T[0], T[1]
    # print(x1, y1, x2, y2)
    if abs(x1 - x2) < 2 and abs(y1 - y2) < 2:  # within 1 step
        return
    if abs(y1 - y2) == 2:  # 2 steps above or below
        y2 += 1 if y1 > y2 else -1
        x2 = x1
    if abs(x1 - x2) == 2:  # 2 steps right or left
        x2 += 1 if x1 > x2 else -1
        y2 = y1
    visited.add((x2, y2))
    T = [x2, y2]
    return


for move in moves:
    dir, dist = move
    dist = int(dist)
    # print(dir, dist)

    # move H
    for _ in range(dist):
        match dir:
            case 'R': H[0] += 1
            case 'L': H[0] -= 1
            case 'U': H[1] += 1
            case 'D': H[1] -= 1
        update()
    # print(H, T)
# print(visited)
print(len(visited))
