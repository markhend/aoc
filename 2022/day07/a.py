with open("test.txt", "r") as f:
    f = [l.strip() for l in f.readlines()]


class Dir:
    def __init__(self, name, parent, dirs=[], files=set()):
        self.name = name
        self.parent = parent
        self.dirs = dirs
        self.files = files

    def get_size(self):
        res = sum(f.size for f in self.files)
        for dir in self.dirs:
            print(dir.get_size())
        return res


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


# each dir has a set of sub directory names and list of files which are
# tuples.  [{dirs} [(size, name)]]
# keep track of curr_dir for 'cd ..' command

root = Dir("root", None)
curr = root

for line in f[1:]:  # skip first line: $ cd /
    print(f"{line=}")
    if line == '$ cd ..':  # $ cd ..
        curr = curr.parent

    elif line[:3] == 'dir':  # dir dir_name
        _, dir_name = line.split()
        if not any(dir.name == dir_name for dir in curr.dirs):
            curr.dirs.append(Dir(dir_name, curr))
            print(f"{curr.dirs}")

    elif line[:4] == '$ cd':  # $ cd dir_name
        _, _, dir_name = line.split()
        # we can assume dir exists
        for dir in curr.dirs:
            if dir.name == dir_name:
                curr = dir

    elif line == '$ ls':  # $ ls
        continue

    else:  # file_size file_name
        size, name = line.split()
        file = name.replace('.', 'dot')
        size = int(size)
        print(size, name)
        curr.files.add(File(name, size))
        print(f"{curr.files=}")

print(root.get_size())