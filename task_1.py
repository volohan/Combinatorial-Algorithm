adjacency_matrix = []

with open('test.txt', 'r') as graph:
    N = int(graph.readline())
    for _ in range(N):
        vertex = list(map(int, graph.readline().split(' ')))
        adjacency_matrix.append(vertex)

if N > 1:
    res = 'Y'
    for head in range(N):
        search = [(head, {head})]
        while len(search):
            vertex_index, visited = search.pop()
            vertex = adjacency_matrix[vertex_index]
            for i in range(N):
                if vertex[i] == 1:
                    if i == head:
                        if len(visited) % 2 != 0:
                            res = 'N'
                    elif i not in visited:
                        new = set(visited)
                        new.add(i)
                        search.append((i, new))
else:
    res = 'N'

print(res)
