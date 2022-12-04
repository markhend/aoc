# Each rucksack has two large compartments. All items of a 
# given type are meant to go into exactly one of the two compartments

# A given rucksack always has the same number of items in each of 
# its two compartments

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# Find the item type that appears in both compartments of each rucksack. 
# What is the sum of the priorities of those item types?


p1 = {k:v for k,v in zip('abcdefghijklmnopqrstuvwxyz', [*range(1, 27)])}
p2 = {k:v for k,v in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', [*range(27, 53)])}
p = p1 | p2

with open("a.txt", "r") as f:
    lines = f.read().splitlines()

res = 0

for L in lines:
    L1 = L[:len(L)//2]
    L2 = L[len(L)//2:]
    item = next(c for c in L1 if c in L2)
    res += p[item]

print(res)


