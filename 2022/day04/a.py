with open("a.txt", "r") as f:
    lines = f.read().splitlines()


# Part A: In how many assignment pairs does one range fully contain the other?
contains = 0

# Part B: In how many assignment pairs do the ranges overlap?
overlaps = 0

for line in lines:
    # split on comma to get assignment pairs
    a, b = line.split(',')
    # split on dash to get start and end of ranges
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))

    if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
        contains += 1

    if (a1 <= b1 and b1 <= a2) or (b1 <= a1 and a1 <= b2):
        overlaps += 1


print("contains", contains)
print("overlaps", overlaps)
