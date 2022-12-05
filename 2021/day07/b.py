from collections import Counter

with open("in.txt", "r") as f:
    arr = [int(c) for c in f.readline().rstrip().split(',')]

# create counter of arr
d = Counter(arr)

i = 0
while True:
    # calc cost at i position and compare to cost of next position
    # part B: cost increases by 1 for each step toward position
    # sum of series is n(n+1)/2
    cost_i, cost_right = 0, 0
    for k, v in d.items():
        n = abs(k - i)
        n1 = abs(k - (i + 1))
        cost_i += n*(n+1)//2 * v
        cost_right += n1*(n1+1)//2 * v
    # if position to the right is lower cost, keep going
    print(i, cost_i, cost_right)
    if cost_right < cost_i:
        i += 1
    else:  # we're done
        print(cost_i)
        break
