# These are passport keys. A valid passport must have all keys.
# cid is optional.

keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

with open("input.txt", 'r') as f:
    not_seen = keys.copy()
    cnt = 0  # num valid
    for line in f:
        line = line.strip()
        if len(line) == 0:  # blank line
            if len(not_seen) == 0:
                cnt += 1
            not_seen = keys.copy()
        else:
            for kv in line.split():
                not_seen.discard(kv[:3])

    print(cnt)
