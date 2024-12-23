with open("2024/Day15/input.txt", 'r') as file:
    inp = [list(line.strip()) for line in file]

matrix = []
for line in inp:
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
    matrix.append(list(string))

x, y = 0, 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '@':
            x, y = i, j
            break
    if x and y:
        break

def push_left(boxes, i, j):
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

def push_right(boxes, i, j):
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

def push_up(i, j, final_indexes):
    for index in range(len(final_indexes)-1, -1, -1):
        x, y = final_indexes[index]
        matrix[x-1][y] = matrix[x][y]
        matrix[x][y] = '.'
    matrix[i][j] = '.'
    matrix[i-1][j] = '@'
    return (i-1, j)

def push_down(i, j, final_indexes):
    for index in range(len(final_indexes)-1, -1, -1):
        x, y = final_indexes[index]
        matrix[x+1][y] = matrix[x][y]
        matrix[x][y] = '.'
    matrix[i][j] = '.'
    matrix[i+1][j] = '@'
    return (i+1, j)

def move(char, i, j):
    # move left
    if char == '<':
        boxes = 0
        for x in range(j-1, 0, -1):
            if matrix[i][x] == '[':
                boxes += 1
                continue
            if matrix[i][x] == '.':
                return push_left(boxes, i, j)
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
                return push_right(boxes, i, j)
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
                return push_up(i, j, final_indexes)
            
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
                return push_down(i, j, final_indexes)

    return (i, j)

