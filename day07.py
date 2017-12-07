from collections import Counter

def construct_tree(lines):
    tree = {}
    for line in lines:
        name, weight, children = parse_line(line)
        if not tree.get(name):
            tree[name] = dict(name=name, weight=weight, parent=None)
        else:
            tree[name]['weight'] = weight
        
        tree[name]['children'] = children
        
        for child in children:
            if not tree.get(child):
                tree[child] = dict(name=child, weight=None, parent=name)
            else:
                tree[child]['parent'] = name
    
    return tree
    
def parse_line(line):
    chunks = line.split()
    name = chunks[0]
    weight = int(chunks[1][1:-1])
    children = []
    if len(chunks) > 2:
        children = [child.strip(',') for child in chunks[3:]]
    return name, weight, children
    
def total_weight(tree, node):
    if node.get('total_weight'):
        return node['total_weight']
    
    if not node['children']:
        node['total_weight'] = node['weight']
    else:
        node['total_weight'] = node['weight'] + sum([total_weight(tree, tree[child]) for child in node['children']])
    
    return node['total_weight']

def weight_discrepancy(tree, node):
    if not node['children']:
        return 0

    child_weights = [total_weight(tree, tree[child]) for child in node['children']]
    return max(child_weights) - min(child_weights)
    
def deepest_weight_discrepancy(tree, node, depth=0):
    if weight_discrepancy(tree, node) == 0:
        return (depth - 1, node['parent'])
    
    else:
        return max([deepest_weight_discrepancy(tree, tree[child], depth + 1) for child in node['children']])
        
def get_tree():
    with open('input/7.txt') as f:
        tree = construct_tree(f)
        return tree
        
def root(tree):
    return [node for node in tree.values() if node['parent'] is None][0]
    

def part1():
    tree = get_tree()
    print(root(tree)['name'])
    
def part2():
    tree = get_tree()
    r = root(tree)
    depth, name = deepest_weight_discrepancy(tree, r)
    node = tree[name]
    
    # one of node's children is either too heavy or too light
    # we can also assume that node has 3 or more children
    assert len(node['children']) > 2
    weights = [total_weight(tree, tree[child]) for child in node['children']]
    c = Counter(weights)
    #print(c)
    normal_weight = c.most_common()[0][0]
    outlier_weight = c.most_common()[-1][0]
    
    #print(normal_weight)
    #print(outlier_weight)
    
    discrepancy = normal_weight - outlier_weight
    outlier = [tree[child]['weight'] for child in node['children'] if total_weight(tree, tree[child]) == outlier_weight][0]
    
    print(outlier + discrepancy)
    
    

if __name__ == '__main__':
    part1()
    part2()
