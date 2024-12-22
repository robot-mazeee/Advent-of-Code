with open("2024/Day 8/input.txt", 'r') as file:
    matrix = [list(line.strip()) for line in file]

def manhattan_distance(x1, y1, x2, y2):
    return (x1-x2, y1-y2)

nodes_visited = []
nodes = 0
def check_node(x1, y1, x2, y2):
    dist = manhattan_distance(x1, y1, x2, y2)
    node1_x = x1 + dist[0]
    node1_y = y1 + dist[1]
    node2_x = x2 - dist[0]
    node2_y = y2 - dist[1]
    
    if 0 <= node1_x < len(matrix) and 0 <= node1_y < len(matrix[0]):
        if [node1_x, node1_y] not in nodes_visited:
            nodes_visited.append([node1_x, node1_y])
            if matrix[node1_x][node1_y] == '.':
                matrix[node1_x][node1_y] = '#'

    if 0 <= node2_x < len(matrix) and 0 <= node2_y < len(matrix[0]):
        if [node2_x, node2_y] not in nodes_visited:
            nodes_visited.append([node2_x, node2_y])
            if matrix[node2_x][node2_y] == '.':
                matrix[node2_x][node2_y] = '#'

def search(char, i, j):
    for x in range(i, len(matrix)):
        if x == i:
            start = j+1
        else:
            start = 0
        for y in range(start, len(matrix[0])):
            if char == matrix[x][y]:
                check_node(i, j, x, y)

def main():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            char = matrix[i][j]
            if char != '.' and char != '#':
                search(char, i, j)

    print("Part 1:", len(nodes_visited))

main()