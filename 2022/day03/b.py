# Each rucksack has two large compartments. All items of a
# given type are meant to go into exactly one of the two compartments

# A given rucksack always has the same number of items in each of
# its two compartments

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# part a:
# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?

# part b:
# Every set of three lines in your list corresponds to a single group.
# The badge is the one item type that is common between all three Elves
# in each group. Find the item type that corresponds to the badges of
# each three-Elf group. What is the sum of the priorities of those item types?


p1 = {k: v for k, v in zip('abcdefghijklmnopqrstuvwxyz', [*range(1, 27)])}
p2 = {k: v for k, v in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', [*range(27, 53)])}
p = p1 | p2

with open("a.txt", "r") as f:
    lines = f.read().splitlines()

res = 0

# Get next 3 lines and add the common item priority to result.
i = 0

while i < len(lines) - 2:
    L1 = lines[i]
    L2 = lines[i+1]
    L3 = lines[i+2]
    item = next(c for c in L1 if c in L2 if c in L3)
    res += p[item]
    i += 3

print(res)
