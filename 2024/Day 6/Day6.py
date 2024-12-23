with open("2024/Day 6/input.txt", 'r') as file:
    matrix = [list(line.strip()) for line in file]

def get_start():
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

    return start_x, start_y

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
    # start walking from beginning
    # if we pass a node already visited with the same direction we have a cycle
    direction = 'up'
    visited = {(x, y): [direction]}

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

def main():
    start_direction = 'up'
    start_x, start_y = get_start()
    matrix[start_x][start_y] = 'X'
    walk(start_direction, start_x, start_y)

    # Part 1
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'X':
                count += 1
    print("Part 1:", count)

    # Part 2
    count = 0
    matrix[start_x][start_y] = '^'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # se for visitado e nao for a posição inicial
            if matrix[i][j] == 'X' and  not (i == start_x and j == start_y):
                matrix[i][j] = '#' # colocar obstaculo
                if check_cycle(start_x, start_y): # testar se temos ciclo
                    count += 1
                    matrix[i][j] = 'O'
                else:
                    matrix[i][j] = 'X'

    print("Part 2:", count)

main()