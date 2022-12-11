with open("in.txt", "r") as f:
    program = [line.strip().split() for line in f.readlines()]
    # print(program)


# cycles = [cycle, instruction, operand, X register, signal strength]
cycles = []

# noop takes one cycle to complete. It has no other effect.
# addx V takes two cycles to complete. After two cycles, the X register
# is increased by the value V. (V can be negative.)
# signal strength = cycle * X

# Part Two:
# X register sets the horizontal position of the middle of a 3px sprite.
# CRT is 40px x 6px. Draws left to right, top to bottom. Positions 0-39.
# CRT draws single pixel during each cycle.
# If the sprite is positioned such that one of its three pixels is the
# pixel currently being drawn, the screen produces a lit pixel (#);
# otherwise, the screen leaves the pixel dark (.).


def draw(cycle, X):
    pos = (cycle - 1) % 40  # draw position
    if abs(pos - X) <= 1:
        print('#', end='')
    else:
        print(' ', end='')
    if cycle % 40 == 0:
        print()
    return


cycle, ins, V, X = 0, None, None, 1

for p in program:
    if len(p) == 1:
        ins = 'noop'
        V = None
        cycle += 1
        draw(cycle, X)
        cycles.append((cycle, ins, V, X, cycle*X))

    else:  # addx operand
        ins, V = p[0], int(p[1])
        # first cycle
        cycle += 1
        draw(cycle, X)
        cycles.append((cycle, ins, V, X, cycle*X))

        # second cycle
        cycle += 1
        draw(cycle, X)
        cycles.append((cycle, ins, V, X, cycle*X))
        X += V

ans = 0
for line in cycles:
    # print(line)
    if (line[0]-20) % 40 == 0:
        ans += line[-1]
        # print(line)
print(ans)
