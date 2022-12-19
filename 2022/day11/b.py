with open("small_test.txt", "r") as f:
    lines = [line.split() for line in f.readlines()]

monkeys = []
len_monkeys = len([1 for line in lines if line != [] and line[0] == "Monkey"])


# Each monkey will hold 3 items:
# 1. list of vals in its queue, 2. an op fn, 3, a test fn
g = iter(lines)
for i in range(len_monkeys):
    monkey = []

    # skip Monkey line
    next(g)

    # set monkey[0] to list of vals on next line
    line = next(g)
    vals = [int(c.strip(',')) for c in line[2:]]
    monkey.append([int(c) for c in vals])

    # create Operation fn and append to monkey
    line = next(g)
    op, val = line[-2:]
    if val == "old":
        fn = eval(f"lambda x: x ** 2")
    else:
        fn = eval(f"lambda x: x {op} {val}")
    monkey.append(fn)

    # create Test fn and append to monkey
    a, b, c = next(g), next(g), next(g)
    # print(b[-1], a[-1], c[-1])
    fn = eval(f"lambda x: {b[-1]} if x % {a[-1]} == 0 else {c[-1]}")
    monkey.append(fn)

    monkeys.append(monkey)

    # skip blank line
    if i == len_monkeys-1:
        break
    next(g)


# print(monkeys)

# Each monkey has a queue of items (xs)
# Item value is your "worry level".
# Monkey inspects items in order.
# Then value / 3 and rounded down to nearest int.
# Value undergoes operation from old to new.
# Monkey applies test to value.
# T/F result determines where item is thrown.
# Receiver monkey adds item to queue.

# --- Part Two ---
# Worry levels are no longer divided by three after each item 
# is inspected; you'll need to find another way to keep your 
# worry levels manageable. What is the level of monkey business 
# after 10000 rounds?

rounds = 20
cnt = [0]*len_monkeys

# monkeys[0][0] = [1]
# monkeys[1][0] = []
# monkeys[2][0] = []
# monkeys[3][0] = []
# monkeys[4][0] = []
# monkeys[5][0] = []
# monkeys[6][0] = []
# monkeys[7][0] = []

for round in range(rounds):
    for i, monkey in enumerate(monkeys):
        q, op, test = monkey
        while q:
            x = q.pop(0)
            # print("popped", x)
            cnt[i] += 1

            x = op(x)
            # print("after worry op", x)

            # x = x // 3
            # print("bored//3", x)

            receiver = test(x)
            # print("throwing to", receiver)
            monkeys[receiver][0].append(x)
            # print()


# for m in monkeys:
#     print(m[0])
print(rounds, cnt)
# cnt.sort()
# print(cnt[-1] * cnt[-2])