moves = """<<>>^^>^^><>^vv>>v<^vv^^>>>^<>>v^^<>v^^><>><^v<>v>>v<<<>^v>^^v>><vvv^><<<><<><><<v<<>^>>>vv<<<^>v^<vv>v^^><><vv>^<>^^^^<><^>><^vv<<v<vv<^<^^vvv^^>><v><<>>vv^<v><v^v>><>v<<<vv><^^<^^^<^<<v<>vvv^v>>>vv^<<>>^^<<<^><<<><>>v>^<v^^v<^^^<v>^vv>>><^>^v>^^<v<<^><<<^vv<><^>^>>v^>v^^>><>^^vvv^vv<^v>>><vv>^^><>v>v>vv^v^<v<^v^v<>^^vvv><v^<>^vv><>vv<<<v<vv>vv^<v<vv>>v^^^<>^>^<<<>^v^<<v>>v^>^vv^v<>>^^<<>^<<v>^<>>><<v<^>v<>>v>^^>v<vv<^^>^v<^>>v>v^v>v<vv^<vv^^vv>^^^v^>><^><v^^<<<<v>>vv<>^>v^<<<>>><>^<^><<^<>><v<>vv><<<<<^v^<<<<><<>vv^^>vvvv<^<<v<v^<^>^v<^>^>^>>><^<>v<^v<^^^^<^><^<<<v<<<^<v^^v^>^>>v><<vv^><^v^^^<<^>v^<v<<>vv>^><<^<^<<<^>v^<vvvvv^v>v<^^<><<>^v>^<^><<^v^>^^>v^v^>^<<^<><^v>^^>^^v<^<^<^<^<vvv<>^vv<^^<^^<>v><<vv><^^^^^><><>^<>>>^><vvvv>vv^>^vv^v<v<>vvv<^<<><>^^>><v<<vv^v><^>vv<<v>>v^v><^vv>>v^><<>^^<v<><v^vv<^v^^<<vvv<<>^vv^^^>>v<>^^>v^v<<>v><<<^>^<>^v^><^><<^><<<<<^vv<v<v>^vv^^^><v<v^<v<^><<<v^v^^^v>>>v^<^v<vv>v<^<v>v<vv<><>^v>>^^>^><>>^^><^v>>><v>v>><<v>>>>v>>>>v><v>vv<v^<^>v<>v^>v>>^^^<<<
>v><^>^^vv<>v<v>v^v<>><<>><>v^>v^>><vv^v^^v>v<^^><v^v>><<>^>^^v><v>^^^^<vv^>>v>v^>>^^>^^^><<v>^^v<<<>^v>^><vv^><>^>^v>><v^>v^v<>^^<><>v^^v<><<<>><<><v>>v^>^^<^v^>^><^v<^<>^^vv<^><<v<v<>v<<v>>>^^^^>^^^>^^<>^><<vv>^^<<><v^<>>v<^v>v><>^vv>>^^^><<^>>^<>v^<><^^<>^<v<<^^<>^v<^>^>><>v^v>^^>^v>^>vv<^v<><^<^<^v^><^<>v<v^^><><<<v>vv<v<^>v<<><^>v<<>v><>>v>>><^v^>^<<>^^<>>v>v<v>^v>^<v<><v>^vv><>^>vv<^<v>^^vv^vv><^v><<>>^<><v<>vv>><^<<>><v<v>v>>vv>^v^v>vv><<v^^^^v^v><vv>v^vv^v<<>^<<>^^^v^v><<vv>><>vv^^v>^v^vvv>^<<^<^>^^>><><>v^<vv><^>>v>v^^>^>^<><v>>v>v^<<>^^^<v>v^v^><<^vv>^v><>vv^<v<^<>vvv><<<^>^^^v><^<v<><vv^<v^<<v^<^^v^<>v<<><<^>^^<>>^^vv<v<^^vvv^><<<v>^v^^<><^>><>v<<>v<^^^>>>^>v<<>v<^<v^vv^<v>>v^v^^v^>v<v>v<>v<^^>v^<><<^v^^^^v><>vv^<vvv^>^^v<^><vvv<^v>^<>>^>><<><^v^^<v^>>v>^^>>^>^<<^<^v<<<<^>>>^><vv>>^v>><v^v^>v><>^^^<v>^vv<v^><vv><>v^>vvv<<<<^v>vv^^><^^vvv>v^>v<v^^^>>^<<<v<v^vv>v>v<v>><v<^^<v>^<vvv<v^>vv<<<v^<>^<^<v>v<<>^v<<<^<><>v^v>^v><v^<<>>v<^^<v^><<^^^><><v^^v^>v>>v>v><<>^<<^v><v<<<>>>>^^
<^^v<>vv^<>v^<vv>v<>>v<>^<>^vv<v^>^^>>^>^v>^vv<<v<<<^vv^<<<<<>>v^^^^vv>>><^>>^<>^^^^<^<><<<<v<<>v<^><v><><>><<><^v<^^v>>>^v^^^^<^<>>><^^v<v<>><<>v^>><v<^>^<>v^vvv<<v<v^<^^^^>^^v><>v^><>v^<v<vvv^vv^vvvv<^v>^^<v<><^^^v<^v<^>v<<<^v^>v<^vv<>^>>v>><>^^<^>vv^^^<v<<v<>>>v<>v<v>^v<><<v<<^v<<<>>vvv<^vv^>^v^<<<<><<>v^^v>v^>><<^vvv^>>>>v<^v>v^v^<>><>^>v^><>^v^v<<vvv>^^<^<v<<<<^^v>>vv><<<<v^>>v^><<v>>><<^<^^<^>^^>>vv^<<v<><<vvv<><v<v<v^>v^>^>v^><>^<v>v>vvv^>>^>^v^><^>^<<v<>^^vvv<^<v>>^<>^<^>^^vvv>^>>v><v<^^<><v<^v><<>vv<vv<><v<<<<<^<v^<<^^v<^vv>^<<<^<^v^^>><vv^^<><<v^><>^v<<<>>>>>><^^^<v><<>>><><<>>><>vvv<vv>>v>v>^<v^v^<^><v^<v<<>><>v>^^v>>^^>>^<>v^^<<>^v^^>v^^<vv>>^vv>>>v^<vv<><<v<^^><^<v<<>><v^v<>v^^<>^<<>>^>^vv^><^v<v>>^^<<>^vv<v>^><>v<^v<>>vv>^v>vv^^>^>>v^v^v^vvv>>^^>><<^<v>><^<<v^v>^v><>v><<>v^vv^<>^<vv>>v>^>v^v>>>v^v^v><v>^v^>>>>>^>^<^v>>>v<^v<<^vv>v<v^^<^<<v^v^<<><<^v^^^<<>^^v><^^^vv^<><v<v^v>^<^^v<><^^vv><<>v^>><^^<<>^<>>v>vv^>^v>v^>v>^^^v>><^<v<v<><<^<<<<<><>^><v>v<<><^<>^<v<><vv><^>^^><<
>v>^^^v^^<>v^>>^<v>^^vvv^v<<<<>^^^v<>^>><^^^<><><>v<>^v<v<^v><<^^v^^>>vv><>><>^<v>^>><<^^^>^^v<^<^^>vv>v<^<v^<v<v<v>^^>vv<<>>><<^^>><><>^<vvv><^v<vv^v^^v<^><<v>>^>^v>>^vv^^^>v>v<^>^^<>v>^^^^^^>>>>v<>v>v>^<><v>v^<<<<<<<>>>v>^<^^>vvv<>>>^<>>v^>^^vv>^<^^^^>><<><><>>v>>>^v<v^>^<<^>>^<^^^^>v<><^<vv<>v><<<>v^vvv>^>^>v><>^^<^v><v<>v<vv<<v>v^>v^<><v<^>v>><<v^^>^^<vv<v^<vv^<>v<^vv><>v^v<v><>^<v^<v^v^<<<<<^v<v>vv^v<^<>>^><v^v<>>^>>^v><<>^^>vv>v<^>vv^^vv>v^^v^<^v^>^v>>><^><^<>^^^v><v<^v>>v<v>>v^<<^>v^vv><^<vvv^<^><>v>^>v<^<<^v^<>>v<<v>v><>^<v<<><>>^>>v<><^><<<^<<v>v>^<>><^v^>>><v>>^>vv<v>^<v<><^>^<>vv>vv^>v<<v<<>v>^v^>>vv<><<v^^v^<<v^<><><vv>^><><vvv^>^vv^^>^v<v<^v<^v<^<^<^v>v><^>>>><<>vv^^vv^v^>^><<>vvv^^><v<><<^^<v^vvvv^<>v><<<^>vv^v>>>^v^^v^<v<>vv^^^>><v<>^v>^>><v<>><vv<v^^<<v>^>^v>^v<<v><>>^^^><>>^<v<<vv^><^v<^>^vv^vvv^v>v^^^v<v^<<<v<v><^<<<^<^><^^v>^v^^><v>>^^>^><vvv>^>vv<^>^v^v^vv<<>>^v^^>vvv<<^v^>^<<>v^^^<>^>v<v<^^><<>^<vvv^vvvvvv^<^<v^^<><>v>v^^>v>^>>>^v^<v<<^v><<^<vv>vvv^v><<<>>><><<><^v
v>>>vv>^v<<<^^>^v>v<<>v<^>>>vv<v^<>^<>v>>>v<^><^v>vvv<^>><vv^v<^^<<^<v^<v<<^>>>v<<>vvv><^^^<<^<^v>>>^^v<^^^>v^>^<^<vvv>>v<^^v><>>><v^^<<^>v><<vv^>v>v>^><^>v>v>>^^^>v>^^^><v>^>>v>v<v<>v<>v<>>v<^><^<v^<<<v<<<>^v^v>>>><>v>>vvv^v<>v<>>>^^v>^^v^>>>><v<>>>^^^>><v>v<^>v>>v>vv>v^>>^v^vv>>v<v^<vv<>>v>^v^<v>v>v>^>v<v^<<v<^v^^^<>v^<>><^><<<v<vvv>>^v<vv<vvv^v^<<><^^<<^vv^<^>><v<^<v^<>^vvv><<v^>^><<^<>^>>^vv>^<^>^>v^>v<>>^vv><<><^<>^>><^>>>v<vv<>^>^vvvv><>vv^^v><^vv<<^<v>>v>>>^><<^^v>>><<<<<^>vv>>>^>>vv^vvv^<^^<<>>v>^>>vv>^<>^v<^^>v<<vv^>^vvv^<<v><^>^v>^vv>v<^^^vvv^^<^v<<><><><<vv><vv<^vv^v^v>vv<>^>><<^v><^>vvv<^<^v<vv^v>^><><><>>v<^<><<^v<v<^>v<v^^^>>v<^v>v^^v><^v><v>v><>^^v>>v^^>v<<^<^^>^^><^^>^<^<v^v^><^>v>v>v<vvv>v>><v^v>^^<v<<^<<v^>v><>v>^<<><>v>v<vv^v>vvvv^<v^><v<<^>>><^><vv^<<v<v^<v^v>>^^^^^v>>v<<vv^v^>v>^^<<<^>v^<^v>^vv^vv<>>v>^<><^><^v^<><>><^><^vvv^<vvvv><^>v<<v>vv^<^<>v<>^><<^vv<v>^>^^<<^<<<^v<>>><><<^<^^v^^vvvv^><<>><v>^<>><>^v>>v<vvvv^>v^^vv><vv>v^<vv><^^><v^v>^<^><>v^v^v<>^v^<<v<v^>>v
vvv>>v^<<v^^^^>^v^^<>>vv>vv>^v<>vvvv^<^^<^^^<<^<>v^><^v^>>v^^v<>^v<vv>v<>>^v^^>>^^<<v<v^^vv<<v^^<v^<v><>vv<^<><<><v^>^v<^>vv^<^v^<vv><v<v^><v^vv^>v<^v^^>^vv^^><>>>^v<>^<<v<^<^>>v>^v<^^^^>><>v^<^v<<>^>^^><<^vvv<v>>^^v^^^v<^v^^>>vv<<<v<><^v<<<><^<>>v<^>^vv^<>vv>>^><>vv>^v<>^>^v<^><<><<^v^><>>v^>^^vvv>>vv<>^<>>v<v<v^v<<>^^^v<^vv^v><v^>>>>^v^<<v>^>^vvv><>v><>>v^<^>^^<v>>^<>^^>^^<<^<<>^>^^^><<<^>^^v<<^>^^<>v>^><v^<<v<vv>>>^<^>>v^<<><^><v^vv>>^<v<<v<>><v<>^<^v^<>v>^vv<><<v>v<<>^<<vv<v<>v^<vv<^>><v<><>v<>>>^><>>vvv^vv<v>^^<<^<^^>>v^<>^^v>v><^>^^vvv>^<>^^>>v^^><vv<>v>v><<^^<>v>>v>^>>vv^^^>>^v<v<<>^^>>^v<<^>v^v>^^<<>v<<^^^<v>v<<>>vv<<<>><^^^v><<>^>>><v^v<v>v^>^v<vv>v>^^vv^^^^^><v<vv^^><^^v^<^>^v^><<<^^vv^^<><v<^>v^>v^v<>>v^<<<v>^<v>^><>^>>^vv<v>^^^<v^>^><>>>^^<v^^>^<v^>>^v<<<vvv<^vv<<v<v<^<>v<v<v>^><><^v^<<<<^<v<<v<<^<>vv>^<<>vv<v^^v<^v<v>v<v<><v<^vv<<<<>v^v^^>>v<^^^<>v<<vv^<>><vvv>^v>>^><>>v>^v^>^v^v^<<^<<v<v<^^vv^v>^<^v>>>>^^<vvvvv<^>vv^^^<v>v^^v^vv^<^<<>v<^^>>^vvv^^>>v<<v^>v^^^v<v<v^<><<<v^^
>>>v<><>v^^>v<<<>^^vv>v<v>>>>v>vv<>v<<>>vv^<^>^v>^v>v^v^vv>>^>v^^>vvv^^<><vvv><v<>v<^v>v^><>>>><v^>>vv>vv><^^^>^>^>^v<><^><^^>^v<^<><^>><v^^<<>vv><^><>vv>>>^v^>^vvv<<<vv><>vv<^^^>v<><><<><^<><^><^<^>v>vv<v>^<<^>^^v<^><vv^v><^v^^vv<^v>vv^vv<vvv><vvv^>>v^^vvvv<v><<v^>v^<^^^^v>>vv^>v<vvvv^^<vvvv^vv^^v<><vvv<>^^<^<vv^>>>v^>vvv<<^>v>vvvv^^>>^v>><v<^<><^>v^^^>^^^^v^>>v><<v>>v^v^v>><vv<^^^<v^v><^v>^^>v>>^<<vvv<^^v<<^v>>v^v^<vv<<>v^>v<><<v>v>v<>^^v<<<^>^^<^v<><v<v^v>^^><^>^^v^^<>>vv>>v^v<^^>v>^>>v^^v<vvv^>^^<^vvv><^<>><<vv<v^>>v<v>>>>v^^<v<<<v>^v>^<v>><<<^<>vv^<><v^<<>>>v<^^v>^v^v<<^vvv^>vv>^<<<<^^>><<>vv<<>^^>vv<v^<^<<v^v^<<>^^^<v^<><^<>v>>>v^^v>>>vv>>vvv<>^^>>v<^><vv^><><<<v^v<<<v<>^^<<>>>v^^>>>>^^^><^vv^v<v>vv>>>^>v^<v^>^<>><<<v><><v<^>v>^>>v^><^<<><<^^v>v><>^^><v^<^>^vv>><^v<<<<vvv<<^>v^v>vv>vv^><^^<<>>>^^>v^>^<<><^^>><<<^>v<<^>^v<><v>^<>^<<^^<<^^^>v^>^^>^><<>v^v>^^>>vv>^><v^<vv<v>v<^<>v>v<<><^^<^>vv<>vv<^<>^>v>>^<>^vv<^vv^>v^v<<v<v>v^^v<<vvvv<v><>^v<>>^vvvv<>v<>>^<><<v>><vv<vv^<>><>^>^^^^
^^<^<><>^v<<v>^vv><vv<><vv>^vv<>v<<><vv<v>vvv>^<v>^<>^^<^<>>v<^>^<vv^v^>v^<<^<v<^<^>^<v<>>v>>^v<v^>^><v>>v^><v<<><<>v^>^<<^<v<<><>^v>^<^^<v<<<v<v^^^^^vvv<^<<v<<<>vv<<>v>^<v>v<<<><<<>^^v<^<^<>v><^<vv>^^<vv<><>^<>><^>><vv>^^>vvv^>>>vv><><vv^<<<^^v<<>vvvv^^><>>^^<vv<^v><<>v><^^v<^><v<^<>><>v^v<<<>^>>><v<<vv<^><^^^^^>vv><^>vv<vv<<>><<<<<v<<^>>v>v<vvvv>>v^v>v>^>vv>v<v><v<^v^v>><^<><^v^v<^>>vv^^><^<v><^>>><vv><v>^^v^v>^^<<^^><^^^v<<<^><v^<^<>v^v<^>v<v>^<>><<vvv<>v^vv^<v<^vv^<v><<><v<><<^<^vv<><v>^v>><><>^^v>^v<<^<>^><vv^<v<^v^<<^^<>>v>v>^^<vv<v><^^><^^<<v<>vvv^><^^^<<^><<<<<>^><>^>v^vv>>>v<v>v<<^>>><<^>^^v>^^^^<^^<>^<>^^<>>><^^<><^>>>^>>^^<>v<<v>^><<^vvvv<<<^<^vv^v<<>>^^<<v>vv>^<^^>>^^v>^>><<<v^<^>^><>v><<<<v>v<vv<v><<><>vv<<><v^^v^v<^vv<v>^v>^<^><>vvv<<^>>>>^v>v^v<><^><><<^vv^>vv>^<^^<vvv<v><^<<<v<vvv^v>^>v>>><^<vv<v>>>>v<>^^^<<><<^^>><>^>>v<v^^<<vv><>vv<v^^<v>^<^^vv<^>vvvv<^>v<<<^<>vv<><<<>><<^<<vv<v^^>v^vv<<>>>vv^>^^<<>^>v><v>>^^^^^>^vvv<^>^v^^^v><v><^<>v^v>>^^<><^<>>v^^^<vvv^v>^^<>^<v>>>
v<<<^<v<^><^v^<v^<v^<^>v^^<>^<<>^>^>v>v^v<^<>^^vv<<vvv>v<<^v<>v>v>vv>>^v<<v<>^v<<><^v>^<<>>^<>^>vv^<^v<<>^>>^v>>v^^v><<<>>^<^<vv>v<<>^v>^v<^vv^vv<>><<^>^><^^v<^<v^>>^>>>>^^v^^^^<<^<><<^v<^^^v><v<^><^^<v<^>^><^^^v<><v><<<<<vvv^>v>>>v><v<^>v<<v><^>v><>v>^vv<<v^^^<<v<<v^v^>^^>v<v>>>^><^<v>v<>>><>v^>^<^v^vv<<>>^>>v<<v^^v^^><v^><^v<v^>v^^^^>v<<v^>>>^<<v>^^<v<v^<<><>vvv<>^vv>>>>^v^<<^<v^<^^v^<^v>v>^<vv><>>v><v^<^^^>>^>>>^>v<><>v<<vv<>^<<<v<vv<^><<>v><>>>v<v<^v>vv>vv^>^^<^>>v>^><^<v^>^^<^^<>><>^>v><<<^vv^v<v<^^^^>^<^^vvv<<<^>v^>>v<v^><>v^<>^>>v>>vv>><><^>>>>v<>^^>^vv^<<<^>><v^><<v<<v>v><><^v<<<^vvvvv<^>><^v<v^v^^<vv^^><<><^^^<<v^v^><^^<>>>^v<<^v^><><^<^^v>>^^>>v^vv<v<><^vvv><>v^<^v^^^<^v>v<^>v^<<<v^><>v><v>^v>^><v<><^v<v>^>v<^<<<><vv^>vv>vv^^^>>v<>>>>^><^v<v<^vv>^^^^^^>><>^>><<<>>>v>vvv^<<<<^>^<^^^v>>vv>^<>v><<>>^v<^<^^^^vv^>^v<<>^v^<>v<>>>^v>^^<<v><v^>^>v<>vv<v<v^v<vv^^^v>><v^>^v<^>v<<<vv>><^<^<v>><vv<v^>v^><<<>v^v<<><^<<^^>^^vv>^^^>v><>^<>^><>^<<<<<>>v^v>^^<><<^v>>^v>><^<<^^v^<^>^^vvv<>vvv>
>v<>><v<<><^v<v>>^<^<v<vv^<vv><^<v>^v<<><^vvv<v^v^v>><>>v^^>><^^vv<^^vvvv>^<>>v<>^>^>^>^<>^v^v>>v>v^v<<^<^<>>v><vvv><^>>v^^vv>^>>^<v>v<^>^v><^^>vv^><><>>^^vvv<>^<<vvv>^^^v>vv>v>^><><<v>v^<><<<^>>v^<><^<<v^>vv^vv>vv^>^^<<v>^vv^^vv<<<<<^^>^^><<v>v>v><v<<vv>^^<>>v>^^<v><<v>>>>>vv>>>v<>^^^^v^<^>^<<vv><<v><^vv^^v<vvv^>>>v><vv<^v><>vv>><^>><>^vvv^>^>^>^>^<^^>^>^v<<^>>^<v<>^><v>^v><<>v^<v>v<^>^>>>^><>>v^>><^^>v^^>^<>^^vvv^v^>^>^>v<^^v>vv>^<<^v><v<<<v^>>^>^<^>>>>vv>^^^vvv>v>>><<<vv>^>^>v>^v>v^^^^vv<^v<<^><v><>^<<<v>><^>^^^>^^vvv^vv<v><^v^<<^<><^v>>v<<><<>^><<v^v^v<<^>^>><>>v<v^<<^^v>vv^<v<v<<v^v>v><v<v<vvvv<v<>^><<<vv<v<v^^<v<>^>v^><<>>v>v<v^<>^v^<>^^v^v><v<<^<<v>^vv<v<<^v^^><<<<>v^v^v<v^<^^vv>>^><><<<<v<v^<><^v^>v^>><>v^^^>><<<<<v<v^v>v>>v^>^<^^>>^^v^>v^v<>>^^^v^>vv<v^v<vv<vvv><>>^^^v^>v<^<><v<>vv>>><><<<<>><<^>v>>><^<^<>>v>vv><<^v><<v>^^v>v<^v><>^<>^>^><^>v<vvv<<>v<v>><<^v><><<>v><><v<><<><><v<>>^^^v>>>>^>>><<><>^v>^^^v>^>^<v>v<><v>^^vv>vv<<vv>v^<<><><^>>^vv>^>>>>^<^<^v^<<v<v><v^><v<>^^<><<<
vv><v<^v^^<^<^^^<><^>>^<v>v<<v>^<^>v^>v^v>>^^>>>v^<v<^v><^><^<^v>vv>vv<^^<^>v><<^^><v^v<^vv><<><v^<>v^^v<>>^>vv>vv<vvvv^<v^^<v><<><vvv><<v>^<<<>>>>>^v<><^^^>v^^^><<v<v^^v^^>^v<^^>^v^<v>>>v><>^><>><v^v^vv<v>^^>^^>vvvv<^<^^<<^^><><^^>^v^<<<^v<vv<><^^^vvv><v<>>^>>^>><>v><^^<v<^>^^^^v<>v<v<v<<^<^<v><^v^v<><<v<<><vv^^^<vvv^<^^<>>^<^>>vv>^><vvv^v>v<^^<>^<>^<><<<^vv>v^<<<^>v>^^v<^vv>v^vvv<<vvv<v><<vv><<>v>^vvv^^><v^v<^v>v^<><^<><vv><^v<v><>vv>>v^><<><^^>>vv>^>v^>>v<^v^^^><>vv<<v^v>>>><v^<><<^<v<>vv^<v^^>>^>^^>^^><^>v<vv>>v<<v<>^<<v>>^vv^^>v><^vv>^v><<^^>>>v^^^<^v<>>v<>>v><vv<v<^><^<^<^^v<^vv^vvv<^<><<<v<^^<v^^><^><<^^>^><><>>v<<<^<^v^<^v>>><<^>v>^<^<<<v>v^<>^<<><<^<>^^<v><>>^>vvv>vv^<v>>^^v<v^>^^v>>vvv>^>>><>><vv>><^>>>>v^v<v^^v>v^v<vv>>vv<>>v^^v^vv>>^v<v^><><><^^v><>^^>v<>^vv<v<v>v<>^v>><>^<>><>><><>^<>v<vvvv^v<v^><^^>>vv>vv<^^>^v^<^^<<><>^^<v<^>>>>>v>vvvvv<^^^<<><vvv><<<<>^<v<v<^<^^<>vv>vv^vv>vv^>^v>^<>^^vv<<>^><^^^><v^>v>^<<<^<v^^>v^>^<<v^^<<vv^<<v<<<>v<<>^v<<<<>^<vvv<<^^>>v^>><^v>>v<^>>^v
>><^><v><^>^v^^<<<<>^^v<><vv^v<<<><<<^v<v><^v>vv><^v><vv<v<vv><<<^>vv^<v^>v>^^<<>^>v^<<^^^><v><^^^^^^^^^v>>^>^<<v>>^><<<<vv^<<>^<>>>^v>^<><<^^>><v^><>><^^<^vv<<^>v<>v<><>^<^<>^>><^<><v<<^v<<<^v^>^vv>v<v<<<>v<v<v<^><v^^>v>>>^<^^<v<^v^v>>><v<vv^<^^v>vvvv<>vv<>v>>^>>v>^>vv^^<<><>>><>^v<^^vvv^^<><^>v^>><<>v<^>v^^>^^^v>><vvv^^v<><v<>>>>^vv^^v^v>^v<>>v>^vv>><^v>^^<v<<<<^^v>>^^vv>v><v<>vv<v><><<>v><^>v^^^<<<<><>^^>^v>vv>>^<>v><>>^^^^><><>>>>><>^v^<^>>vv^>vv>vv>v>^vv^v><>v<<v^>>vv^v>>vv<>>^v>^<<<v^>^vv>>vvv^<>>vv<v><<v^^v<>v<<<v>>^^>^v^^>^>^<<^vv>>^^<<v^^vv<<v<v<^><>^v<<>vv><<vv>^v<^v><>>^^^>><<<>^>^<<<><>><>>v<>vv^>^>^<>^v>^v^<><^><vv^^v^<<<<v>>><v^<<>^v>v<^>>><^v>^>>^v>^vv<><^>>^v>^^^v>v^^>^>>^^v^vvv<><<^vvv>^^v^>>v^^^v><^<v<^>v^v<><vv>>v<v^^<<><^<^<^^><><<v^v^^^v^v>^>^^<^v>>>><v<^>v>^>^>v<^>v<^<v^>^^>>vv>v^<v>v<>^>>v^<v<^>>><<^<^<v<^^>v<^<<><>v^v<>^<>v>v>>v<<v>>^>>>vvv><>v>^<v^^vv^^^>^<>vv>vv>><^><^><><>v^>^v^^<^>v<<^v<<v<<>>><^^<<>^<>vv<<vv>><<^<v><v><<v>>v^^<><vv>v><^>v>>>>>^^>^>v>v<^v^>^
^<>v>^vv<vv<><^>>v><^<v<^>>><<^^>^^>^<^>>^>^>><<>v<vv><^^>>^><<^<>v>v^<>^>>v><v><><<>^v^v^^<<>^<^>>v>>^vv>vv^<<^>>>^>v<^^>><>>v^vvv^>^^>>v^v>^v^<^<v>^v><><v^^><<^v^>^<^><>vvvvv>>>>v><^<^<<vv>>^<>^><>^^<^><v<>vv^<>>v<vv<>^<<^v^^>v^^^><<v>v<^^^^^v>v<^^v>^<<^<^>>v^^^v^^v^>v^vv>v>>^^v><v^v>vvvv<>><<<>v<>^vvv<v>v<^<vvvv^v^><v<v<<^v>>^^v<v^^><^vv<<^><v<v^>>v<^>^^v^v^v<<>>v<<^^^v<><vv<<^v<v><<>^v<v<^^<vv^>^><^<v<>v>>>v<<^<<>^^^>vv>^<>>><<v^>>>>>>vv^^<<<^<vv^>vv>v>v^v>^^<^><><^^v^^>^<v>><>><v>vv>^<^vv>>^v^v<^<^>><>^v^>vv>v>vv^>>v<>>vv<>^^<^<^^^^>^vv><v<v><^<v<^>>><v>><^<v<<>^^<vv<v^<^<vvv<v><<>>^v>v^^<>^<v>^v>><^v>^v<^>>>>>^<>>v^vvvv><<>^<v><<><^vv^vv^>vv^vv<>^v^<^<^>v^^<^v>>><<^<<^^<^v><<<<<v><>^v^vv^^><v^<<>><^v<><v^>vv<<>vv<<v>^v<>>v<<vv<<>^v<v>>vvv<<<^>^^<>><^v<>vv^v>>^^v<^<v<v^^<>>>v^<v>>vv<^^>>>><<><^<^v<<><^<^>>>^<>v<v>><>^^>v>vv^<>^^^vv<^<v>^>v^^<>v^><<^<<><^^^v<v^^<^><<vv<v>^>v><^<^>^v<v^v<^><^><>^v><^^^^<^vv<>>><v<vv^><>^>^vv<>v>v>>^v>^^<>>^<><<v<<^<<^vvv>>>v^>v>^>^^>>v<<>v<<><^^vv<<
<<^<>>v^^<^^vv^>v<>><vv<>vvv<^^>^><vv<<vv>v<<<<<>>><<><>^>v>^^v<v><<<^><><>^v>><v^>>>>^>vv<<>v><<><^^<>vv<<>>>^>^<<^v>><^<v^^^^<v<v^<^>^vvv<^v>v^<^<<^^^v<>v^><v>^v^v^vv^>v<v>>v>>><v<^^v<^<><v^><<<vv><^><>>^><^vv^>v^><^v><^^>^^<<v^<><<^v<v<>v^^>v^<<^<v<<^v<><v<<^v<<^>^<>v^<>^v^^<>><vv<v<v^^v^>v>><>^^v^><<<^<<>vv<^v>v^^^<^>^<>>>^^^>>^^<><v><^><<<>><>v<vv><v>^<<>^>^><>^<<^><v^><<<><<^vv>^^^<vv>^^<><vv>><<v<<>v>vvv^^>vv>>vv>><<^<v^<<vv<v<v^^><>><v>^>>>^><><>>>^<<^vv<>^^^>>v^<>^^<^v>>vv^<<v>^vv^^>v><><>^^^<vv^<<v^>v^<v^v^v^^<^>^<v>v^<<v<v>>v>>><><v>v<vv<v<v<<<v><>><vvvvv<<v>^^>>^>>>^^^>^^v><^^>>><^v^^v>>>^v^v>>v<^><^>>><>v><v^v><^<>^v>v<^^^>^^^^vvvv<v^^<^<^<>v^v<^v>>v>><v<>^v>^>vv^^^>>^>^^^^<><v>^^>v^>><^>^<>><^^>vv^<><v<^^^<<<v>vv<<<<<>v><^>^^>>^v<<^^<^v^>>>v^><>v^><>>>^v^>>>^^<<>^<^vv>^<>^^>><^><^^>vv>><<^>>vv><^v>><^>v^^^^^>^<v<>><>>v^vvv^>^<^^^<vv<v<^>>><<>^^>v>vv>^><<v<^<>v^<^>v<^>>>^^^<^^<<^><vv<>v<v^vvv<vv<>>^<v^v>v<><<<^>v>>><<<^v<^^>^<>><><<v^>>^v><^><v<>v>v<^^vv^^vv^>vv<<vv^<>^v>v
^<>>v<vv>v>>>^>^^<^>>>vvv>><<^v<^v<^<<<>v><>^^<<^>^^v>v<><^><>^v>^v^^>v^<^^vv<><^v<>>^<v^^v><<<><^v^vv><<v^<v<vv^><<^>>^><>>>v>^><>^^v^>^^v^<<v<^<vvv<^>^>^v<>v^v^v^^<>^>v^^<><v^<<<^^>v^^v<>>^>vv^<<^v^><^v^<><^<>^<v<v<v^><^^>vvv^^^^^<<v>><><>>vv^^>^^><^<>^>^vv<>vv<<<^v<v^<^^><>vv<>>^>v>^>^^>^>^<v<<>v^v^<v^<^^<<>^><<><>>^^^>^>>v>^^>>v<<>^<<<^^<^v<^<<v^<v<^>>^<^<v<^v<>v<v<>v<>v>v>^>v<^<><^^v^^vv^<><>^<<<<><<<>v<^<vv^v<vvv<><<^^v^^<^v^^v<<<><<v>^<<<>^^>v>><v><v<^^vvv><<^^>^<^>^^vv<><<v^>^v<><<^^>v<^^>^^^v<^v^>v^v<v>^<<^^^v<><^><<<<^><><v<^>^^<<>><v<^<^<v<<^v>>^v>v<<<v<<<<^><^><^<<><^><v^^<<>><^^vv<^^v><<v^v<^v<^><>^>^<<>^>>vv<<^^^v<<>vv<vvv><^>v>^vv>vvv^>>v<<>>v<<v^^v>>v^<vvv<v>>>^>v<v>vv^^^^><v>><vvv>>><^>v<><>>><<^>v^<vv>>v^v><<<><v^>>>vv^<<<<v<^^vv><><^><>v^><^>>^<v>>^<^^>^>>^><<v<vv^v>vvv<>v<>v<>vv^>>^<<>v^vv<^^<<^<^<>^<v>^>><<>v>^>v<>v^>>v^<^v>>v>^^><^<^^<v^>><^^>>^^><>><<v>^v^^<^<^>><v<<v<<^^<^<v<<<<^v>>>v<v<>>>>>>vvv^>>v^>^>>v<vv<v<><^v>>>v<^>>><>^vvv>^v^vvv^<^^^><<<>vv><<v^<><^>>v>
><>^vvv<^^^<>>>^>>>><v>>v<v^v^>^vvv^<^v^<vv>^>^^>v><^<><^>^v^^<v<^<vv^<><><><v<^v>^v^<v>^^<^^>v^<^vv^<>^^><^^<>v<<^vv<>v<<v<^><^>^^>^^vv<<>>vv^v><^^vv>v<<v^v>^<v>>>v<>vvv>^v^^v^<v<<^<^v^<v^^<<^>^v^^><<>^^<v<v^><^vv>v><>>>v>><<^vv^^^^vv<v><<><v<<v<^^^>^v^><^v^^^vv<^<v>v^^><^>^^vv^>>^<^vv<v><^^v>^v^><<>v<v^^<^^v^^^v>vv<>v<><<^v>>><>>>vv^<v^^^<^>>v<><<<><<<<>^<<>^v^<^v><>v>>>>^v>>^<^<<>>vv^<<^<<^v>v<v>vv^v>>^vv^v^^v^<^<>>>^<>><^v^>>^v^<<>^v<^<<<>vv<<^<>^^v^^<<<<><>>v><<^<<<^^>^^>>v^v<^<><vv>>vv^v>v>^>^v>v>^>>^>^<>><v^>><<>>^v^><vvv^<v^v^^><<^>>^v<<^^v^><<v<vvv^<v><v<<><vv>>v><v<<<<v<<^vvvvv><^^^vv^>>^^<<<^<^v^^^v>^>>v<^^v>vv<<^>v<>v<^<<>>v^<v<v<^>^^^vv><><><><^^v<>>^<>vv><>>v<^vv<^<>v>>><^>v>v^><>>>^v>>v^^>v>^><><><v<>v^^><^^^>^<><><vv><v^<^^^v>>vv<><<>^v<<^<^<<^v<<^v^>^<<<^<^^><^^<<v<^>><vv><<<><v<<^><>^>>v<>v<><>^>vvv>^>>^vv><v>^^^v<<<>>>v<^<>v<^<<>v<v^<^>^<<^<>^v<>>v<v^<<<<<v<>^>v^^<v>vvv^<^^>>v>^vv^v>>>^<^vv><v<^><<>><^<>^v><<><><^<^v^>>>vv^^><^>^^v<^>><^><v>>v^v^<<<>><vv<v^v^v^<vv>^^
^^v^>^<^vv><>vv>^>^>^><>>^v<>v>v^>^vv<^>>>v>v>^<^>v>^>^<^<<<>vv<vv^>^v<v^^>^^v<>^v^<><^^v^v>v>v><<<^<^v^v<^^<<>v<>^vv<>v<>^^>^<<^v<v^v^^^<v<<<v<^<><^>>>^^v<>><vv><<<<>v>^<>^>^>>v<^v<>^>>>><>v><<^<^<v^v<^^^>>><<v^<<><<^^>v^<vv>v^v>v^^^<>v<^>^v^^^<<<>><>>^>>>>vvv<<>v^^^^<><^<<<^>v^<vv>><v><^>v>^v^^^v^v^>^vvvv<>v^><><vv^<<<^>>>^<^<^>><^^v^^<>^<v<<>><>>^v>>^v<<^<^^v^vv<^<<>vv>vvv>>v<<vvv<^^>v^v^v>>vv^v>vv^v^^<vv>v^v^^>v<>v<v<v>>^>>^<>^^><^^^vv>><v<v^<<<>v^v^>v>>v^<<^^^^<v>><v^v^vv><<v>^^^v^<<v<>^vvv^^<><<^>v^^<>>^v<^v^<v<^<>v>^vvvv^v^><><>><<<>vv<v<>^><v<^vv><^v<<vv^v^^^v<v><>>v<>^<^vvv<>v<>^v^><<><>v<v<v>>^vv>v>>v<><^<^^<vv<^<v>>>>v<v^v^>v>><<vv<<^^vv>^><v>vv>v<<v^>>^<><v^v^<<>v^v<>vv<vv^vv<^<><v^>^>^><v<>>v^^<<^>vv^><^><<v^<><^^<v>v>v^<>vv<<<<><v^vvv>><<<>v><<^vv^>^vv<<vv<>><^>vvv>^<<<>^><v^><^<v<^v>>>vv>^><<^>>>vvv^^^^^<vv>v>v^v<vv^<v^>^>^v>>vvv>v>><<<>vv>v<^^vv>>^vvvv<<>^v><^<^^<<<v^^^>v<v<>^<<>^<<v^^^<v<v^vv^vv^v^^v<vv>^<>^v^><>v>^v>>>v^v<><><>vv<v^<><<^<^><^v<<^<>^^^<><^<<<<^v^<>^<^^
^v>v><v><>v>^v<<^v>^>><^^<v^><v<v<^<vvvv<<vv^><<vv<<><<v^v<<>vv^<>v>><<<><^>^><v<v<<<<>>>^^>^^^v>v^<>^^<>>v><v>v>><>v>^^v>^>v^>^>^<v>>^><vvvv<<^><v<vv^><><v^^<<vv<vvv<<><>^<<^vvv>v<^vv<v><<<v><v<<><<v^^vv^v><>><^<^^v^<>v>>^^v^>><<<^<<v<>vvv><^<v<>v^^<<^vv<>^v^^^>^>v><^vv^>v^^^v>^v><<>vv<><<^^>>^>^^^vv<v<<^vv^<<>v^^^v^^><><v<<>>^>v^<<v^<^><^v>vv>v^>^><^v>v<^v>>v<<v^<^>>^v^^vvv^>v<<v>v^><<>^<v>^^^>^^<<>^vv^v^^>>^v<vvv><v<>^>>><><<^v^><vv^v^^>vv<v<^>v<<<^v^^vv<<<<><>><v<^<>><><^<<^^>><v^^v^v<v^<>vvv^^v^<><>><<^<^vv^>^<>^<^^<v><v<^v<^>><^v>>>>vv^^v^<<<^>>^>>>^><<vv^v>^<>>v<^v<v^<>v<vvvv<>>^><>v><^<>>v><><>>^v<^<^<>^v^>^<<v^^>v<>>>v^>v><v<<>>^><<^>^^v>>>^<^<v^>^>><>>^v<v^<<^^v<^>v>^<<v<v^v<><v>v^v^v<<<^^^v>^<<<v<>v<v>>v>^^<vv<>^>^<v^^^v<>v>v<^^^^^^^^^^>v<^>>><vvv^vv<>v<^^^^>>>>^<<^v<<<>>>v<<>>^<<^<<<v>v>>>^<<vvvv<<v><<v><<^>v^^^v^>vv<^<v^^><<<^vv><>^v^>vv><<^v>^>v><<>v^^v><^^^<>vvv>v>^vv^><>><<^<^v^>^^>v<><^v<vvv^^>^vv^<>><<><<^<>v>^><<v><vvv<><>v<v<v^>v<v^^><^^>vv>v><^><v<<><v^<>><<<<v>v>^
<v^^<<>>>><>>v>^<v^v>^v>><^>^v><<<v<<^^v>^^<>>^^v^><v^^^^^^>^^>v^^<v><><<^^v^>^v<<<<v>^><<>v>>vvv<v>^>>v<>v^^v><^<v>^^<v>v^>v^v^^vv<v^<vvv^^^^^^v<<^^vv<v^^>^v>>^^^^^<^v>v<v><><<<vvv>^^<^^v<>>>^>^>v><><vvv^<>v^vv>^^><>v^>^>^^>>vv^>v>v^^>vv<<>^<<v<><<<>><v>>>>^<><^<<<^^v^^^>v<><^<><^<v^^^>^<^^>v<vv<>><v^v>><>>v<^<^>^>v<v<^>>vvv<v<>^^<^v^>v<>><><<<vvv><^^<>^<<>v^>^^><<v^<^^^><><v^>v<<^<><<v>vv<v<^^>>>^><<v<^<<>v<v<<v<<^>><>>><>>^<<v>>v><>v><>^v>^<vvv^^^v^v>v<^^<^v>v><v<>^^>^<<^>vv<>^^><^^<^^v<v<^v>v^vv><vv<^v^>v<v^>><v^^^><<^>>^^v^<^^v^<<<^<^^<^v<vv>^>^>v^^^^>^<<v<<<v<>^<v<v^^><v^^v^<>^>>v<<v<>>>>>>^<^v^>^<vv><^vv<vvv<^<<v<>>v^v<^^^v<^<v<>v<>v><v>^^<<v>^><<<><v>><>v>>><>^<^<^<v>>>><<<v^^^<<<v><v>v^v^vvv>^>^<<>v^<v<^>^>><<>v<>v<v>^^vvv<v>v^v<v<>^>v^v^>>>v>^v>v<<>v><<v^v><v^<^v^>>^<v><v><><<^><v^>^<>^>>^v^v<^^><>^>^v>>vvv<<><><>><>v^>v<vv<>v>><v>v><<<^v>>vvv><^^^>>^v^<v>^^<><v>v^^>v^v^^v^^>^<v^<^^^vvv^vv>^<vv<^v><^^<<>^>><v>>>^><<^v>v<>^v<v^>>^v<^^v^v>v<^><<^<v>^v<<v^<<^>vv<<<v^^><>v^><v^<<
<<>>v>>vv>>v<^><>^v^^><v<^>v^^<vv^v><vv>^<^vv>^>>^^<<vvvv<v^v^>^^>v<vvv<v^v<^>v>v<<<><vv<<>^^><><>vv>v>>><<vvv^>v<><v<>^v>>^^v>^v>><<<>><<<<<>v^>>^v<>v<><>v<>^<<^vv<>^vv^>v^^<^<<vv^^v>>>>v<^>v>><vv^v<><>vv^>><<><<^^>^^vv^^^v<v<><^^^v>^>><v^^^>v<vvvv<^>><<vvv<<<v^^>vv<<^vv<v<v<<><<^<^^>>v<>>v><>^v>v^^><<v<^^>v<^>vv>v<>>>>>v<<>^v>><v^^vvvvv<v>v<>^vv^^<<>>>>^v>^v>^>^^^v><^^>^^v^>>>><>v^><>^v<<>v^^<^>^><<>>v><v^^v><><>v<^>>>^v<v<>>>v^v>v<v^^^><<vvv>>><>v^v><^<><<<^vv<<>v<^<v>v<><^v<>><v>><<^^v>v><vv^><>>^^<^v<<<^v<<>v<<>^<v>>^vv^><vv>>vv<v<^<<<>^>v><^>^^><^^>>>>v>><^v<vvv^vv>^vvvv>^<<>>>v>^<v^>^<^<v><<^^^^^vv<vv^^^<v^>>vv>>vvv^v>^^^<<vv><^>>^^^>v^v^<^><^<v<^v^^^^v<v>>v>>><^^>^<<><<^><><<v>v<>^^^<><^^<>>vv^<>^<<<<v<v<vv><<><<^v^v^v<>>v><<^^<<><^>>v^v^^vv>^^v^vv<v>>v>^^>^>^^<v<>>^>>^<<^<>v>>vvv<<v<<v<<<<<>^>^v^^^<<vv<<>^><>^v<vv^><^><^><v<>v<><^^<>v^v^v<v^^<<>>><v><><>v>>>><^vv^vv<^<<^<v><<vv<v>>^vvv<^>^^>v<><>>^<vv^^v^><^<v><<>^>^<v^>vv<<^vv^v^<<vv>v><><^v>v^v^>vv>><v>vv>>v<<><v<>^<<>^^^<v^"""

moves = list(moves)
num_moves = len(moves)
for i in range(num_moves):
    x, y = move(moves[i], x, y)

# with open('Day 15/test.out', 'w') as out:
#     for line in matrix:
#         for char in line:
#             out.write(char)
#         out.write('\n')

dist = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '[':
            dist += 100*i+j

print(dist)