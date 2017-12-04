def advent_input(day):
    filename = f"input/{day}.txt"
    return open(filename)
    
def first(iterable): 
    return next(iter(iterable))
    
def neighbors8(p):
    x, y = p
    return [(x + 1, y), (x+1, y+1), (x, y+1), (x-1, y+1), 
            (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1)
    ]