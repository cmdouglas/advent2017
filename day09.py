from collections import deque

def score_stream(stream):
    ignore_next_char = False
    in_garbage = False
    stack = deque()
    score = 0
    
    for char in stream:
        if ignore_next_char:
            ignore_next_char = False
            continue
        
        if char == '!':
            ignore_next_char = True
            continue
        
        if in_garbage and char == '>':
            in_garbage = False
            continue
        
        if not in_garbage:
            if char == '<':
                in_garbage = True
                continue
            
            if char == r'{':
                stack.append(char)
                continue
                
            if char == r'}':
                score += len(stack)
                stack.pop()
                continue
    
    return score
    
def count_garbage_chars(stream):
    ignore_next_char = False
    in_garbage = False
    stack = deque()
    score = 0
    
    for char in stream:
        if ignore_next_char:
            ignore_next_char = False
            continue
        
        if char == '!':
            ignore_next_char = True
            continue
        
        if in_garbage:
            if char == '>':
                in_garbage = False
                continue
            else:
                score += 1
        
        if not in_garbage:
            if char == '<':
                in_garbage = True
                continue
            
            if char == r'{':
                stack.append(char)
                continue
                
            if char == r'}':
                stack.pop()
                continue
    
    return score
    
def tests():
    assert score_stream('{}') == 1
    assert score_stream('{{{}}}') == 6
    assert score_stream('{{{},{},{{}}}}') == 16
    assert score_stream('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3
    
def part1():
    with open('input/9.txt') as f:
        stream = f.read().strip()
        print(score_stream(stream))
        
    
def part2():
    with open('input/9.txt') as f:
        stream = f.read().strip()
        print(count_garbage_chars(stream))

if __name__ == '__main__':
    part1()
    part2()

            
        