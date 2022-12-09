with open("in.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
t = []
for line in lines:
    t.append([int(c) for c in list(line)])
    # print(line)


# grid of tree heights 0-9
# Measure the viewing distance from a given tree, look up, down, left,
# and right from that tree; stop if you reach an edge or at the first
# tree that is the same height or taller than the tree under consideration.
# A tree's scenic score is found by multiplying together its viewing distance
# in each of the four directions. For this tree, this is 4 (found by
# multiplying 1 * 1 * 2 * 2).


cols = range(0, len(t))
rows = range(0, len(t))


def scenic_score(i, j):
    up, down, right, left = 0, 0, 0, 0
    # print(tree, end='')

    # check up, i less j same
    dir = "up"
    for m in range(i-1, -1, -1):
        n = j
        up += 1
        # print(f"  {t[m][n]=} {up=}")
        if tree <= t[m][n]:
            break

    # check down, i more j same
    dir = "down"
    for m in range(i+1, len(t)):
        n = j
        down += 1
        if tree <= t[m][n]:
            break

    # check left, i same j less
    dir = "left"
    for n in range(j-1, -1, -1):
        m = i
        left += 1
        if tree <= t[m][n]:
            break

    # check right, i same j more
    dir = "right"
    for n in range(j+1, len(t)):
        m = i
        right += 1
        if tree <= t[m][n]:
            break

    return up * down * right * left


scenic = 0
for i in rows:
    for j in cols:
        tree = t[i][j]
        scenic = max(scenic, scenic_score(i, j))
print(f"part 2 {scenic=}")
