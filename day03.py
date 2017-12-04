import math

from util import neighbors8

def spiral():
    x = 0
    y = 0
    val = 1
    ring = 1
    prevring = 0

    while True:
        side_length = int(math.sqrt(prevring)) + 1
        yield x, y, val        
        
        val += 1
        
        # we've reached the end of our current ring, start a new ring
        if val - 1 == ring:
            prevring, ring = ring, int(math.sqrt(ring) + 2)**2
            x += 1
            
        elif prevring < val <= prevring + side_length:
            y += 1
            
        elif prevring + side_length < val <= prevring + side_length * 2:
            x -= 1
            
        elif prevring + side_length * 2 < val <= prevring + side_length * 3:
            y -= 1
            
        else:
            x += 1
            
def spiral2():
    x = 0
    y = 0
    values = {(0, 0): 1}
    pos = 1
    ring = 1
    prevring = 0

    while True:
        side_length = int(math.sqrt(prevring)) + 1
        yield x, y, values[(x, y)]        
        
        pos += 1
        
        # we've reached the end of our current ring, start a new ring
        if pos - 1 == ring:
            prevring, ring = ring, int(math.sqrt(ring) + 2)**2
            x += 1
            
        elif prevring < pos <= prevring + side_length:
            y += 1
            
        elif prevring + side_length < pos <= prevring + side_length * 2:
            x -= 1
            
        elif prevring + side_length * 2 < pos <= prevring + side_length * 3:
            y -= 1
            
        else:
            x += 1
            
        values[(x, y)] = sum(values.get((x_, y_), 0) for x_, y_, in neighbors8((x, y)))
            
def part1():
    s = spiral()
    x, y, v = next(s)
    
    while v < 368078:
        x, y, v = next(s)
    
    return abs(x) + abs(y)
    
def part2():
    s = spiral2()
    x, y, v = next(s)
    
    while v < 368078:
        x, y, v = next(s)
        
    return v
    
if __name__ == '__main__':
    print(part1())
    print(part2())
    
        
