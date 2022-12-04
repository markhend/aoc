from itertools import combinations

with open('a.txt', 'r') as f:
    lines = [[int(x) for x in line.split()] for line in f]

# For each row, determine max - min
# the checksum is the sum of all of these differences
print(sum(max(row) - min(row) for row in lines))


# Find the only two numbers in each row where one evenly divides the other.
# Divide them, and add up each line's result.
res = 0
for row in lines:
    for x, y in combinations(row, 2):
        a, b = max(x, y), min(x, y)
        if a % b == 0:
            res += a // b
            break
print(res)
