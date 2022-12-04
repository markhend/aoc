with open("a.txt", "r") as f:
    lines = f.read().splitlines()

curr = 0
res = set()

for line in lines:
    if line == '':
        res.add(curr)
        curr = 0
        continue
    curr += int(line)

print(sum(sorted(res, reverse=True)[:3]))
