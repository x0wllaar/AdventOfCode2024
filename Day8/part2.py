import sys
from itertools import product
import math

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

def scalar_vec_mul(v, s):
    return (s * v[0], s * v[1])

def vec_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def normalize(v):
    g = math.gcd(v[0], v[1])
    return (v[0] // g, v[1] // g)

anp = set()
for c, ps in antennae.items():
    for a, b in product(ps, repeat=2):
        if a == b:
            continue
        
        vec = (b[0] - a[0], b[1] - a[1])
        vec = normalize(vec)
        
        mult = 1
        while True:
            n = vec_add(a, scalar_vec_mul(vec, mult))
            if not point_in_bounds(n):
                break
            anp.add(n)
            mult += 1
        

test_matrix = [["."] * size_x for _ in range(size_y)]
for c, ps in antennae.items():
    for x, y in ps:
        test_matrix[y][x] = c
for x, y in anp:
    test_matrix[y][x] = "#"
#for l in test_matrix:
#    print(''.join(l))
print(len(anp))