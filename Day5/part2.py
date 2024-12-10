import sys

rules = set()
updates = []

while (line := sys.stdin.readline()):
    line = line.strip()
    if "|" in line.strip():
        rule_left, rule_right = line.split('|')
        rule_left = int(rule_left.strip())
        rule_right = int(rule_right.strip())
        rules.add((rule_left, rule_right))
        continue
    
    if len(line) == 0:
        continue
    
    c_upd = tuple([int(x.strip()) for x in line.split(',')])
    updates.append(c_upd)

def check_update(upd):
    all_pages = frozenset(upd)
    for rule in rules:
        if rule[0] in all_pages and rule[1] in all_pages:
            i1 = upd.index(rule[0])
            i2 = upd.index(rule[1])
            if i1 > i2:
                return False, i1, i2
    return True, None, None

def fix_update(upd):
    upd = list(upd[:])
    while True:
        r, i1, i2 = check_update(upd)
        if r:
            break
        upd[i1], upd[i2] = upd[i2], upd[i1]
    return tuple(upd)

s = 0
for upd in updates:
    r, _, _ = check_update(upd)
    if not r:
        u = fix_update(upd)
        #print(u)
        s += u[len(u) // 2]
print(s)