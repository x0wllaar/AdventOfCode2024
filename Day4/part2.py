import sys


all_syms = []
line_n = 0
while (line := sys.stdin.readline().strip()):
    line = line.strip()
    line_syms = tuple((c, line_n, x) for c,x in zip(list(line), range(len(line))))
    all_syms.append(line_syms)
    line_n += 1

def line2str(line):
    return ''.join([c for c, _, _ in line])

def get_stencil_matches(s, i, j):
    diag1 = [s[i][j], s[i+1][j+1], s[i+2][j+2]]
    diag2 = [s[i][j+2], s[i+1][j+1], s[i+2][j]]
    d1s = line2str(diag1)
    d2s = line2str(diag2)
    d1m = d1s == "MAS" or d1s == "SAM"
    d2m = d2s == "MAS" or d2s == "SAM"
    if d1m and d2m:
        return tuple(diag1 + diag2)
    return ()
    
global_all_occ = set()
for i in range(len(all_syms)-2):
    for j in range(len(all_syms[0])-2):
        m = get_stencil_matches(all_syms, i, j)
        if(len(m) > 0):
            global_all_occ.add(m)

N = len(all_syms)
M = len(all_syms[0])
test_matrix = [["."] * M for _ in range(N)]
for occ in global_all_occ:
    for c, x, y in occ:
        test_matrix[x][y] = c
#for l in test_matrix:
#    print(''.join(l))
            
print(len(global_all_occ))
