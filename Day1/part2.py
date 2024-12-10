import sys
from collections import Counter

l1 = []
l2 = []
while (line := sys.stdin.readline().strip()):
    line = line.strip()
    n1, n2 = line.split('   ')
    n1 = int(n1.strip())
    n2 = int(n2.strip())
    l1.append(n1)
    l2.append(n2)

l1 = list(sorted(l1))
l2 = list(sorted(l2))

l2_ctr = dict(Counter(l2))

s = 0
for n in l1:
    rs = l2_ctr.get(n, 0)
    s += n * rs
print(s)