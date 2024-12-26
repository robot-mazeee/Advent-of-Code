def parse_input():
    with open("2024/Day15/input.txt", 'r') as file:
        lines = [list(line.strip()) for line in file]

    matrix_p1 = []
    for line in lines:
        current_line = []
        for char in line:
            current_line.append(char)
        matrix_p1.append(current_line)

    matrix_p2 = []
    for line in lines:
        string = ''
        for char in line:
            if char == '#':
                string += '##'
            elif char == 'O':
                string += "[]"
            elif char == '.':
                string += '..'
            elif char == '@':
                string += '@.'
        matrix_p2.append(list(string))
    
    with open("2024/Day15/moves.txt", 'r') as file:
        lines = [line.strip() for line in file]

    moves = ""
    for line in lines:
        moves += line

    return matrix_p1, matrix_p2, moves

def get_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '@':
                return (i, j)

def push_left_p1(matrix, boxes, i, j):
    if boxes == 0:
        if j-1 > 0 and matrix[i][j-1] != '#':
            matrix[i][j] = '.'
            matrix[i][j-1] = '@'
            return (i, j-1)
    else:
        while boxes != 0:
            matrix[i][j-boxes-1] = 'O'
            boxes -= 1
        matrix[i][j] = '.'
        matrix[i][j-1] = '@'
        return (i, j-1)
    
    return (i, j)

def push_right_p1(matrix, boxes, i, j):
    if boxes == 0:
        if j+1 < len(matrix[0]) and matrix[i][j+1] != '#':
            matrix[i][j] = '.'
            matrix[i][j+1] = '@'
            return (i, j+1)
    else:
        while boxes != 0:
            matrix[i][j+boxes+1] = 'O'
            boxes -= 1
        matrix[i][j] = '.'
        matrix[i][j+1] = '@'
        return (i, j+1)
    return (i, j)

def push_up_p1(matrix, boxes, i, j):
    if boxes == 0:
        if i-1 > 0 and matrix[i-1][j] != '#':
            matrix[i][j] = '.'
            matrix[i-1][j] = '@'
            return (i-1, j)
    else:
        while boxes != 0:
            matrix[i-boxes-1][j] = 'O'
            boxes -= 1
        matrix[i][j] = '.'
        matrix[i-1][j] = '@'
        return (i-1, j)

def push_down_p1(matrix, boxes, i, j):
    if boxes == 0:
        if i+1 < len(matrix) and matrix[i+1][j] != '#':
            matrix[i][j] = '.'
            matrix[i+1][j] = '@'
            return (i+1, j)
    else:
        while boxes != 0:
            matrix[i+boxes+1][j] = 'O'
            boxes -= 1
        matrix[i][j] = '.'
        matrix[i+1][j] = '@'
        return (i+1, j)

def move_p1(matrix, char, i, j):
    # move left
    if char == '<':
        boxes = 0
        for x in range(j-1, 0, -1):
            if matrix[i][x] == 'O':
                boxes += 1
            elif matrix[i][x] == '.':
                return push_left_p1(matrix, boxes, i, j)
            else:
                break
            
    elif char == '>':
        boxes = 0
        for x in range(j+1, len(matrix[0])-1):
            if matrix[i][x] == 'O':
                boxes += 1
            elif matrix[i][x] == '.':
                return push_right_p1(matrix, boxes, i, j)
            elif matrix[i][x] == '#':
                break
            
    # move up
    elif char == '^':
        boxes = 0
        for x in range(i-1, 0, -1):
            if matrix[x][j] == 'O':
                boxes += 1
            elif matrix[x][j] == '.':
                return push_up_p1(matrix, boxes, i, j)
            elif matrix[x][j] == '#':
                break
            
    # move down
    elif char == 'v':
        boxes = 0
        for x in range(i+1, len(matrix)):
            if matrix[x][j] == 'O':
                boxes += 1
            elif matrix[x][j] == '.':
                return push_down_p1(matrix, boxes, i, j)
            elif matrix[x][j] == '#':
                break
            
    return (i, j)

def push_left_p2(matrix, boxes, i, j):
    if boxes == 0:
        if j-1 > 0 and matrix[i][j-1] != '#':
            matrix[i][j] = '.'
            matrix[i][j-1] = '@'
            return (i, j-1)
    else:
        while boxes != 0:
            matrix[i][j-2*boxes-1] = '['
            matrix[i][j-2*boxes] = ']'
            boxes -= 1
        matrix[i][j] = '.'
        matrix[i][j-1] = '@'
        return (i, j-1)

    return (i, j)

def push_right_p2(matrix, boxes, i, j):
    if boxes == 0:
        if j+1 < len(matrix[0]) and matrix[i][j+1] != '#':
            matrix[i][j] = '.'
            matrix[i][j+1] = '@'
            return (i, j+1)
    else:
        while boxes != 0:
            matrix[i][j+boxes*2+1] = ']'
            matrix[i][j+boxes*2] = '['
            boxes -= 1
        matrix[i][j] = '.'
        matrix[i][j+1] = '@'
        return (i, j+1)
    return (i, j)

