import re

# Result: 167090022

with open('Day 3/input.txt', 'r') as file:
    lines = file.readlines()

result = 0
for line in lines:
    mult = False    
    pattern = r'mul\('
    pattern_nums = r'\d+'
    parts = re.split(pattern, line)

    for m in parts:
        num1 = 0
        num2 = 0
        pattern = r'(\d+),(\d+)\)'
        match = re.match(pattern, m)

        if match:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            result += num1*num2

        print(m, num1, num2, '\n')

print('Result:', result)