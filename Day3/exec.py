import sys

state = True
s = 0
while (line := sys.stdin.readline().strip()):
    if line == "do()":
        state = True
        continue
    if line == "don't()":
        state = False
        continue
    if state:
        line = line.removeprefix('mul(')
        line = line.removesuffix(')')
        n1, n2 = line.split(',')
        n1 = int(n1.strip())
        n2 = int(n2.strip())
        s += n1 * n2
print(s)