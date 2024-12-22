with open("Day 11/input.txt", 'r') as file:
    matrix = [list(line.split()) for line in file]

for line in matrix:
    for elem in line:
        if elem == ' ':
            line.remove(elem)

def get_number(line):
    for _ in range(25):
        length = len(line)
        i = 0
        while i < length:
            if line[i] == '0':
                line[i] = '1'
                i += 1
            elif len(line[i]) % 2 == 0:
                # partir a string
                num1 = int(line[i][:len(line[i])//2])
                num2 = int(line[i][len(line[i])//2:])
                line = line[:i] + [str(num1)] + [str(num2)] + line[i+1:]
                length += 1
                i += 2
            else:
                line[i] = str(int(line[i])*2024)
                i += 1
    return len(line)

res = 0
for line in matrix:
    for elem in line:
        res += get_number([elem])

print(res)