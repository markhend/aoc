with open("a.txt", "r") as f:
    lines = []
    for line in f.readlines():
        lines.append(line.strip().replace(' -> ', ',').split(','))
    lines = [[*map(int, line)] for line in lines]

# NxN grid, (0, 0) top left  (N-1, N-1) bottom right
# Each row in file has format x1,y1 -> x2,y2
# where x1,y1 and x2,y2 are line endpoints.
# Only consider horizontal and vertical lines: either x1 = x2 or y1 = y2.
# At how many points do at least two lines overlap?

# intialize grid with all '.'
# N = max(c for line in lines for c in line) + 1
grid = [[0 for _ in range(1000)] for _ in range(1000)]
diagonal_lines = []

for line in lines:
    x1, y1, x2, y2 = line
    if x1 == x2:  # vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1
    elif y1 == y2:  # horizontal
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1
    else:
        diagonal_lines.append(line)

overlaps = len([point for row in grid for point in row if point > 1])
print(overlaps)


# Add diagonal lines
for line in diagonal_lines:
    x1, y1, x2, y2 = line
    # swap endpoint order if necessary so x1 < x2
    if x1 > x2:
        x2, y2, x1, y1 = x1, y1, x2, y2

    if y1 < y2:  # decline - x and y both increase
        for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
            grid[y][x] += 1

    else:  # incline - x increases and y decreases
        for x, y in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1)):
            grid[y][x] += 1

overlaps = len([point for row in grid for point in row if point > 1])
print(overlaps)
