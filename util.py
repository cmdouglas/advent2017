from heapq import heappush, heappop

def advent_input(day):
    filename = f"input/{day}.txt"
    return open(filename)
    
def first(iterable): 
    return next(iter(iterable))
    
def neighbors4(p):
    x, y = p
    return [
        (x+1, y), (x, y+1),
        (x-1, y), (x, y-1)
    ]

def neighbors8(p):
    x, y = p
    return [(x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), 
            (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1)
    ]


def a_star(start, goal, moves_func, h_func):
    frontier = [(h_func(start), start)]
    previous = {start: None}
    path_cost = {start: 0}
    def path_func(state):
        path = []
        while state:
            path.append(state)
            state = previous[state]
        
        return list(reversed(path))
    
    while frontier:
        (cost, state) = heappop(frontier)
        if state == goal:
            return path_func(state)
        
        for new_state in moves_func(state):
            g = path_cost[state] + 1
            if new_state not in path_cost or g < path_cost[new_state]:
                heappush(frontier, (g + h_func(new_state), new_state))
                path_cost[new_state] = g
                previous[new_state] = state
    