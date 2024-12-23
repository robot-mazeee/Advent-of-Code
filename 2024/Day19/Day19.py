def parse_input():
    with open("2024/Day19/input.txt", 'r') as file:
        lines = file.readlines()

    towels = lines[0]
    towels = towels.strip()
    towels = towels.split(', ')

    patterns = []
    for i in range(2, len(lines)):
        line = lines[i].strip()
        patterns.append(line)

    return towels, patterns

def is_possible(pattern, towels, num_towels, current, index, memo):
    if (current, index) in memo:
        return memo[(current, index)]
    
    for i in range(num_towels):
        offset = len(towels[i])
        if current + towels[i] == pattern[:index+offset]:
            if index+offset == len(pattern):
                memo[(current, index)] = True
                return True
            if is_possible(pattern, towels, num_towels, current+towels[i], index+offset, memo):
                memo[(current, index)] = True
                return True
    
    memo[(current, index)] = False
    return False

def count_ways(pattern, towels, current, index, memo):
    if (current, index) in memo:
        return memo[(current, index)]

    if index == len(pattern):
        return 1

    count = 0
    for towel in towels:
        offset = len(towel)
        if current + towel == pattern[:index + offset]:
            count += count_ways(pattern, towels, current + towel, index + offset, memo)

    memo[(current, index)] = count
    return count

def main():
    towels, patterns = parse_input()
    num_towels = len(towels)

    count = 0
    num_ways = 0
    for pattern in patterns:
        # print('Pattern: ', pattern)
        # Part 1
        if is_possible(pattern, towels, num_towels, '', 0, {}):
            count += 1
            # Part 2
            num_ways += count_ways(pattern, towels, '', 0, {})

    print("Part 1:", count)
    print("Part 2:", num_ways)

main()