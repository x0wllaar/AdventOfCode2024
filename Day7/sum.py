import sys

c_s = 0
while (line := sys.stdin.readline().strip()):
    line = line.strip()
    res, _ = line.split(':')
    res = int(res)
    c_s += res
print(c_s)