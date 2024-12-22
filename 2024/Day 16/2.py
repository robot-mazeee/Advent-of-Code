from queue import Queue
import heapq
from collections import defaultdict

with open("Day 16/input.txt", 'r') as file:
    lines = file.readlines()

matrix = []
for line in lines:
    chars = []
    line = line.strip()
    for char in line:
        chars.append(char)
    matrix.append(chars)

def get_end():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'E':
                return (i, j)

def get_start():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                return (i, j)
            
def get_graph():
    graph = {}
    size = len(matrix)
    inner_size = len(matrix[0])

    for i in range(size):
        for j in range(inner_size):
            if matrix[i][j] == '#':
                continue

            adj_nodes = []
            # check up
            if i-1 > -1 and matrix[i-1][j] != '#':
                adj_nodes.append(['up', (i-1, j)])
            # check down
            if i+1 < size and matrix[i+1][j] != '#':
                adj_nodes.append(['down', (i+1, j)])
            # check left
            if j-1 > -1 and matrix[i][j-1] != '#':
                adj_nodes.append(['left', (i, j-1)])
            # check right
            if j+1 < inner_size and matrix[i][j+1] != '#':
                adj_nodes.append(['right', (i, j+1)])

            graph[(i, j)] = adj_nodes

    return graph

def dijkstra(graph, start):
    # Distância inclui direção
    dist = {(node, direction): float('inf') for node in graph for direction in ['right', 'left', 'up', 'down']}
    dist[(start, 'right')] = 0  # Inicializa o custo para a direção inicial
    prev = defaultdict(set)  # Predecessores não precisam de direção aqui

    # Fila de prioridade com direção
    priority_queue = [(0, 'right', start)]  # (distância, direção, nó atual)

    while priority_queue:
        current_distance, direction, current_node = heapq.heappop(priority_queue)

        # Verifica custo associado à direção
        if current_distance > dist[(current_node, direction)]:
            continue

        # Explora vizinhos
        for new_direction, neighbor in graph[current_node]:
            distance = current_distance + 1
            if new_direction != direction:
                distance += 1000

            # Atualiza predecessores e custos com base na direção
            if distance < dist[(neighbor, new_direction)]:
                dist[(neighbor, new_direction)] = distance
                prev[(neighbor, new_direction)] = {(current_node, direction)}
                heapq.heappush(priority_queue, (distance, new_direction, neighbor))
            elif distance == dist[(neighbor, new_direction)]:
                prev[(neighbor, new_direction)].add((current_node, direction))

    # print(prev[(7, 5), 'left'])
    return dist, prev

def reconstruct_paths(predecessors, distances, end):
    queue = Queue()
    queue.put((end, 'right'))
    paths = set([end])
    directions = ['right', 'left', 'up', 'down']

    while not queue.empty():
        node, direction = queue.get()
        for prev_node, new_direction in predecessors[(node, direction)]:
            if prev_node not in paths:
                queue.put((prev_node, new_direction))
                paths.add(prev_node)
            distance = distances[(prev_node, new_direction)]
            for d in directions:
                if dist[(prev_node, d)] == distance:
                    queue.put((prev_node, d))

    for pos in paths:
        matrix[pos[0]][pos[1]] = 'O'

    return paths

def write_out():
    with open("Day 16/test.out", 'w') as file:
        for line in matrix:
            for char in line:
                file.write(char)
            file.write('\n')

start = get_start()
end = get_end()
graph = get_graph()
dist, pred = dijkstra(graph, start)
paths = reconstruct_paths(pred, dist, end)
write_out()
print(len(paths))