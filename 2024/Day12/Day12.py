with open("2024/Day12/input.txt", 'r') as file:
    lines = file.readlines()

matrix = []
for line in lines:
    chars = []
    line = line.strip()
    for char in line:
        chars.append(char)
    matrix.append(chars)

def get_adj_p1(visited, char, i, j):
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

def get_adj_p2(visited, char, i, j):
    adj = []

    # esquerda
    if j-1 >= 0: 
        if matrix[i][j-1] == char and (i, j-1) not in visited:
            adj.append((i, j-1))
            visited.append((i, j-1))
        
    # direita
    if j+1 < len(matrix[0]):
        if matrix[i][j+1] == char and (i, j+1) not in visited:
            adj.append((i, j+1))
            visited.append((i, j+1))

    # up
    if i-1 >= 0:
        if matrix[i-1][j] == char and (i-1, j) not in visited:
            adj.append((i-1, j))
            visited.append((i-1, j))

    # down
    if i+1 < len(matrix):
        if matrix[i+1][j] == char and (i+1, j) not in visited:
            adj.append((i+1, j))
            visited.append((i+1, j))

    return adj

def get_single_adj(char, i, j):
    adj = []

    # esquerda
    if j-1 >= 0 and matrix[i][j-1] == char:
        adj.append((i, j-1))
        
    # direita
    if j+1 < len(matrix[0]) and matrix[i][j+1] == char:
        adj.append((i, j+1))

    # up
    if i-1 >= 0 and matrix[i-1][j] == char:
            adj.append((i-1, j))

    # down
    if i+1 < len(matrix) and matrix[i+1][j] == char:
        adj.append((i+1, j))

    return adj    

def is_adj(i, j, x, y):
    if i == x+1 and j == y:
        return True
    if i == x-1 and j == y:
        return True
    if i == x and j == y+1:
        return True
    if i == x and j == y-1:
        return True
    return False

def get_per(char, region):
    up = []
    down = []
    left = []
    right = []
    per = 0

    for i, j in region:
        adj = get_single_adj(char, i, j)
        if (i, j+1) not in adj:
            right.append((i, j))
        if (i, j-1) not in adj:
            left.append((i, j))
        if (i+1, j) not in adj:
            down.append((i, j))
        if (i-1, j) not in adj:
            up.append((i, j))

    up = sorted(up, key=lambda x: (x[0], x[1]))
    right = sorted(right, key=lambda x: (x[0], x[1]))
    down = sorted(down, key=lambda x: (x[0], x[1]))
    left = sorted(left, key=lambda x: (x[0], x[1]))

    k = 0
    l = 0
    while k < len(left)-1:
        l = k+1
        i, j = left[k]
        remove_left = []
        while l < len(left):
            x, y = left[l]
            if is_adj(i, j, x, y):
                remove_left.append((i, j))
                i, j = x, y
            l += 1
        for pos in remove_left:
            left.remove(pos)
        if len(remove_left) == 0:
            k += 1

    k = 0
    l = 0
    while k < len(right)-1:
        l = k+1
        i, j = right[k]
        remove_right = []
        while l < len(right):
            x, y = right[l]
            if is_adj(i, j, x, y):
                remove_right.append((i, j))
                i, j = x, y
            l += 1
        for pos in remove_right:
            right.remove(pos)
        if len(remove_right) == 0:
            k += 1

    k = 0
    l = 0
    while k < len(up)-1:
        l = k+1
        i, j = up[k]
        remove_up = []
        while l < len(up):
            x, y = up[l]
            if is_adj(i, j, x, y):
                remove_up.append((i, j))
                i, j = x, y
            l += 1
        for pos in remove_up:
            up.remove(pos)
        if len(remove_up) == 0:
            k += 1

    k = 0
    l = 0  
    while k < len(down)-1:
        l = k+1
        i, j = down[k]
        remove_down = []
        while l < len(down):
            x, y = down[l]
            if is_adj(i, j, x, y):
                remove_down.append((i, j))
                i, j = x, y
            l += 1
        for pos in remove_down:
            down.remove(pos)
        if len(remove_down) == 0:
            k += 1

    per = len(left) + len(right) + len(down) + len(up)
    return per

def calculate_region_p1(visited, char, i, j):
    region = [(i, j)]
    area = 0
    per = 0

    while region:
        node = region.pop()
        area += 1
        i = node[0]
        j = node[1]
        adj, p = get_adj_p1(visited, char, i, j)
        per += p
        for pos in adj:
            visited.append(pos)
            region.append(pos)

    # print(char, area, per)
    return area*per

def calculate_region_p2(visited, char, i, j):
    region = [(i, j)]
    final_region = []
    area = 0

    while region:
        node = region.pop()
        final_region.append(node)
        area += 1
        i = node[0]
        j = node[1]
        adj = get_adj_p2(visited, char, i, j)
        for pos in adj:
            visited.append(pos)
            region.append(pos)

    per = get_per(char, final_region)
    # print(char, area, per)
    return area*per

def print_matrix():
    string = ''
    for line in matrix:
        for char in line:
            string += char
        string += '\n'
    print(string)

def main():
    res1 = 0
    res2 = 0
    visited1 = []
    visited2 = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) not in visited1:
                visited1.append((i, j))
                res1 += calculate_region_p1(visited1, matrix[i][j], i, j)
            if (i, j) not in visited2:
                visited2.append((i, j))
                res2 += calculate_region_p2(visited2, matrix[i][j], i, j)
        # print(i)

    print("Part 1:", res1)
    print("Part 2:", res2)

main()