from queue import Queue
from collections import deque
import functools
import heapq

with open("Day 16/test.txt", 'r') as file:
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

graph = get_graph()
visited = []

@functools.cache
def find_best_score_bfs(current, end, score, cur_dir):
    if current == end:
        return 0

    adj = graph[current]
    for node in adj:
        new_dir = node[0]
        new_node = node[1]
        if new_node not in visited:
            visited.append(new_node)
            if new_dir != cur_dir:
                score += 1000
            return min(score, find_best_score_bfs(new_node, end, score+1, new_dir))

def find_all_paths_bfs(graph, start, end):
    # Queue to store paths, initialized with the start node
    queue = deque([[start]])
    all_paths = []

    while queue:
        # Get the current path
        path = queue.popleft()
        current_node = path[-1]

        # Explore neighbors from the graph
        for neighbor in graph[current_node]:
            # Extract the destination node from the neighbor info
            next_node = neighbor[1]
            print(next_node)

            # If the destination is reached, save the path
            if next_node == end:
                print(path+[next_node])
                all_paths.append(path+[next_node])
                continue

            # Avoid revisiting nodes in the current path
            if next_node not in path:
                new_path = path + [next_node]
                queue.append(new_path)

    return all_paths

def find_all_paths_dfs_recursive(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    result = []
    maze[end[0]][end[1]] = '.'

    def is_valid(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == '.' and not visited[x][y]

    def dfs(x, y, path, visited):
        # Add current cell to the path
        path.append((x, y))
        visited[x][y] = True

        # If end is reached, add the path to the result
        if (x, y) == end:
            result.append(path[:])  # Append a copy of the path
        else:
            # Explore all neighbors (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, visited):
                    dfs(nx, ny, path, visited)

        # Backtrack: Remove current cell from path and unmark visited
        path.pop()
        visited[x][y] = False

    # Create a visited matrix
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Start DFS from the start position
    dfs(start[0], start[1], [], visited)

    return result

def find_all_paths_dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    result = []
    maze[end[0]][end[1]] = '.'
    score = float('inf')

    def is_valid(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == '.' and not visited[x][y]

    # Stack contains tuples of (current_x, current_y, path_so_far, visited_state)
    stack = [(start[0], start[1], [(start[0], start[1])], [[False for _ in range(cols)] for _ in range(rows)])]

    while stack:
        x, y, path, visited = stack.pop()

        # Mark the current cell as visited
        visited[x][y] = True

        # If the end is reached, save the path
        if (x, y) == end:
            print(score)
            score = min(score, get_score(path))
            result.append(path)
            continue

        # Explore all valid neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                # Push the neighbor to the stack with the updated path and visited grid
                new_visited = [row[:] for row in visited]  # Create a copy of visited
                stack.append((nx, ny, path + [(nx, ny)], new_visited))

    return score
                
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

    print(directions)

    return steps + num_directions*1000

# def dijkstra(graph, source, target):
#     # Initialize distances and priority queue
#     distances = {node: float('inf') for node in graph}
#     distances[source] = 0
#     directions = {node: None for node in graph}
#     directions[start] = 'right'
    
#     # Predecessor map to reconstruct the shortest path
#     predecessors = {node: None for node in graph}
    
#     priority_queue = [(0, source, 'right')]  # (distance, node)

#     while priority_queue:
#         current_distance, current_node, last_direction = heapq.heappop(priority_queue)

#         # Skip if we have already found a shorter path
#         if current_distance > distances[current_node]:
#             continue

#         # If we reached the target, no need to process further
#         if current_node == target:
#             break

#         # Explore neighbors
#         for direction, neighbor in graph[current_node]:
#             weight = 0
#             if direction != last_direction:
#                 weight = 1000

#             tentative_distance = current_distance + weight + 1

#             # Update the shortest distance if necessary
#             if tentative_distance < distances[neighbor]:
#                 directions[neighbor] = direction
#                 distances[neighbor] = tentative_distance
#                 predecessors[neighbor] = current_node
#                 heapq.heappush(priority_queue, (tentative_distance, neighbor))

#     # Reconstruct the shortest path from source to target
#     path = []
#     current_node = target
#     while current_node is not None:
#         path.append(current_node)
#         current_node = predecessors[current_node]

#     path.reverse()  # Reverse the path to get it from source to target

#     return distances[target], path

def dijkstra_with_direction_change(graph, source, target):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    # Predecessor map to reconstruct the shortest path
    predecessors = {node: None for node in graph}
    
    # Directions from each node (to store the last direction we came from)
    directions = {node: None for node in graph}  # None means no direction yet
    directions[start] = 'right'

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
    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]

    path.reverse()  # Reverse the path to get it from source to target

    return distances[target], path

start = get_start()
end = get_end()
score, path = dijkstra_with_direction_change(graph, start, end)

print(score)