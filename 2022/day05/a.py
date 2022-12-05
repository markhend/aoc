from copy import deepcopy

lines = open("input.txt", "r").readlines()
stacks = [[] for _ in range(9)]

# initialize stacks
for row in range(7, -1, -1):
    for i, col in enumerate(range(1, 34, 4)):
        c = lines[row][col]
        if c != ' ':
            stacks[i].append(c)

start_stacks = deepcopy(stacks)


# move 2 from 4 to 6

def move(cnt, src, dest):
    for _ in range(cnt):
        item = stacks[src-1].pop()
        stacks[dest-1].append(item)


for line in lines[10:]:
    w = line.split()
    cnt, src, dest = int(w[1]), int(w[3]), int(w[5])
    move(cnt, src, dest)

print(''.join(stack[-1] for stack in stacks))


# Part B - moves are in groups instead of one at a time
stacks = deepcopy(start_stacks)


def move_block(cnt, src, dest):
    block = []
    for _ in range(cnt):
        block = [stacks[src-1].pop()] + block
    stacks[dest-1].extend(block)


for line in lines[10:]:
    w = line.split()
    cnt, src, dest = int(w[1]), int(w[3]), int(w[5])
    move_block(cnt, src, dest)

print(''.join(stack[-1] for stack in stacks))
