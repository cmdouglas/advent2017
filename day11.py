from util import a_star
import math

DIRS = {
    'n': (0, 2),
    'ne': (1, 1),
    'se': (1, -1),
    's': (0, -2),
    'sw': (-1, -1),
    'nw': (-1, 1)
}

def follow_path(path):
    x, y = (0, 0)
    for direction in path:
        dx, dy = DIRS[direction]
        x += dx
        y += dy
    
    return x, y
    
def furthest_from_origin(path):
    x, y = (0, 0)
    furthest_distance = 0
    furthest_point = (0, 0)
    for direction in path:
        dx, dy = DIRS[direction]
        x += dx
        y += dy
        distance = abs(x + y)
        if distance >= furthest_distance:
            furthest_distance = distance
            furthest_point = (x, y)
            
    return furthest_point
    
def moves(p):
    x, y = p
    return [(x + dx, y + dy) for dx, dy in DIRS.values()]
    
def part1():
    with open('input/11.txt') as f:
        original_path = f.read().strip().split(',')
        goal = follow_path(original_path)
        print(goal)
        
        def heuristic(p):
            x, y = p
            gx, gy = goal
            return math.hypot((gx - x),(gy - y))
        
        shortest_path = a_star((0, 0), goal, moves, heuristic)
        print(len(shortest_path) - 1) # remove one, becuase path includes the start state
        
def part2():
    with open('input/11.txt') as f:
        original_path = f.read().strip().split(',')
        goal = furthest_from_origin(original_path)
        print(goal)
        
        def heuristic(p):
            x, y = p
            gx, gy = goal
            return math.hypot((gx - x),(gy - y))
        
        shortest_path = a_star((0, 0), goal, moves, heuristic)
        print(len(shortest_path) - 1 ) # remove one, becuase path includes the start state
        
def test():
    def heuristic(p):
        x, y = p
        return math.hypot(2 - x, 2 - y)
    print(a_star((0, 0), (2, 2), moves, heuristic))

if __name__ == '__main__':
    part1()
    part2()
    #test()