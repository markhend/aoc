import re

# open in.txt and read in all the lines and create a list of lists
# for each line split on any non alphanumeric character
with open('/home/mhenders/aoc/2020/day02/in.txt', 'r') as file:
    inp = [re.split(r'\W+', line.strip()) for line in file]

res = 0

for lst in inp:
    min_count = int(lst[0])
    max_count = int(lst[1])
    char = lst[2]
    password = lst[3]

    if min_count <= password.count(char) <= max_count:
        res += 1

print(res)

res = 0
for lst in inp:
    min_count = int(lst[0])
    max_count = int(lst[1])
    char = lst[2]
    password = lst[3]
    cnt = 0

    if password[min_count-1] == char:
        cnt += 1
    if password[max_count-1] == char:
        cnt += 1
    if cnt == 1:
        res += 1
    # print(lst, cnt)
print(res)
