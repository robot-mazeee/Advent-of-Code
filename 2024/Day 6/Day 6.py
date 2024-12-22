with open("Day 6/input.txt", 'r') as file:
    matrix = [list(line.strip()) for line in file]

direction = 'up'

start_x = None
start_y = None
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            found = True
            start_x = i
            start_y = j
            break
    if found:
        break

def print_matrix():
    string = ''
    for line in matrix:
        for char in line:
            string += char
        string += '\n'
    print(string)

def walk(direction, x, y):
    while True:
        if direction == 'up':
            if x-1 < 0:
                return
            while matrix[x-1][y] != '#':
                x -= 1
                matrix[x][y] = 'X'
                if x-1 < 0:
                    return
            direction = 'right'
            
        if direction == 'down':
            if x+1 >= len(matrix):
                return
            while matrix[x+1][y] != '#':
                x += 1
                matrix[x][y] = 'X'
                if x+1 >= len(matrix):
                    return
            direction = 'left'
            
        if direction == 'right':
            if y+1 >= len(matrix[0]):
                return
            while matrix[x][y+1] != '#':
                y += 1
                matrix[x][y] = 'X'
                if y+1 >= len(matrix[0]):
                    return
            direction = 'down'

        if direction == 'left':
            if y-1 < 0:
                return
            while matrix[x][y-1] != '#':
                y -= 1
                matrix[x][y] = 'X'
                if y-1 < 0:
                    return
            direction = 'up'
            
walk(direction, start_x, start_y)

def check_visted_direction(x, y, visited):
    if (x, y) not in visited.keys():
        return False
    
    visited_dirs = []
    for direction in visited[(x, y)]:
        if direction in visited_dirs:
            return True
        visited_dirs.append(direction)
        
    return False

def check_cycle(x, y):
    # começar a andar desde o inicio. V
    # se passamos por um vertice ja visitado com a mesma direção
    # temos um ciclo
    direction = 'up'
    visited = {(x, y): [direction]}
    # print(visited)

    while True:
        if direction == 'up':
            if x-1 < 0:
                return False
            while matrix[x-1][y] != '#':
                x -= 1
                if (x, y) in visited.keys():
                    visited[(x, y)].append(direction)
                else:
                    visited[(x, y)] = [direction]
                if x-1 < 0:
                    return False
                if check_visted_direction(x, y, visited):
                    return True
            direction = 'right'
            
        if direction == 'down':
            if x+1 >= len(matrix):
                return False
            while matrix[x+1][y] != '#':
                x += 1
                if (x, y) in visited.keys():
                    visited[(x, y)].append(direction)
                else:
                    visited[(x, y)] = [direction]
                if x+1 >= len(matrix):
                    return False
                if check_visted_direction(x, y, visited):
                    return True
            direction = 'left'
            
        if direction == 'right':
            if y+1 >= len(matrix[0]):
                return False
            while matrix[x][y+1] != '#':
                y += 1
                if (x, y) in visited.keys():
                    visited[(x, y)].append(direction)
                else:
                    visited[(x, y)] = [direction]
                if y+1 >= len(matrix[0]):
                    return False
                if check_visted_direction(x, y, visited):
                    return True
            direction = 'down'

        if direction == 'left':
            if y-1 < 0:
                return False
            while matrix[x][y-1] != '#':
                y -= 1
                if (x, y) in visited.keys():
                    visited[(x, y)].append(direction)
                else:
                    visited[(x, y)] = [direction]
                if y-1 < 0:
                    return False
                if check_visted_direction(x, y, visited):
                    return True
            direction = 'up'

count = 0
matrix[start_x][start_y] = '^'
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(i, j, ': ', count)
        # se for visitado e nao for a posição inicial
        if matrix[i][j] == 'X' and  not (i == start_x and j == start_y):
            matrix[i][j] = '#' # colocar obstaculo
            if check_cycle(start_x, start_y): # testar se temos ciclo
                count += 1
                matrix[i][j] = 'O'
            else:
                matrix[i][j] = 'X'

print_matrix()
print(count)