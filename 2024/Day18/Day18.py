from queue import Queue

def parse_input(rows, cols, num_bytes):
    with open("2024/Day18/input.txt", 'r') as file:
        lines = file.readlines()

    matrix = [['.' for _ in range(rows)] for _ in range(cols)]

    i = 0
    for line in lines:
        i += 1
        if i > num_bytes:
            break
        line = line.strip()
        line = line.split(',')
        x, y = int(line[0]), int(line[1])
        matrix[y][x] = '#'

    return matrix, lines

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

def get_adj(matrix, i, j):
    size = len(matrix)
    inner_size = len(matrix[0])

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
    
    return adj_nodes

def main():
    start = (0, 0)
    end = (70, 70)
    rows = 71
    cols = 71
    num_bytes = 1024

    matrix, lines = parse_input(rows, cols, num_bytes)
    graph = get_graph(matrix)
    path = bfs(graph, start, end)

    print("Part 1:", len(path)-1)

    # if a node is in path, change bfs choice only at that node
    for i in range(num_bytes+1, len(lines)):
        # print(i)
        line = lines[i]
        line = line.strip()
        line = line.split(',')
        y, x = int(line[0]), int(line[1])
        matrix[x][y] = '#'

        adj_nodes = get_adj(matrix, x, y)
        for adj in adj_nodes:
            graph[adj].remove((x, y))
        if (x, y) in path:
            # the start becomes the node we came from to get to (x, y)
            index = 0
            for pos in path:
                if pos == (x, y): # se chegamos a pos que vamos substituir
                    start = path[index-1] # pegar de onde ela veio
                    break
                index += 1
            new_path = bfs(graph, start, end)
            if new_path is None:
                print("Part 2:", str(y) + ',' + str(x))
                break
            path = path[:index] + new_path

main()