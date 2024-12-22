i = 0
ids = 0
number = []
count = 0
with open('Day 9/input.txt', 'r') as file:
    while True:
        char = file.read(1)  # Read one character at a time
        if not char:  # EOF reached
            break
        # Se for par, eh um bloco
        n = int(char)
        if i % 2 == 0:
            for _ in range(n):
                number.append(str(ids))
            count += 1
            ids += 1
        elif n != 0:
            for _ in range(n):
                number.append('.')
        i += 1

# with open('Day 9/output.txt', 'w') as file:
#     for char in number:
#         file.write(char + '\n')
# print(number)

def get_size(index):
    size = 0
    char = number[index]
    for i in range(index, 0, -1):
        if number[i] != char:
            break
        else:
            size += 1
    for i in range(index+1, len(number)):
        if number[i] != char:
            break
        else:
            size += 1
    # print(char, size)
    return size

def get_size_front(index):
    size = 0
    for i in range(index, len(number)):
        if number[i] != '.':
            break
        else:
            size += 1
    return size

index = len(number)-1
res = 0
for i in range(index, -1, -1):
    print(i)
    if number[i] == '.':
        continue
    else:
        size = get_size(i)
        l = i
        j = 0
        while not (number[j] == '.' and get_size_front(j) >= size):
            j += 1
            if j >= i:
                break
            continue
        if j >= i:
            continue
        
        if get_size_front(j) >= size:
            for _ in range(size):
                number[i], number[j] = number[j], number[i]
                i -= 1
                j += 1
            i = l-size

# print(number)
length = len(number)
res = 0
for i in range(length):
    if number[i] == '.':
        continue
    res += i*int(number[i])

print(res)
