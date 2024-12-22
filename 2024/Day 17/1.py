program = '2415751641550330'

def get_combo_operand(value):
    if value == 0:
        return 0
    if value == 1:
        return 1
    if value == 2:
        return 2
    if value == 3:
        return 3
    if value == 'A':
        return 4
    if value == 'B':
        return 5
    if value == 'C':
        return 6

values = {}
values[get_combo_operand('B')] = 0
values[get_combo_operand('C')] = 0

def get_out(p, regA):
    out = ''

    program = []
    for char in p:
        program.append(int(char))

    values[get_combo_operand('A')] = regA

    i = 0
    num_instructions = len(program)
    while i < num_instructions-1:
        if program[i] == 0:
            regA = get_combo_operand('A')
            reg = program[i+1]
            if reg >= 4:
                denominator = 2**values[reg]
            else:
                denominator = 2**reg
            numerator = values[regA]
            result = numerator // denominator
            values[regA] = result

        elif program[i] == 1: # B XOR operand -> B 
            regB = get_combo_operand('B')
            value1 = values[regB]
            value2 = program[i+1]
            res = value1 ^ value2
            values[regB] = int(res)

        elif program[i] == 2: # values[operand] % 8 -> B
            operand = program[i+1]
            regB = get_combo_operand('B')
            result = values[operand] % 8
            values[regB] = result

        elif program[i] == 3: # nothing if regA = 0
            reg = get_combo_operand('A')
            operand = program[i+1]
            if values[reg] != 0:
                i = operand
                continue

        elif program[i] == 4: # B XOR C -> B
            regB = get_combo_operand('B')
            regC = get_combo_operand('C')
            res = values[regB] ^ values[regC]
            values[regB] = int(res)

        elif program[i] == 5: # operand % 8 -> stdout
            operand = program[i+1]
            if operand >= 4:
                reg = values[operand]
            else:
                reg = operand
            value = reg % 8
            out += str(value)

        elif program[i] == 6: # A / 2**operand -> B
            regA = get_combo_operand('A')
            regB = get_combo_operand('B')
            reg = program[i+1]
            if reg >= 4:
                denominator = 2**values[reg]
            else:
                denominator = 2**reg
            numerator = values[regA]
            result = numerator // denominator
            values[regB] = result

        elif program[i] == 7: # A / 2**operand -> C
            regA = get_combo_operand('A')
            regC = get_combo_operand('C')
            reg = program[i+1]
            if reg >= 4:
                denominator = 2**values[reg]
            else:
                denominator = 2**reg
            numerator = values[regA]
            result = numerator // denominator
            values[regC] = result

        i += 2

    return out

def get_regA(program, index, regA):
    for remainder in range(8):
        if (get_out(list(program), regA*8+remainder) == program[index:]):
            if index == 0:
                return regA*8+remainder
            temp_regA = get_regA(program, index-1, regA*8+remainder)
            if temp_regA != -1:
                return temp_regA
    return -1

print(get_regA(program, len(program)-1, 0))