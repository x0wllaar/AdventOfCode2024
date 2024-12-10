import sys
from tqdm import tqdm

line = sys.stdin.readline().strip()
line = [int(x) for x in line]

def print_blocks(blocks):
    for block in blocks:
        if block is None:
            print('.', end='')
        else:
            print(block, end='')
    print()

def find_next_free_extent(blocks, ptr):
    start = None
    end = None
    for i in range(ptr, len(blocks)):
        if blocks[i] is None and start is None:
            start = i
        if blocks[i] is None and start is not None:
            end = i
        if blocks[i] is not None and start is not None:
            return start, end
    return -1, -1

def find_last_file_extent(blocks, ptr):
    end = None
    file = None
    for i in range(ptr, -1, -1):
        if blocks[i] is not None and end is None:
            end = i
            file = blocks[i]
        if blocks[i] == file and end is not None:
            start = i
        if blocks[i] != file and end is not None:
            return start, end, file
    return -1, -1, -1

def zrange(len):
    if len == 0:
        return [0]
    return range(len)

blocks = []
is_file = True
cur_id = 0
all_files = set()
for size in line:
    if is_file:
        all_files.add(cur_id)
        blocks.extend(([cur_id]*size)[:])
        cur_id += 1
        is_file = False
    else:
        blocks.extend(([None]*size)[:])
        is_file = True

file_ptr = len(blocks) - 1
free_ptr = 0
#print_blocks(blocks)


done = False
attempted_files = set()
#pbar = tqdm(total=len(all_files))
while not done:
    c_file_ptr = file_ptr
    found = False
    while True:
        nfls, nfle, file = find_last_file_extent(blocks, c_file_ptr)
        file_size = nfle - nfls + 1
        c_file_ptr = nfls - 1
        if file == -1:
            done = True
            break
        if file in attempted_files:
            continue
        attempted_files.add(file)
        #pbar.n = len(attempted_files) + 1
        #pbar.refresh()
        c_free_ptr = 0
        while True:
            nfrs, nfre = find_next_free_extent(blocks, c_free_ptr)
            if nfrs == -1:
                break
            extent_size = nfre - nfrs + 1
            if nfrs > nfls:
                break
            if file_size <= extent_size:
                found = True
                break
            c_free_ptr = nfre + 1
        if found:
            file_ptr = c_file_ptr
            break
    if not done:
        for i in zrange(file_size):
            blocks[nfrs + i], blocks[nfls + i] = blocks[nfls + i], blocks[nfrs + i]
        #print_blocks(blocks)

chksm = 0
for bid, fid in enumerate(blocks):
    if fid is not None:
        chksm += bid * fid
print(chksm)