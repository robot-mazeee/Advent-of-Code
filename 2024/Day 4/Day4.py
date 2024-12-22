with open("2024/Day 4/input.txt", 'r') as file:
    lines = file.readlines()

def parse_input():
    chars = []
    for line in lines:
        l = []
        for c in line:
            l.append(c)
        chars.append(l)
    return chars

def check_diagonals_XMAS(chars, i, j):
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

def check_horizontal_XMAS(chars, i, j):
    count = 0
    if j < len(chars[i])-3:
        if chars[i][j+1] == 'M' and chars[i][j+2] == 'A' and chars[i][j+3] == 'S':
            count += 1
    if j > 2:
        if chars[i][j-1] == 'M' and chars[i][j-2] == 'A' and chars[i][j-3] == 'S':
            count += 1

    return count

def check_vertical_XMAS(chars, i, j):
    #up and down
    count = 0

    if i < len(chars)-3:
        if chars[i+1][j] == 'M' and chars[i+2][j] == 'A' and chars[i+3][j] == 'S':
            count += 1
    if i > 2:
        if chars[i-1][j] == 'M' and chars[i-2][j] == 'A' and chars[i-3][j] == 'S':
            count += 1

    return count

def check_MAS(chars, i, j):
    # diagonal positiva (down)
    if i > 0 and j > 0 and i < len(chars)-1 and j < len(chars[i])-1:
        if chars[i-1][j-1] == 'M' and chars[i-1][j+1] == 'S' and chars[i+1][j-1] == 'M' and chars[i+1][j+1] == 'S':
            return True
        
        if chars[i-1][j-1] == 'M' and chars[i-1][j+1] == 'M' and chars[i+1][j-1] == 'S' and chars[i+1][j+1] == 'S':
            return True

        if chars[i-1][j-1] == 'S' and chars[i-1][j+1] == 'M' and chars[i+1][j-1] == 'S' and chars[i+1][j+1] == 'M':
            return True
        
        if chars[i-1][j-1] == 'S' and chars[i-1][j+1] == 'S' and chars[i+1][j-1] == 'M' and chars[i+1][j+1] == 'M':
            return True

    return False 

def main():
    chars = parse_input()
    count1 = 0
    count2 = 0
    for i in range(len(chars)):
        for j in range(len(chars[i])):
            if chars[i][j] == 'X':
                count1 += check_diagonals_XMAS(chars, i, j)
                count1 += check_vertical_XMAS(chars, i, j)
                count1 += check_horizontal_XMAS(chars, i, j)
            if chars[i][j] == 'A':
                count2 += check_MAS(chars, i, j)

    print("Part 1:", count1)
    print("Part 2:", count2)

main()