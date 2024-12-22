import re
from queue import Queue

with open("2024/Day 21/input.txt", 'r') as file:
    lines = file.readlines()

codes = []
for line in lines:
    line = line.strip()
    codes.append(line)

keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['', '0', 'A']]
robot_keypad = [['', '^', 'A'], ['<', 'v', '>']]

# One directional keypad that you are using.
# Two directional keypads that robots are using.
# One numeric keypad (on a door) that a robot is using.

def get_keypad_pos(val):
    if val == '7':
        return (0, 0)
    if val == '8':
        return (0, 1)
    if val == '9':
        return (0, 2)
    if val == '4':
        return (1, 0)
    if val == '5':
        return (1, 1)
    if val == '6':
        return (1, 2)
    if val == '1':
        return (2, 0)
    if val == '2':
        return (2, 1)
    if val == '3':
        return (2, 2)
    if val == '0':
        return (3, 1)
    if val == 'A':
        return (3, 2)

def get_robot_keypad_pos(val):
    if val == '^':
        return (0, 1)
    if val == 'A':
        return (0, 2)
    if val == '<':
        return (1, 0)
    if val == 'v':
        return (1, 1)
    if val == '>':
        return (1, 2)

def get_graph(keypad):
    graph = {}
    rows = len(keypad)
    cols = len(keypad[0])
    for i in range(rows):
        for j in range(cols):
            if keypad[i][j] == '':
                continue
            adj = []
            if i+1 < rows and keypad[i+1][j] != '':
                adj.append(((i+1, j), 'v'))
            if i-1 > -1 and keypad[i-1][j] != '':
                adj.append(((i-1, j), '^'))
            if j+1 < cols and keypad[i][j+1] != '':
                adj.append(((i, j+1), '>'))
            if j-1 > -1 and keypad[i][j-1] != '':
                adj.append(((i, j-1), '<'))
            graph[(i, j)] = adj

    return graph

def get_all_paths(graph, start, end):
    visited = {start}
    all_paths = []
    queue = Queue()
    min_length = float('inf')
    queue.put([(start, '')])

    while not queue.empty():
        path = queue.get()
        pos = path[-1][0]
        visited.add(pos)
        neighbors = graph[pos]

        for node in neighbors:
            if node[0] not in visited:
                new_path = path+[node]
                if node[0] == end:
                    path_length = len(new_path)
                    if path_length <= min_length:
                        all_paths.append(new_path)
                        min_length = path_length
                else:
                    queue.put(new_path)
    
    paths = []
    for path in all_paths:
        dirs = ''
        for _, d in path:
            if d == '':
                dirs += 'A'
            dirs += d
        dirs += 'A'
        dirs = dirs[1:]
        paths.append(dirs)

    return paths

def get_dirs(graph, string):
    paths = []
    for i in range(4):
        start, end = get_keypad_pos(string[i]), get_keypad_pos(string[i+1])
        all_paths = get_all_paths(graph, start, end)
        if len(paths) == 0:
            for path in all_paths:
                paths.append(path)
        else:
            new_paths = []
            for current_path in paths:
                for path in all_paths:
                    new_paths.append(current_path+path)
            paths = new_paths
    return paths

def get_robots_dirs(graph, string):
    paths = []
    length = len(string)
    for i in range(length-1):
        start, end = get_robot_keypad_pos(string[i]), get_robot_keypad_pos(string[i+1])
        if start == end:
            new_paths = []
            for current_path in paths:
                new_paths.append(current_path+'A')
            paths = new_paths
        else:
            all_paths = get_all_paths(graph, start, end)
            if len(paths) == 0:
                for path in all_paths:
                    paths.append(path)
            else:
                new_paths = []
                for current_path in paths:
                    for path in all_paths:
                        new_paths.append(current_path+path)
                paths = new_paths
                
    return paths

def main():
    complexity = 0
    robots_graph = get_graph(robot_keypad)
    for code in codes:
        graph = get_graph(keypad)
        number = int(re.findall(r'\d+', code)[0])
        code = 'A'+code
        paths = get_dirs(graph, code)

        min_path_length = float('inf')
        for path in paths:
            new_paths = get_robots_dirs(robots_graph, 'A'+path)
            for path in new_paths:
                final_paths = get_robots_dirs(robots_graph, 'A'+path)
                for path in final_paths:
                    min_path_length = min(min_path_length, len(path))
        
        print(min_path_length)
        complexity += number * min_path_length

    print(complexity)

main()
