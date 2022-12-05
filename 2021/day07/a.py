from collections import Counter

with open("in.txt", "r") as f:
    arr = [int(c) for c in f.readline().rstrip().split(',')]

# create counter of arr
d = Counter(arr)

i = 0
while True:
    # calc cost at i position and compare to cost of next position
    cost_i, cost_right = 0, 0
    for k, v in d.items():
        cost_i += abs(k - i) * v
        cost_right += abs(k - (i + 1)) * v
    # if position to the right is lower cost, keep going
    print(i, cost_i, cost_right)
    if cost_right < cost_i:
        i += 1
    else:  # we're done
        print(cost_i)
        break
