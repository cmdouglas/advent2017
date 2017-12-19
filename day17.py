def spin_and_insert(nums, pos, to_insert, steps):
    steps = steps % len(nums)
    new_pos = (steps + pos) % len(nums) 
    
    nums.insert(new_pos + 1, to_insert)

    return nums, new_pos + 1
    
def spin_state(current_pos, length, num_after_0, steps):
    steps = steps % length
    new_pos = (current_pos + steps) % length
    if new_pos == 0:
        num_after_0 = length
    length += 1
    
    return new_pos + 1, length, num_after_0
    
def part1():
    nums = [0]
    pos = 0
    steps = 335
    for i in range(2017):
        nums, pos = spin_and_insert(nums, pos, i + 1, steps)
    
    print(nums[(pos + 1) % len(nums)])
    
def part2():
    pos = 0
    length = 1
    num_after_0 = 0
    steps = 335
    for _ in range(50_000_000):
        pos, length, num_after_0 = spin_state(pos, length, num_after_0, steps)
        
    print(num_after_0)

def test():
    nums = [0]
    pos = 0
    steps = 335
    for i in range(10):
        nums, pos = spin_and_insert(nums, pos, i + 1, steps)
        print(pos, len(nums), nums[1])
        
def test2():
    pos = 0
    length = 1
    num_after_0 = 0
    steps = 335
    for i in range(10):
        pos, length, num_after_0 = spin_state(pos, length, num_after_0, steps)
        print(pos, length, num_after_0)
    
    
if __name__ == '__main__':
    part1()
    part2()