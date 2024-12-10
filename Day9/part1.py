import sys


line = sys.stdin.readline().strip()
line = [int(x) for x in line]

def print_blocks(blocks):
    for block in blocks:
        if block is None:
            print('.', end='')
        else:
            print(block, end='')
    print()

def find_next_free_block(blocks, ptr):
    for i in range(ptr, len(blocks)):
        if blocks[i] is None:
            return i

def find_last_file_block(blocks, ptr):
    for i in range(ptr, -1, -1):
        if blocks[i] is not None:
            return i

blocks = []
is_file = True
cur_id = 0
for size in line:
    if is_file:
        blocks.extend(([cur_id]*size)[:])
        cur_id += 1
        is_file = False
    else:
        blocks.extend(([None]*size)[:])
        is_file = True

file_ptr = len(blocks) - 1
free_ptr = 0
#print_blocks(blocks)
while True:
    nfrp = find_next_free_block(blocks, free_ptr)
    nflp = find_last_file_block(blocks, file_ptr)
    if nflp == nfrp - 1:
        break
    blocks[nfrp], blocks[nflp] = blocks[nflp], blocks[nfrp]
    #print_blocks(blocks)

chksm = 0
for bid, fid in enumerate(blocks):
    if fid is not None:
        chksm += bid * fid
print(chksm)