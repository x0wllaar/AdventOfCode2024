import sys

obstacles = set()
guard_pos = None

y = 0
while (line := sys.stdin.readline().strip()):
    for x, c in enumerate(line):
        if c == '#':
            obstacles.add((x, y))
        if c == '^':
            guard_pos = (x, y)
    y += 1

size_x = x + 1
size_y = y

def move(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def is_at_obstacle(pos, direction):
    return move(pos, direction) in obstacles

def turn_right(direction):
    if direction == (0, -1):
        return (1, 0)
    if direction == (1, 0):
        return (0, 1)
    if direction == (0, 1):
        return (-1, 0)
    if direction == (-1, 0):
        return (0, -1)

def is_in_bounds(pos):
    return 0 <= pos[0] < (size_x) and 0 <= pos[1] < (size_y) 
    
direction = (0, -1)
positions = set()
positions.add(guard_pos)

while True:
    while is_at_obstacle(guard_pos, direction):
        direction = turn_right(direction)
    guard_pos = move(guard_pos, direction)
    if not is_in_bounds(guard_pos):
        break
    positions.add(guard_pos)

test_matrix = [["."] * size_x for _ in range(size_y)]
for x, y in obstacles:
    test_matrix[y][x] = "#"
for x, y in positions:
    test_matrix[y][x] = "X"

#for l in test_matrix:
#    print(''.join(l))
print(len(positions))
