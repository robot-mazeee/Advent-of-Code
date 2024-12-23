from queue import Queue
from collections import defaultdict
import heapq

def parse_input():
    with open("2024/Day16/input.txt", 'r') as file:
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
                return (i, j)

def get_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                return (i, j)
            
def get_graph(matrix):
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

def get_shortest_path(graph, start, end):
    visited = [start]
    queue = Queue()
    queue.put([start])
    score = float('inf')

    while not queue.empty():
        path = queue.get()
        neighbours = graph[path[-1]]

        for _, pos in neighbours:
            if pos == end:
                score = min(get_score(path + [pos]), score)
            if pos not in visited:
                visited.append(pos)
                new_path = path + [pos]
                queue.put(new_path)

def get_score(path):
    steps = len(path)
    directions = '>'

    for i in range(1, steps):
        prev_x, prev_y = path[i-1]
        cur_x, cur_y = path[i]
        if cur_x == prev_x+1:
            directions += 'v'
        elif cur_x == prev_x-1:
            directions += '^'
        elif cur_y == prev_y+1:
            directions += '>'
        elif cur_y == prev_y+1:
            directions += '<'

    num_directions = 0
    for i in range(1, len(directions)):
        if directions[i] != directions[i-1]:
            num_directions += 1

    return steps + num_directions*1000

def dijkstra_with_direction_change(graph, source, target):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    # Predecessor map to reconstruct the shortest path
    predecessors = {node: None for node in graph}
    
    # Directions from each node (to store the last direction we came from)
    directions = {node: None for node in graph}  # None means no direction yet
    directions[source] = 'right'

    # Priority queue for Dijkstra's algorithm
    priority_queue = [(0, source, 'right')]  # (distance, node, direction_from_parent)

    while priority_queue:
        current_distance, current_node, last_direction = heapq.heappop(priority_queue)

        # Skip if we already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # If we reached the target, no need to continue
        if current_node == target:
            break

        # Explore neighbors
        for direction, (neighbor) in graph[current_node]:
            # Add cost based on direction change
            extra_cost = 0
            if last_direction and direction != last_direction:
                extra_cost = 1000  # Direction change adds cost of 1000
            
            tentative_distance = current_distance + extra_cost + 1

            # Update the shortest distance if necessary
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                predecessors[neighbor] = current_node
                directions[neighbor] = direction  # Store the direction
                heapq.heappush(priority_queue, (tentative_distance, neighbor, direction))

    # Reconstruct the shortest path
    # path = []
    # current_node = target
    # while current_node is not None:
    #     path.append(current_node)
    #     current_node = predecessors[current_node]

    # path.reverse()  # Reverse the path to get it from source to target

    return distances[target]

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
                if distances[(prev_node, d)] == distance:
                    queue.put((prev_node, d))

    return paths

def main():
    matrix = parse_input()
    graph = get_graph(matrix)

    start = get_start(matrix)
    end = get_end(matrix)
    score = dijkstra_with_direction_change(graph, start, end)

    dist, pred = dijkstra(graph, start)
    paths = reconstruct_paths(pred, dist, end)

    print("Part 1:", score)
    print("Part 2:", len(paths))

main()