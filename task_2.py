adjacency_list = []

with open('in.txt', 'r') as graph:
    N = int(graph.readline())
    for _ in range(N):
        vertex = list(map(lambda x: int(x) - 1,
                          graph.readline().split(' ')[:-1]))
        adjacency_list.append(vertex)

res = ('A', None)
all_visited = set()
for j in range(N):
    if j not in all_visited:
        all_visited.add(j)
        path = [j]
        search = [(j, path)]
        while len(search):
            vertex_index, path = search.pop(0)
            vertex = adjacency_list[vertex_index]
            for i in vertex:
                if i in path:
                    if i != path[-2]:
                        start = path.index(i)
                        res = ('N', path[start:])
                        break
                else:
                    all_visited.add(i)
                    new = list(path)
                    new.append(i)
                    search.append((i, new))
        if res[0] == 'N':
            break

with open('out.txt', 'w') as file:
    file.write(res[0])
    if res[1]:
        file.write('\n' + str(sorted(map(lambda x: x + 1, res[1]))))