def push_up_p2(matrix, i, j, final_indexes):
    for index in range(len(final_indexes)-1, -1, -1):
        x, y = final_indexes[index]
        matrix[x-1][y] = matrix[x][y]
        matrix[x][y] = '.'
    matrix[i][j] = '.'
    matrix[i-1][j] = '@'
    return (i-1, j)

def push_down_p2(matrix, i, j, final_indexes):
    for index in range(len(final_indexes)-1, -1, -1):
        x, y = final_indexes[index]
        matrix[x+1][y] = matrix[x][y]
        matrix[x][y] = '.'
    matrix[i][j] = '.'
    matrix[i+1][j] = '@'
    return (i+1, j)

def move_p2(matrix, char, i, j):
    # move left
    if char == '<':
        boxes = 0
        for x in range(j-1, 0, -1):
            if matrix[i][x] == '[':
                boxes += 1
                continue
            if matrix[i][x] == '.':
                return push_left_p2(matrix, boxes, i, j)
            elif matrix[i][x] == '#':
                break

    # move right
    elif char == '>':
        boxes = 0
        for x in range(j+1, len(matrix[0])-1):
            if matrix[i][x] == '[':
                boxes += 1
                continue
            if matrix[i][x] == '.':
                return push_right_p2(matrix, boxes, i, j)
            elif matrix[i][x] == '#':
                break

    # move up
    elif char == '^':
        if matrix[i-1][j] == '.':
            matrix[i][j] = '.'
            matrix[i-1][j] = '@'
            return (i-1, j)
        indexes = []
        final_indexes = []
        possible = True
        # adicionar parentesis de abertura
        if matrix[i-1][j] == '#':
            return (i, j)
        elif matrix[i-1][j] == ']': # ver parentesis diretamente acima
            final_indexes.append((i-1, j))
            final_indexes.append((i-1, j-1))
        elif matrix[i-1][j] == '[':
            final_indexes.append((i-1, j))
            final_indexes.append((i-1, j+1))
        for pos in final_indexes:
            indexes.append(pos)
        # verificar todas as linhas acima
        for x in range(i-2, 0, -1):
            temp_indexes = []
            possible = True
            for (v, w) in indexes:
                if matrix[v-1][w] == '#':
                    return (i, j)
                elif matrix[v-1][w] == ']':
                    possible = False
                    temp_indexes.append((v-1, w))
                    temp_indexes.append((v-1, w-1))
                elif matrix[v-1][w] == '[':
                    possible = False
                    temp_indexes.append((v-1, w))
                    temp_indexes.append((v-1, w+1))
            indexes = set(temp_indexes)
            for pos in indexes:
                final_indexes.append(pos)
            if possible:
                return push_up_p2(matrix, i, j, final_indexes)
            
    # move down
    elif char == 'v':
        if matrix[i+1][j] == '.':
            matrix[i][j] = '.'
            matrix[i+1][j] = '@'
            return (i+1, j)
        indexes = []
        final_indexes = []
        possible = True
        # adicionar parentesis de abertura
        if matrix[i+1][j] == '#':
            return (i, j)
        elif matrix[i+1][j] == ']': # ver parentesis diretamente abaixo
            final_indexes.append((i+1, j))
            final_indexes.append((i+1, j-1))
        elif matrix[i+1][j] == '[':
            final_indexes.append((i+1, j))
            final_indexes.append((i+1, j+1))
        for pos in final_indexes:
            indexes.append(pos)
        # verificar todas as linhas abaixo
        for x in range(i+2, len(matrix)):
            temp_indexes = []
            possible = True
            for (v, w) in indexes:
                if matrix[v+1][w] == '#':
                    return (i, j)
                elif matrix[v+1][w] == ']':
                    possible = False
                    temp_indexes.append((v+1, w))
                    temp_indexes.append((v+1, w-1))
                elif matrix[v+1][w] == '[':
                    possible = False
                    temp_indexes.append((v+1, w))
                    temp_indexes.append((v+1, w+1))
            indexes = set(temp_indexes)
            for pos in indexes:
                final_indexes.append(pos)
            if possible:
                return push_down_p2(matrix, i, j, final_indexes)

    return (i, j)

def main():
    matrix_p1, matrix_p2, moves = parse_input()

    x, y = get_start(matrix_p1)
    num_moves = len(moves)
    for i in range(num_moves):
        x, y = move_p1(matrix_p1, moves[i], x, y)

    dist = 0
    for i in range(len(matrix_p1)):
        for j in range(len(matrix_p1[0])):
            if matrix_p1[i][j] == 'O':
                dist += 100*i+j
    
    print("Part 1:", dist)

    x, y = get_start(matrix_p2)
    num_moves = len(moves)
    for i in range(num_moves):
        x, y = move_p2(matrix_p2, moves[i], x, y)

    dist = 0
    for i in range(len(matrix_p2)):
        for j in range(len(matrix_p2[0])):
            if matrix_p2[i][j] == '[':
                dist += 100*i+j

    print("Part 2:", dist)

main()