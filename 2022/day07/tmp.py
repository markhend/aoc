a = 1
L = []
try:
    print(a in L)
except:
    print("no a")

class A:
    def __init__(self, val):
        self.val = val

c1 = A(1)
c2 = A(2)
cs = set()
cs.add(c1)
cs.add(c2)
print(cs)
cs.add(c1)
print(cs)

L.append(c1)
print(c1 in L)


