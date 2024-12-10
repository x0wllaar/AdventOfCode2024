import sys

def sgn(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    return 0

def check_single_line(nums):
    diff = None
    for i in range(1, len(nums)):
        if diff is None:
            diff = nums[i] - nums[i - 1]
        else:
            new_diff = nums[i] - nums[i - 1]
            if sgn(new_diff) != sgn(diff):
                return False
            diff = new_diff
        if abs(diff) > 3:
            return False
        if abs(diff) < 1:
            return False
    return True

def check_line(line):
    nums = [int(x) for x in line.strip().split(' ')]
    if check_single_line(nums):
        return True
    for i in range(len(nums)):
        new_line = nums[:]
        new_line.pop(i)
        if check_single_line(new_line):
            return True
    return False

while (line := sys.stdin.readline().strip()):
    line = line.strip()
    if check_line(line):
        print(line)