import sys

l1 = []
l2 = []
while (line := sys.stdin.readline().strip()):
    n1, n2 = line.split('   ')
    n1 = int(n1.strip())
    n2 = int(n2.strip())
    l1.append(n1)
    l2.append(n2)

l1 = list(sorted(l1))
l2 = list(sorted(l2))

r_l = [abs(a - b) for a, b in zip(l1, l2)]
print(sum(r_l))