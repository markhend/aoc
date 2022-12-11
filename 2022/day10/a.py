with open("in.txt", "r") as f:
    program = [line.strip().split() for line in f.readlines()]
    # print(program)


# res = [cycle, instruction, operand, X register, signal strength]
res = []

# noop takes one cycle to complete. It has no other effect.
# addx V takes two cycles to complete. After two cycles, the X register
# is increased by the value V. (V can be negative.)
# signal strength = cycle * X

cycle, ins, V, X = 0, None, None, 1

for p in program:
    if len(p) == 1:
        ins = 'noop'
        V = None
        cycle += 1
        res.append((cycle, ins, V, X, cycle*X))
    else:  # addx operand
        ins, V = p[0], int(p[1])
        # first cycle
        cycle += 1
        res.append((cycle, ins, V, X, cycle*X))

        # second cycle
        cycle += 1
        res.append((cycle, ins, V, X, cycle*X))
        X += V

ans = 0
for line in res:
    # print(line)
    if (line[0]-20) % 40 == 0:
        ans += line[-1]
        print(line)
print(ans)
