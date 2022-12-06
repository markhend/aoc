with open("test.txt", "r") as f:
    t = ['9'+line.strip()+'9' for line in f.readlines()]
# add a border of 9s so we can check all values the same way
s = '9'*len(t[0])
t.insert(0, s)
t.append(s)
# print(t)

res = 0
lows = set()  # of (i, j)
# check each location in table t (excluding border) to find low points
for i in range(1, len(t) - 1):
    for j in range(1, len(s) - 1):
        if t[i][j] < min(t[i-1][j], t[i][j-1], t[i+1][j], t[i][j+1]):
            lows.add((i, j))
            res += int(t[i][j]) + 1

print(res)
print(len(lows))

# A basin is all locations that eventually flow downward to a single 
# low point. Therefore, every low point has a basin, although some basins 
# are very small. Locations of height 9 do not count as being in any basin, 
# and all other locations will always be part of exactly one basin.
# What do you get if you multiply together the sizes of the three largest basins?

