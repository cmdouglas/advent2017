def redistribute(bins):
    largest = max(bins)
    index = bins.index(largest)
    bins[index] = 0
    for i in range(1, largest + 1):
        bins[(index + i) % len(bins)] += 1
    
    return bins
    
def find_cycle(bins):
    seen = set()
    seen.add(tuple(bins))
    num = 0
    
    while True:
        bins = redistribute(bins)
        num += 1
        if tuple(bins) in seen:
            return num
        else:
            seen.add(tuple(bins))
            
def find_cycle_length(bins):
    find_cycle(bins)
    return find_cycle(bins)
            
def part1():
    with open('input/6.txt') as f:
        bins = [int(n) for n in f.read().split('\t')]
        print(find_cycle(bins))

def part2():
    with open('input/6.txt') as f:
        bins = [int(n) for n in f.read().split('\t')]
        print(find_cycle_length(bins))
        
if __name__ == '__main__':
    part1()
    part2()
    