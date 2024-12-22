import re

# Result: 89823704

with open('Day 3/input.txt', 'r') as file:
    lines = file.readlines()

result = 0
do = True
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
            if do:
                result += num1*num2

        pattern_do = r'do\(\)'
        pattern_dont = r'don\'t\(\)'
        if re.search(pattern_do, m):
            do = True
        if re.search(pattern_dont, m):
            do = False

print(result)