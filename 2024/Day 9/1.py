with open('Day 9/input.txt', 'r') as file:
    i = 0
    ids = 0
    number = []
    res = 0
    count = 0
    while True:
        char = file.read(1)  # Read one character at a time
        # print(char)
        if not char:  # EOF reached
            break
        # Se for par, eh um bloco
        n = int(char)
        if i % 2 == 0:
            for j in range(n):
                number.append(str(ids))
            count += n
            ids += 1
        else:
            for j in range(n):
                number.append('.')
        i += 1

print(number)

length = len(number)
index = length-1
num = []
for i in range(count):
    if number[i] != '.':
        num.append(number[i])
    else:
        while number[index] == '.':
            index -= 1
        if index > i:
            num.append(number[index])
            number[index], number[i] = number[i], number[index]
            index -= 1

print(num)
ids = 0
for i in num:
    if i == '.':
        break
    else:
        res += int(i)*ids
    ids += 1

print(res)