import sys
from itertools import product

antennae = {}

y = 0
while (line := sys.stdin.readline().strip()):
    for x, c in enumerate(line):
        if c == '.':
            continue
        antennae[c] = frozenset(antennae.get(c, set()) | {(x, y)})
    y += 1
size_x = x + 1
size_y = y

def point_in_bounds(p):
    return 0 <= p[0] < size_x and 0 <= p[1] < size_y

anp = set()
for c, ps in antennae.items():
    for a, b in product(ps, repeat=2):
        if a == b:
            continue
        vec = (b[0] - a[0], b[1] - a[1])
        pp = (b[0] + vec[0], b[1] + vec[1])
        if point_in_bounds(pp):
            anp.add(pp)
        

test_matrix = [["."] * size_x for _ in range(size_y)]
for c, ps in antennae.items():
    for x, y in ps:
        test_matrix[y][x] = c
for x, y in anp:
    test_matrix[y][x] = "#"
#for l in test_matrix:
#    print(''.join(l))
print(len(anp))