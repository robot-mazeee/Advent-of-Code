# Result: 2003

with open("Day 4/input.txt", 'r') as file:
    lines = file.readlines()

chars = []
for line in lines:
    l = []
    for c in line:
        l.append(c)
    chars.append(l)

def check(i, j):
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

count = 0
for i in range(len(chars)):
    for j in range(len(chars[i])):
        if chars[i][j] == 'A':
            count += check(i, j)

print(count)