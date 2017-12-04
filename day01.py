from util import advent_input

def sum_of_matching_pairs(nums):
    last = nums[-1]
    total = 0
    for num in nums:
        if num == last:
            total += num
        last = num
    
    return total
    
def sum_of_matching_opposite_pairs(nums):
    def opposite(i):
        return int((i + (len(nums))/2) % (len(nums)))
        
    total = 0
    for i, num in enumerate(nums):
        o = opposite(i)
        if num == nums[o]:
            total += num
    
    return total
    
def part1():
    with advent_input(1) as f:
        nums = [int(n) for n in f.read().strip()]
        print("part 1:", sum_of_matching_pairs(nums))

def part2():
    with advent_input(1) as f:
        nums = [int(n) for n in f.read().strip()]
        print("part 2:", sum_of_matching_opposite_pairs(nums))

if __name__ == '__main__':
    part1()
    part2()
        