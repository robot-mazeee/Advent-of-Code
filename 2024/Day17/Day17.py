def get_literal_operand(value):
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

def get_out(values, p, regA):
    out = ''

    program = []
    for char in p:
        program.append(int(char))

    values[get_literal_operand('A')] = regA

    i = 0
    num_instructions = len(program)
    while i < num_instructions-1:
        if program[i] == 0:
            regA = get_literal_operand('A')
            reg = program[i+1]
            if reg >= 4:
                denominator = 2**values[reg]
            else:
                denominator = 2**reg
            numerator = values[regA]
            result = numerator // denominator
            values[regA] = result

        elif program[i] == 1: # B XOR operand -> B 
            regB = get_literal_operand('B')
            value1 = values[regB]
            value2 = program[i+1]
            res = value1 ^ value2
            values[regB] = int(res)

        elif program[i] == 2: # values[operand] % 8 -> B
            operand = program[i+1]
            regB = get_literal_operand('B')
            result = values[operand] % 8
            values[regB] = result

        elif program[i] == 3: # nothing if regA = 0
            reg = get_literal_operand('A')
            operand = program[i+1]
            if values[reg] != 0:
                i = operand
                continue

        elif program[i] == 4: # B XOR C -> B
            regB = get_literal_operand('B')
            regC = get_literal_operand('C')
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
            regA = get_literal_operand('A')
            regB = get_literal_operand('B')
            reg = program[i+1]
            if reg >= 4:
                denominator = 2**values[reg]
            else:
                denominator = 2**reg
            numerator = values[regA]
            result = numerator // denominator
            values[regB] = result

        elif program[i] == 7: # A / 2**operand -> C
            regA = get_literal_operand('A')
            regC = get_literal_operand('C')
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

def get_regA(values, program, index, regA):
    for remainder in range(8):
        if (get_out(values,list(program),regA*8+remainder) == program[index:]):
            if index == 0:
                return regA*8+remainder
            temp_regA = get_regA(values, program, index-1, regA*8+remainder)
            if temp_regA != -1:
                return temp_regA
    return -1

def main():
    values = {}
    values[get_literal_operand('B')] = 0
    values[get_literal_operand('C')] = 0
    program = '2415751641550330'

    out = get_out(values, program, 60589763)
    out = str(out)

    output = ''
    for char in out:
        output += char + ','

    print("Part 1:", output[:len(output)-1])
    print("Part 2:", get_regA(values, program, len(program)-1, 0))

main()