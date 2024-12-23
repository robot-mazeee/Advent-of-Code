def parse_input():
    with open("2024/Day23/input.txt", 'r') as file:
        lines = [line.strip().split('-') for line in file]

    return lines

def get_graph(lines):
    graph = {}

    for line in lines:
        first = line[0]
        second = line[1]
        if first in graph:
            graph[first].append(second)
        else:
            graph[first] = [second]
        if second in graph:
            graph[second].append(first)
        else:
            graph[second] = [first]

    return graph

def check_connections(connections, key, value, val):
    con1 = (key, value, val)
    con2 = (key, val, value)
    con3 = (value, key, val)
    con4 = (value, val, key)
    con5 = (val, key, value)
    con6 = (val, value, key)

    if con1 in connections or con2 in connections or con3 in connections or con4 in connections or con5 in connections or con6 in connections:
        return False
    
    return True

def bors_kerbosch(R, P, X, G, C):
    if len(P) == 0 and len(X) == 0:
        if len(R) > 2:
            C.append(sorted(R))
        return 
    
    for v in P.union(set([])):
        bors_kerbosch(R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G, C)
        P.remove(v)
        X.add(v)

def part1(graph):
    res = 0
    connections = []

    for key in graph:
        values = graph[key]
        for value in values:
            v = graph[value]
            for val in v:
                if val in values and val != key:
                    if check_connections(connections, key, value, val):
                        connections.append((key, value, val))
                        if key[0] == 't' or value[0] == 't' or val[0] == 't':
                            res += 1

    return res

def part2(graph):
    cliques = []
    bors_kerbosch(set([]), set(graph.keys()), set([]), graph, cliques)
    
    max_len = 0
    for clique in cliques:
        if len(clique) > max_len:
            max_len = len(clique)
            password_computers = clique

    password = ''
    for computer in password_computers:
        password += computer + ','

    password = password[:len(password)-1]
    return password

def main():
    lines = parse_input()
    graph = get_graph(lines)

    res1 = part1(graph)
    res2 = part2(graph)

    print("Part 1:", res1)
    print("Part 2:", res2)

main()
