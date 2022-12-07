# start-of-packet marker in the datastream is indicated by a sequence
# of four characters that are all different.
# Report the number of characters from the beginning of the buffer to
# the end of the first such four-character marker.

with open("in.txt", "r") as f:
    s = f.read()

for i in range(3, len(s)):
    if len(set(s[i-3:i+1])) == 4:
        print(s[i-3:i+1])
        print(set(s[i-3:i+1]))
        print(i + 1)
        break

# Part B: first 14 unique chars
for i in range(13, len(s)):
    if len(set(s[i-13:i+1])) == 14:
        print(s[i-13:i+1])
        print(set(s[i-13:i+1]))
        print(i + 1)
        break
