import re

with open('2024/Day 3/input.txt', 'r') as file:
    lines = file.readlines()

def main():
    result1 = 0
    result2 = 0
    do = True
    for line in lines:
        pattern = r'mul\('
        parts = re.split(pattern, line)

        for m in parts:
            num1 = 0
            num2 = 0
            pattern = r'(\d+),(\d+)\)'
            match = re.match(pattern, m)

            if match:
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                # Part 1
                result1 += num1*num2
                # Part 2
                if do:
                    result2 += num1*num2

            pattern_do = r'do\(\)'
            pattern_dont = r'don\'t\(\)'
            if re.search(pattern_do, m):
                do = True
            if re.search(pattern_dont, m):
                do = False

    print("Part 1:", result1)
    print("Part 2:", result2)

main()