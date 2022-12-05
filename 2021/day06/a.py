with open("a.txt", "r") as f:
    today = [*map(int, f.readline().split(','))]

# Each day each fish gets 1 day younger unless it's 0
# which resets to 6 and adds 8 to end of list

days = 80
for _ in range(days):
    tomorrow = []
    spawn = 0
    for n in today:
        if n > 0:
            tomorrow.append(n - 1)
        else:  # n is 0
            spawn += 1
            tomorrow.append(6)
    tomorrow += [8] * spawn
    today = tomorrow

# print(today)
print(len(today))
