from collections import Counter

with open("in.txt") as f:
    lines = [line.rstrip().split(' | ') for line in f]

d1, d4, d7, d8 = 0, 0, 0, 0
for line in lines:
    for w in line[1].split():
        match len(w):
            case 2: d1 += 1
            case 4: d4 += 1
            case 3: d7 += 1
            case 7: d8 += 1
print(sum((d1, d4, d7, d8)))


# Part B:
res = 0

for line in lines:
    words = line[0]
    # count letters: 6=>p2, 4=>p5, 9=>p6
    c = Counter(words.replace(' ', ''))
    p2 = [k for k in c if c[k] == 6][0]
    p5 = [k for k in c if c[k] == 4][0]
    p6 = [k for k in c if c[k] == 9][0]
    # p3 is the length 2 word less p6 letter
    p3 = [w for w in line[0].split() if len(w) == 2][0]
    p3 = p3.replace(p6, '')
    # p1 is the length 3 word less p3 and p6 letters
    p1 = [w for w in line[0].split() if len(w) == 3][0]
    p1 = p1.replace(p6, '').replace(p3, '')
    # p4 is in the length 4 word less p2, p3, and p6 letters
    p4 = [w for w in line[0].split() if len(w) == 4][0]
    p4 = p4.replace(p6, '').replace(p3, '').replace(p2, '')
    tmp = set("abcdefg") - set([p1, p2, p3, p4, p5, p6])
    p7 = tmp.pop()

    d = [{p1, p2, p3, p5, p6, p7},
         {p3, p6},
         {p1, p3, p4, p5, p7},
         {p1, p3, p4, p6, p7},
         {p2, p3, p4, p6},
         {p1, p2, p4, p6, p7},
         {p1, p2, p4, p5, p6, p7},
         {p1, p3, p6},
         {p1, p2, p3, p4, p5, p6, p7},
         {p1, p2, p3, p4, p6, p7},
         ]

    # determine the 4 digits of the output values by comparing to table d
    words = line[1].split()
    a = str(d.index(set(words[0])))
    b = str(d.index(set(words[1])))
    c = str(d.index(set(words[2])))
    d = str(d.index(set(words[3])))

    res += (int(a + b + c + d))

print(res)  # in.txt => 1028926
