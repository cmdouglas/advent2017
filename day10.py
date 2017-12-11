from functools import reduce
from operator import xor


def knot(nums, pos, length, skip_size):
    if length > len(nums):
        raise Exception('invalid length')
    
    span_to_end = min(len(nums) - pos, length)
    span_from_start = length - span_to_end if length > span_to_end else 0
    to_reverse = nums[pos:pos+span_to_end] + nums[:span_from_start]
    new_nums = list(reversed(to_reverse))
    
    
    for i, num in enumerate(new_nums):
        nums[(pos + i) % len(nums)] = num
    
    pos = (pos + length + skip_size) % len(nums)
    skip_size += 1
    
    return nums, pos, skip_size
    
def densify(nums):
    dense = []
    for i in range(16):
        j = i * 16
        dense.append(reduce(xor, nums[j:j + 16]))
    
    return dense
    
def hexify(num):
    s = hex(num)[2:]
    if len(s) == 1:
        s = '0' + s
    return s
    
            
    
def knot_hash(string):
    nums = list(range(256))
    lengths = [ord(c) for c in string]
    lengths += [17, 31, 73, 47, 23]
    pos = 0
    skip_length = 0
    
    for _ in range(64):
        for length in lengths:
            nums, pos, skip_length = knot(nums, pos, length, skip_length)
            
            
    dense_hash = densify(nums)
    return ''.join([hexify(num) for num in dense_hash])
    
    
    
def test():
    nums = list(range(5))
    lengths = [3, 4, 1, 5]
    pos = 0
    skip_size = 0
    
    for length in lengths:
        print(f'knotting nums: {nums} with length: {length}, pos: {pos}, skip_size: {skip_size}')
        nums, pos, skip_size = knot(nums, pos, length, skip_size)
        print(f'result: nums: {nums}, pos: {pos}, skip_size: {skip_size}')
    
def part1():
    with open('input/10.txt') as f:
        nums = list(range(256))
        lengths = [int(length) for length in f.read().strip().split(',')]
        
        pos = 0
        skip_size = 0
        
        for length in lengths:
            nums, pos, skip_size = knot(nums, pos, length, skip_size)
        
        print(nums[0] * nums[1])
        
def part2():
    with open('input/10.txt') as f:
        print(knot_hash(f.read().strip()))

if __name__ == '__main__':
    #test()
    part1()
    part2()
    