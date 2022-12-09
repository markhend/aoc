with open("in.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
t = []
for line in lines:
    t.append([int(c) for c in list(line)])
    # print(line)


# grid of tree heights 0-9
# Tree is visible if all trees between it and the border are shorter.
# All border trees are visible.
# How many trees are visible?

rows = range(1, len(t)-1)
cols = range(1, len(t)-1)


def is_visible(i, j):
    up, down, right, left = True, True, True, True

    # check up, i less j same
    for m in range(0, i):
        dir = "up"
        n = j
        if tree <= t[m][n]:
            up = False
            break

    # check down, i more j same
    for m in range(i+1, len(t)):
        dir = "down"
        n = j
        if tree <= t[m][n]:
            down = False
            break

    # check left, i same j less
    for n in range(0, j):
        dir = "left"
        m = i
        if tree <= t[m][n]:
            left = False
            break

    # check right, i same j more
    for n in range(j+1, len(t)):
        dir = "right"
        m = i
        if tree <= t[m][n]:
            right = False
            break

    return up or down or right or left


visible = 4 * len(t) - 4
for i in rows:
    for j in cols:
        tree = t[i][j]
        if is_visible(i, j):
            visible += 1
print(f"part 1 {visible=}")
