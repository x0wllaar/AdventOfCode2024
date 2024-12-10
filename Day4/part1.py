import sys

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def line2str(line):
    return ''.join([c for c, _, _ in line])

all_syms = []
line_n = 0
while (line := sys.stdin.readline().strip()):
    line = line.strip()
    line_syms = tuple((c, line_n, x) for c,x in zip(list(line), range(len(line))))
    all_syms.append(line_syms)
    line_n += 1

all_lines = []

#Add all horizontal lines
for l in all_syms:
    all_lines.append(l)
    
#Add all vertical lines
for i in range(len(all_syms[0])):
    v_l = tuple([l[i] for l in all_syms])
    all_lines.append(v_l)
    
for start_i in range(len(all_syms)):
    for start_j in range(len(all_syms[0])):
        line = []
        i = start_i
        j = start_j
        while i < len(all_syms) and j < len(all_syms[0]):
            line.append(all_syms[i][j])
            i += 1
            j += 1
        all_lines.append(tuple(line))
        
for start_i in range(len(all_syms)):
    for start_j in range(len(all_syms[0])):
        line = []
        i = start_i
        j = start_j
        while i > -1 and j < len(all_syms[0]):
            line.append(all_syms[i][j])
            i -= 1
            j += 1
        all_lines.append(tuple(line))


N = len(all_syms)
M = len(all_syms[0])
test_matrix = [["."] * M for _ in range(N)]

global_all_occ = set()
for l in all_lines:
    line_str = line2str(l)
    all_occ = list(find_all(line_str, "XMAS")) + list(find_all(line_str, "SAMX"))
    for occ in all_occ:
        global_all_occ.add(tuple(l[occ:occ+4]))

for occ in global_all_occ:
    for c, x, y in occ:
        test_matrix[x][y] = c
            
print(len(global_all_occ))
