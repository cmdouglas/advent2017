import enum
from collections import deque

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
RUNNING = 'running'
WAITING = 'waiting'
TERMINATED = 'terminated'

def run(program):
    pc = 0
    regs = {l: 0 for l in LETTERS}
    sounds = []
    
    def value_of(operand):
        if operand in LETTERS:
            return regs[operand]
        else:
            return int(operand)
    
    while True:
        if pc < 0 or pc >= len(program):
            break
        
        inst, *operands = program[pc]
        # print(inst, operands)
        
        if inst == 'snd':
            x = operands[0]
            sounds.append(value_of(x))
        elif inst == 'set':
            x, y = operands
            regs[x] = value_of(y)
        elif inst == 'add':
            x, y = operands
            regs[x] += value_of(y)
        elif inst == 'mul':
            x, y = operands
            regs[x] *= value_of(y)
        elif inst == 'mod':
            x, y = operands
            regs[x] %= value_of(y)
        elif inst == 'rcv':
            x = operands[0]
            if value_of(x) != 0:
                yield sounds[len(sounds) - 1]
        elif inst == 'jgz':
            x, y = operands
            if value_of(x) > 0:
                pc += value_of(y)
                continue;
        
        pc += 1
        
def run2(program, prog_id):
    pc = 0
    regs = {l: 0 for l in LETTERS}
    regs['p'] = prog_id
    
    def value_of(operand):
        if operand in LETTERS:
            return regs[operand]
        else:
            return int(operand)
    
    while True:
        if pc < 0 or pc >= len(program):
            break
        
        inst, *operands = program[pc]
        print(prog_id, pc, inst, operands)
        
        if inst == 'snd':
            x = operands[0]
            yield(('snd', value_of(x)))
        elif inst == 'set':
            x, y = operands
            regs[x] = value_of(y)
        elif inst == 'add':
            x, y = operands
            regs[x] += value_of(y)
        elif inst == 'mul':
            x, y = operands
            regs[x] *= value_of(y)
        elif inst == 'mod':
            x, y = operands
            regs[x] %= value_of(y)
        elif inst == 'rcv':
            x = operands[0]
            snd = yield(('rcv',))
            if type(snd) == int:
                regs[x] = snd
            else:
                continue
        elif inst == 'jgz':
            x, y = operands
            if value_of(x) > 0:
                pc += value_of(y)
                continue;
        
        pc += 1
        
class Runtime:
    def __init__(self, program, id):
        self.program = program
        self.id = id
        self.status = RUNNING
        self.execution = run2(self.program, self.id)
        self.out_queue = deque()
        self.sends = 0
        
    def next(self):
        try:
            response = next(self.execution)
        except StopIteration:
            self.status = TERMINATED
            
        print("RESPONSE", response)
            
        if response[0] == 'snd':
            self.status = RUNNING
            self.out_queue.append(response[1])
            self.sends += 1
        elif response[0] == 'rcv':
            self.status = WAITING
            
    def send(self, value):
        try:
            response = self.execution.send(value)
        except StopIteration:
            self.status = TERMINATED
            
        print("RESPONSE", response)
            
        if response[0] == 'snd':
            self.status = RUNNING
            self.out_queue.append(response[1])
            self.sends += 1
        elif response[0] == 'rcv':
            self.status = WAITING
        

def part1():
    with open('input/18.txt') as f:
        program = [line.split(' ') for line in f.read().split('\n')]
        runtime = run(program)
        sound_recieved = next(runtime)
        print(sound_recieved)
        
def part2():
    with open('input/18.txt') as f:
        program = [line.split(' ') for line in f.read().split('\n')]
        r0 = Runtime(program, 0)
        r1 = Runtime(program, 1)
        
        while True:
            if r0.status == WAITING and r1.out_queue:
                r0.send(r1.out_queue.popleft())
            elif r1.status == WAITING and r0.out_queue:
                r1.send(r0.out_queue.popleft())
            elif r1.status == RUNNING:
                r1.next()
            elif r0.status == RUNNING:
                r0.next()
            else:
                print(r0.status, r1.out_queue, r1.status, r0.out_queue)
                break
        print(r1.sends)

if __name__ == '__main__':
    part1()
    part2()