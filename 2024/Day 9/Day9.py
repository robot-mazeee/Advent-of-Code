def parse_input():
    with open('2024/Day 9/input.txt', 'r') as file:
        i = 0
        ids = 0
        number = []
        count = 0
        while True:
            char = file.read(1)  # Read one character at a time
            # print(char)
            if not char:  # EOF reached
                break
            # Se for par, eh um bloco
            n = int(char)
            if i % 2 == 0:
                for _ in range(n):
                    number.append(str(ids))
                count += n
                ids += 1
            else:
                for _ in range(n):
                    number.append('.')
            i += 1
    
    return number, count

def get_size(number, index):
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

def get_size_front(number, index):
    size = 0
    for i in range(index, len(number)):
        if number[i] != '.':
            break
        else:
            size += 1
    return size

def part1(number, count):
    res = 0
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

    ids = 0
    for i in num:
        if i == '.':
            break
        else:
            res += int(i)*ids
        ids += 1

    print("Part 1:", res)

def part2(number):
    index = len(number)-1
    res = 0
    for i in range(index, -1, -1):
        # print(i)
        if number[i] == '.':
            continue
        else:
            size = get_size(number, i)
            l = i
            j = 0
            while not (number[j] == '.' and get_size_front(number, j) >= size):
                j += 1
                if j >= i:
                    break
                continue
            if j >= i:
                continue
            
            if get_size_front(number, j) >= size:
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

    print("Part 2:", res)

def main():
    number, count = parse_input()
    number_copy = number[:]
    part1(number, count)
    part2(number_copy)

main()