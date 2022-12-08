with open("in.txt", "r") as f:
    f = [l.strip() for l in f.readlines()]


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = set()

    def get_size(self):
        res = sum(f.size for f in self.files)
        for dir in self.dirs:
            res += dir.get_size()
        return res


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


root = Dir("root", None)
curr = root

for line in f[1:]:  # skip first line: $ cd /
    # print(f"{line=}")

    if line[:7] == '$ cd ..':  # $ cd ..
        curr = curr.parent

    elif line == '$ ls':  # $ ls
        continue

    elif line[:3] == 'dir':  # dir dir_name
        continue

    elif line[:4] == '$ cd':  # $ cd dir_name
        _, _, dir_name = line.split()
        if not any(dir.name == dir_name for dir in curr.dirs):
            tmp = Dir(dir_name, curr)
            curr.dirs.append(tmp)
            curr = tmp
        else:  # change curr to existing directory
            for dir in curr.dirs:
                if dir.name == dir_name:
                    curr = dir

    else:  # file_size file_name
        size, name = line.split()
        name = name.replace('.', 'dot')
        size = int(size)
        if not any(file.name == name for file in curr.files):
            curr.files.add(File(name, size))


# find all of the directories with a total size of at most 100000,
# then calculate the sum of their total sizes
print("finding dirs under 100k...")

res = []

def get_size_under100k(self):
    for dir in self.dirs:
        tmp = dir.get_size()
        # print("in dir", dir.name, "size is", tmp)
        if tmp <= 100000:
            # print(dir.name, tmp)
            res.append(tmp)
        get_size_under100k(dir)


get_size_under100k(root)
print(res)
print(f"{sum(res)=}")  # 1908462
print()

# Part B:
# Total system disk space = 70000000
# Needed to run update = 30000000
# Find the smallest directory that, if deleted, would free up enough 
# space on the filesystem to run the update. What is the total size of 
# that directory?

root_size = root.get_size()
print(f"{root_size=}")
# for file in root.files:
#     print(file.name)
space_free = 70000000 - root_size
space_needed = 30000000 - space_free
print(f"{space_needed=}")
res = []

def find_dir_to_free(self):
    for dir in self.dirs:
        tmp = dir.get_size()
        # print(tmp, dir.name)
        if tmp >= space_needed:
            res.append((tmp, dir.name))
        find_dir_to_free(dir)


find_dir_to_free(root)
print(res)
print(f"{min(res)=}")
