with open("Day 19/input.txt", 'r') as file:
    lines = file.readlines()

towels = lines[0]
towels = towels.strip()
towels = towels.split(', ')
num_towels = len(towels)

patterns = []
for i in range(2, len(lines)):
    line = lines[i].strip()
    patterns.append(line)

def is_possible(pattern, towels, current, index, memo):
    if (current, index) in memo:
        return memo[(current, index)]
    
    for i in range(num_towels):
        offset = len(towels[i])
        if current + towels[i] == pattern[:index+offset]:
            if index+offset == len(pattern):
                memo[(current, index)] = True
                return True
            if is_possible(pattern, towels, current+towels[i], index+offset, memo):
                memo[(current, index)] = True
                return True
    
    memo[(current, index)] = False
    return False

def count_ways(pattern, towels, current, index, memo):
    # Check if the result for the current state is already computed
    if (current, index) in memo:
        return memo[(current, index)]

    # Base case: If we've matched the entire pattern, count as 1 way
    if index == len(pattern):
        return 1

    count = 0
    for towel in towels:
        offset = len(towel)
        # Check if the next segment matches the pattern
        if current + towel == pattern[:index + offset]:
            # Add the count of ways from the next state
            count += count_ways(pattern, towels, current + towel, index + offset, memo)

    # Store the result in the memo and return it
    memo[(current, index)] = count
    return count

count = 0
num_ways = 0
for pattern in patterns:
    print('Pattern: ', pattern)
    # Part 1
    if is_possible(pattern, towels, '', 0, {}):
        count += 1
        # Part 2
        num_ways += count_ways(pattern, towels, '', 0, {})

print(count, num_ways)