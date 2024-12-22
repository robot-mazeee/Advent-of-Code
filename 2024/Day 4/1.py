# Result: 2549

with open("Day 4/input.txt", 'r') as file:
    lines = file.readlines()

chars = []
for line in lines:
    l = []
    for c in line:
        l.append(c)
    chars.append(l)

def check_diagonals(i, j):
    # diagonal positive and negative
    count = 0

    # down diagonal
    if i < len(chars)-3 and j < len(chars[i])-3:
        if chars[i+1][j+1] == 'M' and chars[i+2][j+2] == 'A' and chars[i+3][j+3]== 'S':
            count += 1

    # up diagonal
    if i > 2 and j > 2:
        if chars[i-1][j-1] == 'M' and chars[i-2][j-2] == 'A' and chars[i-3][j-3] == 'S':
            count += 1

    # down counter diagonal: increment i and decrement j
    if i < len(chars)-3 and j > 2:
        if chars[i+1][j-1] == 'M' and chars[i+2][j-2] == 'A' and chars[i+3][j-3] == 'S':
            count += 1

    # up counter diagonal: increment j and decrement i
    if j < len(chars[i])-3 and i > 2:
        if chars[i-1][j+1] == 'M' and chars[i-2][j+2] == 'A' and chars[i-3][j+3] == 'S':
            count += 1

    return count 

def check_horizontal(i, j):
    count = 0
    if j < len(chars[i])-3:
        if chars[i][j+1] == 'M' and chars[i][j+2] == 'A' and chars[i][j+3] == 'S':
            count += 1
    if j > 2:
        if chars[i][j-1] == 'M' and chars[i][j-2] == 'A' and chars[i][j-3] == 'S':
            count += 1

    return count


def check_vertical(i, j):
    #up and down
    count = 0

    if i < len(chars)-3:
        if chars[i+1][j] == 'M' and chars[i+2][j] == 'A' and chars[i+3][j] == 'S':
            count += 1
    if i > 2:
        if chars[i-1][j] == 'M' and chars[i-2][j] == 'A' and chars[i-3][j] == 'S':
            count += 1

    return count

count = 0
for i in range(len(chars)):
    for j in range(len(chars[i])):
        if chars[i][j] == 'X':
            count += check_diagonals(i, j)
            count += check_vertical(i, j)
            count += check_horizontal(i, j)

print(count)