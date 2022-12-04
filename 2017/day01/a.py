with open("a.txt", "r") as f:
    xs = [int(x) for x in f.readline()]


# Find the sum of all digits that match the next digit in the list.
# The list is circular.
res = 0
for a, b in zip(xs[:-1], xs[1:]):
    if a == b:
        res += a
if xs[-1] == xs[0]:
    res += xs[0]
print(res)


# Only include a digit in your sum if the digit halfway round
# (e.g. 10/2 = 5 steps forward) matches it. len(list) is even.
res = 0
n = len(xs)
for i in range(n):
    if xs[i] == xs[(i + n//2) % n]:
        res += xs[i]
print(res)
