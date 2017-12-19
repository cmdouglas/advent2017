import re

SPIN = re.compile(r's([\d]+)')
EXCHANGE = re.compile(r'x([\d]+)/([\d]+)')
PARTNER = re.compile(r'p([a-z])/([a-z])')

def parse_moves(strs):
    moves = []
    for s in strs:
        if s[0] == 's':
            moves.append(('s', int(re.findall(SPIN, s)[0])))
        elif s[0] == 'x':
            p1, p2 = [int(p) for p in re.findall(EXCHANGE, s)[0]]
            moves.append(('x', p1, p2))
        elif s[0] == 'p':
            d1, d2 = re.findall(PARTNER, s)[0]
            moves.append(('p', d1, d2))

    return moves

def do_spin(dancers, num):
    for _ in range(num):
        dancers.insert(0, dancers.pop())

def do_exchange(dancers, p1, p2):
    dancers[p1], dancers[p2] = dancers[p2], dancers[p1]
    
def do_partner(dancers, d1, d2):
    do_exchange(dancers, dancers.index(d1), dancers.index(d2))
    
def do_move(dancers, move):
    if move[0] == 's':
        do_spin(dancers, move[1])
    elif move[0] == 'x':
        do_exchange(dancers, move[1], move[2])
    elif move[0] == 'p':
        do_partner(dancers, move[1], move[2])
        
def do_dance(dancers, moves):
    for move in moves:
        do_move(dancers, move)
    return dancers
    
def get_moves():
    with open('input/16.txt') as f:
        moves = parse_moves(f.read().strip().split(','))
        return moves

def part1():
    dancers = list('abcdefghijklmnop')
    moves = get_moves()
    for move in moves:
        do_move(dancers, move)
    
    print(''.join(dancers))
    
def find_cycle(dancers, moves):
    positions = {}
    pos = 0
    while True:
        position = ''.join(dancers)
        existing = positions.get(position)
        if existing:
            return existing, pos - existing
        positions[''.join(dancers)] = pos
        pos += 1
        do_dance(dancers, moves)
        
    
def part2():
    dancers = list('abcdefghijklmnop')
    moves = get_moves()
    ending_pos = 1_000_000_000
    pos, cycle_length = find_cycle(dancers, moves)
    ending_pos -= pos
    offset = ending_pos % cycle_length
    for _ in range(offset):
        do_dance(dancers, moves)
    
    print(''.join(dancers))

if __name__ == '__main__':
    part1()
    part2()