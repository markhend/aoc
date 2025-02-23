import math

with open('/home/mhenders/aoc/2020/day03/in.txt', 'r') as f:
    inp = [list(line.strip()) for line in f]
# print(inp)

res = 0
pos = 0
m = len(inp)
n = len(inp[0])


def trees(right, down):
    pos = res = 0
    start_line = 1 if down == 1 else 2
    for line in inp[start_line::down]:
        pos = (pos + right) % n
        if line[pos] == '#':
            res += 1
    return res


# part 1
print(math.prod(trees(a, b) for (a, b) in [(3, 1)]))

# part 2
print(math.prod(trees(a, b)
      for (a, b) in [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]))
