with open("in.txt", "r") as f:
    moves = []
    for line in f:
        dir, n = line.split()
        moves.append((dir, int(n)))
    # print(moves)

T_visited = {(0, 0)}

# Rather than two knots, you now must simulate a rope consisting of
# ten knots. One knot is still the head of the rope and moves according
# to the series of motions. Each knot further down the rope follows the
# knot in front of it using the same rules as before.

# move directions = R, L, U, D, followed by dist n
H = [0, 0]  # [x, y]
tails = [[0, 0] for _ in range(9)]
# print(tails)
visited = {(0, 0)}  # T9 locations


def update(H, T):  # part B have to account for 2 steps away diagonally
    x1, y1, x2, y2 = H[0], H[1], T[0], T[1]
    # print(x1, y1, x2, y2)
    if abs(x1 - x2) < 2 and abs(y1 - y2) < 2:  # within 1 step
        return

    if abs(x1 - x2) == 2 and abs(y1 - y2) == 2:  # 2 steps diag
        if y1 > y2:
            y2 += 1
            x2 += 1 if x1 > x2 else -1
        elif y1 < y2:
            y2 -= 1
            x2 += 1 if x1 > x2 else -1
    elif abs(y1 - y2) == 2:  # 2 steps above or below
        y2 += 1 if y1 > y2 else -1
        x2 = x1
    elif abs(x1 - x2) == 2:  # 2 steps right or left
        x2 += 1 if x1 > x2 else -1
        y2 = y1
    # T = [x2, y2]
    T[0], T[1] = x2, y2
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
        # move all the tails
        head = H
        for tail in tails:
            update(head, tail)
            head = tail
        visited.add(tuple(tail))
    # print(H, T)
# print(visited)
print(len(visited))
