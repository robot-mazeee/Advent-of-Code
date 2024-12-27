def parse_input():
    with open("2024/Day24/input.txt", 'r') as file:
        lines = [line.strip() for line in file]
    
    start_values = []
    operations = []
    length = len(lines)

    start = 0
    for i in range(length):
        if lines[i] == '':
            start = i+1
            break
        else:
            line = lines[i].split(': ')
            start_values.append(line)

    for i in range(start, length):
        line = lines[i].split(' -> ')
        line[0] = line[0].split()
        operations.append(line)

    return start_values, operations

def get_output(wires, wire1, gate, wire2):
    if gate == 'AND':
        return wires[wire1] and wires[wire2]
    if gate == 'OR':
        return wires[wire1] or wires[wire2]
    if gate == 'XOR':
        return wires[wire1] ^ wires[wire2]

def simulate(wires, operations, num_operations):
    index = 0
    while num_operations > 0 and index < num_operations:
        wire1, operation, wire2 = operations[index][0]
        out_wire = operations[index][1]
        if wire1 in wires and wire2 in wires:
            wires[out_wire] = get_output(wires, wire1, operation, wire2)
            operations.remove(operations[index])
            num_operations -= 1
            index = 0
        else:
            index += 1

def part1(start_values, operations):
    wires = {}
    for key, value in start_values:
        wires[key] = int(value)

    simulate(wires, operations.copy(), len(operations))
    sorted_wires = dict(sorted(wires.items(), reverse=True))

    number = ''
    for key in sorted_wires:
        value = sorted_wires[key]
        if key[0] == 'z':
            number += str(value)
        else:
            break
    
    return int(number, 2)

def swap_wires(operations, wire1, wire2):
    num_operations = len(operations)
    for i in range(num_operations):
        _, out_wire = operations[i]
        if out_wire == wire1:
            operations[i][1] = wire2
        elif out_wire == wire2:
            operations[i][1] = wire1

def get_out_wire(operations, wire1, gate, wire2):
    for operation, out_wire in operations:
        if operation[0] == wire1 and operation[1] == gate and operation[2] == wire2:
            return out_wire
        if operation[0] == wire2 and operation[1] == gate and operation[2] == wire1:
            return out_wire

def get_swapped_wires(operations):
    '''
    This is a ripple-carry adder; bit 0 is a half-adder, the others are
    full-adders (composed by two half-adders):

    half-adder: SUM = x XOR y
                CARRY = x AND y
    full-adder: SUM = (x XOR y) XOR CARRY-IN
                CARRY-OUT = (x AND y) OR (CARRY-IN AND (x XOR y))

    LOGIC: SUM, CARRY_OUT, CARRY_IN, etc, are WIRES, not values
        for each bit:
            if current bit is 0: 
                current carry = x00 AND y00 (half-adder carry)
            otherwise: 
                get x XOR y (half-adder sum)
                get x AND y (half-adder carry)
                get SUM ((x XOR y) XOR current carry - full-adder sum)
                if SUM does not exist: 
                    swap half-adder carry with half-adder sum
                elif SUM is not the correspondent z-wire:
                    swap SUM with correspondent z-wire
                get next carry and go to next bit
    '''
    CARRY_IN = None
    bit = 0
    swapped_wires = []

    while bit < 45:
        x_wire = f'x{bit:02d}'
        y_wire = f'y{bit:02d}'
        z_wire = f'z{bit:02d}'

        if bit == 0:
            CARRY_IN = get_out_wire(operations, x_wire, 'AND', y_wire)
        else:
            # sum both wires
            INTERMEDIATE_SUM = get_out_wire(operations, x_wire, 'XOR', y_wire)
            # sum with carry
            SUM = get_out_wire(operations, INTERMEDIATE_SUM, 'XOR', CARRY_IN)
            # get intermediate carry
            INTERMEDIATE_CARRY = get_out_wire(operations, x_wire, 'AND', y_wire)

            if SUM is None:
                # swap intermediate sum with intermediate carry
                swapped_wires.append(INTERMEDIATE_SUM)
                swapped_wires.append(INTERMEDIATE_CARRY)
                swap_wires(operations, INTERMEDIATE_SUM, INTERMEDIATE_CARRY)
                continue

            elif SUM != z_wire:
                # swap output wire with z-wire
                swapped_wires.append(z_wire)
                swapped_wires.append(SUM)
                swap_wires(operations, z_wire, SUM)
                continue

            # get next carry
            carry = get_out_wire(operations, INTERMEDIATE_SUM, 'AND', CARRY_IN)
            CARRY_IN = get_out_wire(operations, INTERMEDIATE_CARRY, 'OR', carry)

        # go to next bit
        bit += 1

    return swapped_wires

def part2(operations):
    swapped_wires = get_swapped_wires(operations)
    swapped_wires = sorted(swapped_wires)

    wires = ''
    for wire in swapped_wires:
        wires += wire + ','
    wires = wires[:len(wires)-1]

    return wires

def main():
    start_values, operations = parse_input()
    
    number = part1(start_values, operations)
    print("Part 1:", number)

    swapped_wires = part2(operations)
    print("Part 2:", swapped_wires)

main()