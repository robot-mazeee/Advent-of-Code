from queue import Queue

def parse_input():
    with open("2024/Day20/input.txt", 'r') as file:
        lines = file.readlines()

    matrix = []
    for line in lines:
        chars = []
        line = line.strip()
        for char in line:
            chars.append(char)
        matrix.append(chars)
    
    return matrix

def get_end(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'E':
                matrix[i][j] = '.'
                return (i, j)

def get_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                matrix[i][j] = '.'
                return (i, j)
   
def get_graph(matrix):
    graph = {}
    size = len(matrix)
    inner_size = len(matrix[0])

    for i in range(size):
        for j in range(inner_size):
            if matrix[i][j] == '.':
                adj_nodes = []
                if i-1 > -1 and matrix[i-1][j] != '#':
                    adj_nodes.append((i-1, j))
                # check down
                if i+1 < size and matrix[i+1][j] != '#':
                    adj_nodes.append((i+1, j))
                # check left
                if j-1 > -1 and matrix[i][j-1] != '#':
                    adj_nodes.append((i, j-1))
                # check right
                if j+1 < inner_size and matrix[i][j+1] != '#':
                    adj_nodes.append((i, j+1))
                graph[(i, j)] = adj_nodes

    return graph

def bfs(graph, start, end):
    visited = []
    start_path = [start]
    q = Queue()
    q.put(start_path)

    while not q.empty():
        path = q.get()
        neighbours = graph[path[-1]]

        for node in neighbours:
            if node == end:
                return path + [end]
            
            if node not in visited:
                visited.append(node)
                new_path = path + [node]
                q.put(new_path)

def get_adj(matrix, pos, char):
    x, y = pos

    adj = []
    # down
    if x+1 < len(matrix) and matrix[x+1][y] == char:
        adj.append((x+1, y))
    # up
    if x-1 >= 0 and matrix[x-1][y] == char:
        adj.append((x-1, y))
    # right
    if y+1 < len(matrix[0]) and matrix[x][y+1] == char:
        adj.append((x, y+1))
    # left
    if y-1 >= 0 and matrix[x][y-1] == char:
        adj.append((x, y-1))

    return adj

def get_cheat_dists(matrix, path, pos, node, index):
    # get neighbours of node and add to graph
    adj = get_adj(matrix, node, '.')

    # get index of pos
    length = len(path)
    index = 0
    for i in range(length):
        if path[i] == pos:
            index = i

    # from that index, check if adj
    dists = []
    for i in range(index+1, length):
        if path[i] in adj:
            new_path = path[:index+1] + path[i:]
            dist = len(new_path)
            dists.append(dist)

    return dists

def part1(matrix, path, goal):
    num_cheats = 0
    index = 0
    for pos in path:
        adj = get_adj(matrix, pos, '#')
        for node in adj:
            dists = get_cheat_dists(matrix, path, pos, node, index)
            for dist in dists:
                if dist <= goal:
                    num_cheats += 1
        index += 1

    return num_cheats

def get_dists(path):
    dists = {}
    index = 0
    for pos in path:
        dists[index] = pos
        index += 1
    return dists

def part2(path, goal):
    dists = get_dists(path)
    length = len(path)
    num_cheats = 0
    for d1 in range(length-1):
        x1, y1 = dists[d1]
        for d2 in range(d1+1, length):
            x2, y2 = dists[d2]
            dist = d2 - d1
            cheat_dist = abs(x2-x1) + abs(y2-y1)
            if cheat_dist <= 20:
                new_len = dist - cheat_dist
                if new_len >= goal:
                    num_cheats += 1

    return num_cheats

def main():
    matrix = parse_input()
    start = get_start(matrix)
    end = get_end(matrix)
    graph = get_graph(matrix)
    path = bfs(graph, start, end)
    goal = len(path)-101

    num_cheats = part1(matrix, path, goal)
    print('Part 1:', num_cheats)
    num_cheats = part2(path, 100)
    print('Part 2:', num_cheats)

main()