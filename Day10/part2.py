import sys

all_lines = []
while (line := sys.stdin.readline().strip()):
    line = line.strip()
    line_syms = tuple(int(x) if x != '.' else 999 for x in line)
    all_lines.append(line_syms)
    
size_y = len(all_lines)
size_x = len(all_lines[0])

trailheads = list()
for i in range(size_y):
    for j in range(size_x):
        if all_lines[i][j] == 0:
            trailheads.append((j, i))

def find_neighbors(x, y):
    all_cand_points = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    all_cand_points = [(x, y) for x, y in all_cand_points if x >= 0 and x < size_x and y >= 0 and y < size_y]
    c_height = all_lines[y][x]
    neigh = [(x, y) for x, y in all_cand_points if all_lines[y][x] - c_height == 1]
    return neigh

def find_trails(x, y, c_trail, trails):
    c_trail = (*c_trail, (x, y))
    if all_lines[y][x] == 9:
        trails.append(c_trail)
    for x, y in find_neighbors(x, y):
        find_trails(x, y, c_trail, trails)

s = 0
for x, y in trailheads:
    trails = []
    find_trails(x, y, (), trails)
    trails = set(trails)
    r = len(trails)
    s += r
print(s)