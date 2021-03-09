adjacency_matrix = []

with open('in.txt', 'r') as graph:
    N = int(graph.readline())
    for _ in range(N):
        vertex = list(map(int, graph.readline().split(' ')))
        adjacency_matrix.append(vertex)

if N > 1:
    res = 'Y'
    fraction_one = {0}
    fraction_two = set()
    search = [(0, {0})]
    while len(search):
        vertex_index, visited = search.pop()
        vertex = adjacency_matrix[vertex_index]
        for i in range(N):
            if vertex[i] == 1:
                if len(visited) % 2 == 0:
                    if i in fraction_two:
                        res = 'N'
                        break
                    fraction_one.add(i)
                else:
                    if i in fraction_one:
                        res = 'N'
                        break
                    fraction_two.add(i)
                if i not in visited:
                    new = set(visited)
                    new.add(i)
                    search.append((i, new))
        if res == 'N':
            break
else:
    res = 'N'

with open('out.txt', 'w') as file:
    file.write(res)
