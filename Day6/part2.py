import sys
from tqdm import tqdm
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
obstacles = frozenset(obstacles)

def move(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def is_at_obstacle(pos, direction, obstacles):
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

def get_sym(direction):
    if direction == (0, -1):
        return "|"
    if direction == (1, 0):
        return "-"
    if direction == (0, 1):
        return "|"
    if direction == (-1, 0):
        return "-"

def is_in_bounds(pos):
    return 0 <= pos[0] < (size_x) and 0 <= pos[1] < (size_y) 

def test_loop(obstacles, guard_pos):
    direction = (0, -1)
    positions = set()
    positions.add((guard_pos, direction))
    turns = set()

    while True:
        while is_at_obstacle(guard_pos, direction, obstacles):
            direction = turn_right(direction)
            turns.add(guard_pos)
        guard_pos = move(guard_pos, direction)
        if not is_in_bounds(guard_pos):
            return False, positions, turns
        if (guard_pos, direction) in positions:
            return True, positions, turns
        positions.add((guard_pos, direction))
    

_, known_positions, _ = test_loop(obstacles, guard_pos)

good_obs = set()
for (x, y), _ in known_positions:
    new_obstacles = frozenset(obstacles | {(x, y)})
    r, positions, turns = test_loop(new_obstacles, guard_pos)
    if r:
        good_obs.add((x, y))
#print(good_obs)


#test_matrix = [["."] * size_x for _ in range(size_y)]
#for x, y in obstacles:
#    test_matrix[y][x] = "#"
#for (x, y), d in positions:
#    test_matrix[y][x] = get_sym(d)
#for x,y in turns:
#    test_matrix[y][x] = "+"
#test_matrix[guard_pos[1]][guard_pos[0]] = "^"

#for l in test_matrix:
#    print(''.join(l))
print(len(good_obs))
