from util import advent_input

def count_jumps(nums):
    pos = 0
    jumps = 0
    while -1 < pos < len(nums):
        oldpos = pos
        pos += nums[pos]
        nums[oldpos] += 1
        jumps += 1
    
    return jumps
    
def count_jumps2(nums):
    pos = 0
    jumps = 0
    while -1 < pos < len(nums):
        oldpos = pos
        offset = nums[pos]
        pos += offset
        if offset >= 3:
            nums[oldpos] -= 1
        else:
            nums[oldpos] += 1
        jumps += 1
    
    return jumps
    
def part1():
    with advent_input(5) as f:
        nums = [int(line) for line in f]
        print(count_jumps(nums))

def part2():
    with advent_input(5) as f:
        nums = [int(line) for line in f]
        print(count_jumps2(nums))

if __name__ == '__main__':
    part1()
    part2()
        