from util import neighbors4
from day10 import knot_hash

def generate_grid(s):
    grid = []
    for i in range(128):
        h = knot_hash(s + '-' + str(i))
        row = list(''.join(['{0:04b}'.format(int(c, 16)) for c in h]))
        grid.append(row)
    return grid
    
def value_at(grid, point):
    x, y = point
    
    if x < 0 or x > 127 or y < 0 or y > 127:
        return '0'
    
    return grid[y][x]
    
def fill_region(p, grid, region):
    if value_at(grid, p) == '1' and p not in region:
        region.add(p)
        for p2 in neighbors4(p):
            fill_region(p2, grid, region)
    
def part1():
    hash_input = 'ffayrhll'
    grid = generate_grid(hash_input)
    print(sum([len([c for c in row if c == '1']) for row in grid]))
    
def part2():
    hash_input = 'ffayrhll'
    grid = generate_grid(hash_input)
    regions = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            point = (x, y)
            if cell == '1' and not any(point in region for region in regions):
                new_region = set()
                fill_region(point, grid, new_region)
                regions.append(new_region)
    
    print(len(regions))

if __name__ == '__main__':
    part1()
    part2()
