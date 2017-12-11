def parse_instruction(line):
    reg, op, value, _, cond_reg, cond_op, cond_value = line.split()
    value, cond_value = int(value), int(cond_value)
    return reg, op, value, cond_reg, cond_op, cond_value
    
def meets_condition(regs, cond_reg, cond_op, cond_value):
    reg_val = regs.get(cond_reg, 0)
    
    if cond_op == '==':
        return reg_val == cond_value
    elif cond_op == '>':
        return reg_val > cond_value
    elif cond_op == '>=':
        return reg_val >= cond_value
    elif cond_op == '<':
        return reg_val < cond_value
    elif cond_op == '<=':
        return reg_val <= cond_value
    elif cond_op == '!=':
        return reg_val != cond_value
    
def apply_instruction(regs, reg, op, value, cond_reg, cond_op, cond_value):
    reg_val = regs.get(reg, 0)
    
    if meets_condition(regs, cond_reg, cond_op, cond_value):
        if op == 'inc':
            regs[reg] = reg_val + value
        elif op == 'dec':
            regs[reg] = reg_val - value

def part1():
    regs = {}
    with open('input/8.txt') as f:
        for line in f:
            inst = parse_instruction(line)
            apply_instruction(regs, *inst)
        
    print(max(regs.values()))
    
def part2():
    regs = {}
    highest_value = 0
    with open('input/8.txt') as f:
        for line in f:
            inst = parse_instruction(line)
            apply_instruction(regs, *inst)
            reg = inst[0]
            highest_value = max(highest_value, regs.get(reg, 0))
    
    print(highest_value)

if __name__ == '__main__':
    part1()
    part2()