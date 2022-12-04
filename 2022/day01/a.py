with open("a.txt", "r") as f:
    lines = f.read().splitlines()

hi = curr = 0

for line in lines:
    if line == '':
        hi = max(hi, curr)
        curr = 0
        continue
    curr += int(line)

print(hi)
