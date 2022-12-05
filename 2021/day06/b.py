from collections import Counter

with open("a.txt", "r") as f:
    xs = [*map(int, f.readline().split(','))]

c = Counter(xs)
# Each n in array is the count of how many fish are at that index in cycle
# e.g. 3,4,3,1,2 => [0, 1, 1, 2, 1, 0, 0, 0, 0]
xs = [c[x] for x in range(9)]
print(xs)

# Each day each fish gets 1 day younger unless it's 0
# which resets to 6 and adds 8 to end of list.
# Largest number in start list is 5.
# 7 day cycle

days = 256
old_zeros = 0
for _ in range(days):
    zeros = xs[0]
    xs[0] = xs[1]
    xs[1] = xs[2]
    xs[2] = xs[3]
    xs[3] = xs[4]
    xs[4] = xs[5]
    xs[5] = xs[6]
    xs[6] = xs[7] + zeros
    xs[7] = xs[8]
    xs[8] = old_zeros
    old_zeros = xs[0]

print(sum(xs))
# with test.txt and 80 days => 5934
# with a.txt and 80 days => 351092
