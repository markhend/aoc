with open("a.txt", "r") as f:
    nums = {*map(int, f.read().splitlines())}

# Find the two entries that sum to 2020;
# what do you get if you multiply them together?

for n in nums:
    if (2020 - n) in nums:
        print(n * (2020 - n))
        break

# what is the product of the three entries that sum to 2020?

a, b, c = next((a, b, c) for a in nums
               for b in nums
               for c in nums
               if a + b + c == 2020)
print(a * b * c)
