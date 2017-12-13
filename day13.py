
def position_at_time(t, range_):
    direction = 1 if (t // (range_ - 1)) % 2 == 0 else -1
    offset = t % (range_ - 1)
    if direction == 1:
        return offset
    else:
        return (range_ - 1) - offset
    
def parse(lines):
    scanners = {}
    for line in lines:
        depth, range_ = [int(i) for i in line.split(': ')]
        scanners[depth] = range_
    
    return scanners
    
def severity(layers, start_time=0):
    total = 0
    for depth, range_ in layers.items():
        if position_at_time(depth + start_time, range_) == 0:
            total += depth * range_
    
    return total
    
def hit(layers, start_time=0):
    for depth, range_ in layers.items():
        if position_at_time(depth + start_time, range_) == 0:
            return True
    return False

def part1():
    with open('input/13.txt') as f:
        layers = parse(f)
        print(severity(layers))
        
def part2():
    with open('input/13.txt') as f:
        layers = parse(f)
        start_time = 0
        while(True):
            if not hit(layers, start_time):
                break;
            start_time += 1
        
        print(start_time)    
        
if __name__ == '__main__':
    part1()
    part2()
        
        
        
                