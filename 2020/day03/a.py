with open('/home/mhenders/aoc/2020/day03/in.txt', 'r') as f:
    inp = [list(line.strip()) for line in f]
print(inp)

res = 0
pos = 0
width = len(inp[0])

for line in inp[1:]:
    pos = (pos + 3) % width
    if line[pos] == '#':
        res += 1
print(res)
