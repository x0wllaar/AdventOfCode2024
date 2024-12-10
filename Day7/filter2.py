import sys

def run_operations(numbers, op_num, n_bits):
    res = numbers[0]
    numbers = numbers[1:]
    for i in range(n_bits):
        c_op = op_num % 3
        op_num //= 3
        if c_op == 0:
            res += numbers[i]
        elif c_op == 1:
            res *= numbers[i]
        else:
            res = int(str(res) + str(numbers[i]))
    return res

def check_line(line):
    line = line.strip()
    res, numbers = line.split(':')
    numbers = numbers.strip()
    numbers = numbers.split(' ')
    numbers = [int(x) for x in numbers]
    res = int(res)
    
    n_bits = len(numbers) - 1
    max_val = 3**n_bits
    for i in range(max_val):
        c_res = run_operations(numbers, i, n_bits)
        if c_res == res:
            return True
        
while (line := sys.stdin.readline().strip()):
    line = line.strip()
    if check_line(line):
        print(line)