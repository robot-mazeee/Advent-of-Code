with open("Day 10/input.txt", 'r') as file:
    matrix = [list(line.strip()) for line in file]

def find_all_paths(i, j):
    paths = [[[i, j]]]
    key = 0
    for i in range(9):
        key += 1
        paths_copy = paths[:]
        for path in paths_copy:
            # last coordinate of the path
            x = path[-1][0]
            y = path[-1][1]
            # left 
            if y-1 >= 0 and int(matrix[x][y-1]) == key:
                values = path + [[x, y-1]]
                paths.append(values)
            # right
            if y+1 < len(matrix[0]) and int(matrix[x][y+1]) == key:
                values = path + [[x, y+1]]
                paths.append(values)
            # down
            if x+1 < len(matrix) and int(matrix[x+1][y]) == key:
                values = path + [[x+1, y]]
                paths.append(values)
            # up
            if x-1 >= 0 and int(matrix[x-1][y]) == key:
                values = path + [[x-1, y]]
                paths.append(values)

            paths.remove(path)

    print(paths)
    return len(paths)

res = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # in how many ways we can reach the same nine
        if matrix[i][j] == '0':
            res += find_all_paths(i, j)

print('Result:', res)