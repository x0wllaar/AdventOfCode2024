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
            if upd.index(rule[0]) > upd.index(rule[1]):
                return False
    return True

s = 0
for upd in updates:
    if check_update(upd):
        s += upd[len(upd) // 2]
print(s)