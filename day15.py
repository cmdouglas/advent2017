
A_FACTOR = 16807
B_FACTOR = 48271

A_START = 618
B_START = 814
    
def judge(a, b):
    return (a & 0xFFFF) == (b & 0xFFFF)

def gen(start, factor, filter_=1):
    value = start
    while True:
        value = (value * factor) % 2147483647
        if value % filter_ == 0:
            yield value
    
def part1():
    total = 0
    ga = gen(A_START, A_FACTOR)
    gb = gen(B_START, B_FACTOR)
    for _ in range(40_000_000):
        a = next(ga)
        b = next(gb)
        
        if judge(a, b):
            total += 1
    
    print(total)
    
def part2():
    total = 0
    ga = gen(A_START, A_FACTOR, 4)
    gb = gen(B_START, B_FACTOR, 8)
    for _ in range(5_000_000):
        a = next(ga)
        b = next(gb)
        
        if judge(a, b):
            total += 1
    
    print(total)
    
if __name__ == '__main__':
    part1()
    part2()
