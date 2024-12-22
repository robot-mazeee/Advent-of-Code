with open("Day 12/input.txt", 'r') as file:
    lines = file.readlines()

matrix = []
for line in lines:
    chars = []
    line = line.strip()
    for char in line:
        chars.append(char)
    matrix.append(chars)

visited = []

def get_adj(char, i, j):
    adj = []
    per = 0

    # esquerda
    if j-1 >= 0: 
        if matrix[i][j-1] == char and (i, j-1) not in visited:
            adj.append((i, j-1))
            visited.append((i, j-1))
        elif matrix[i][j-1] != char: 
            per += 1
    else:
        per += 1

    # direita
    if j+1 < len(matrix[0]):
        if matrix[i][j+1] == char and (i, j+1) not in visited:
            adj.append((i, j+1))
            visited.append((i, j+1))
        elif matrix[i][j+1] != char: 
            per += 1
    else:
        per += 1

    # up
    if i-1 >= 0:
        if matrix[i-1][j] == char and (i-1, j) not in visited:
            adj.append((i-1, j))
            visited.append((i-1, j))
        elif matrix[i-1][j] != char: 
            per += 1
    else:
        per += 1

    # down
    if i+1 < len(matrix):
        if matrix[i+1][j] == char and (i+1, j) not in visited:
            adj.append((i+1, j))
            visited.append((i+1, j))
        elif matrix[i+1][j] != char: 
            per += 1
    else:
        per += 1

    return (adj, per)

def calculate_region(char, i, j):
    region = [(i, j)]
    area = 0
    per = 0

    while region:
        node = region.pop()
        area += 1
        i = node[0]
        j = node[1]
        adj, p = get_adj(char, i, j)
        per += p
        for pos in adj:
            visited.append(pos)
            region.append(pos)

    print(char, area, per)
    return area*per

def print_matrix():
    string = ''
    for line in matrix:
        for char in line:
            string += char
        string += '\n'
    print(string)

res = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if (i, j) not in visited:
            visited.append((i, j))
            res += calculate_region(matrix[i][j], i, j)

print(res)