
def parse_graph(lines):
    graph = {}
    for line in lines:
        if not line: 
            continue
        chunks = line.split()
        n1 = int(chunks[0])
        connections = [int(chunk.strip(',')) for chunk in chunks[2:]]
        graph[n1] = connections
    
    return graph
    
def walk_graph(graph, start):
    frontier = [start]
    visited = set()
    
    while frontier:
        node = frontier.pop()
        visited.add(node)
        for new_node in graph[node]:
            if new_node in visited:
                continue
            frontier.append(new_node)
    return visited
    
def find_all_groups(graph):
    groups = []
    for node in graph:
        if any(node in group for group in groups):
            continue
        groups.append(walk_graph(graph, node))
    
    return groups
    
def part1():
    with open('input/12.txt') as f:
        graph = parse_graph(f)
        connections = walk_graph(graph, 0)
        print(len(connections))
        
def part2():
    with open('input/12.txt') as f:
        graph = parse_graph(f)
        groups = find_all_groups(graph)
        print(len(groups))

if __name__ == '__main__':
    part1()
    part2()
    
    