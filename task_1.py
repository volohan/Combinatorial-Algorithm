def task_1(number):
    adjacency_matrix = []

    with open(f'task_1_tests\\{number}.txt', 'r') as graph:
        N = int(graph.readline())
        for _ in range(N):
            vertex = list(map(int, graph.readline().split(' ')))
            adjacency_matrix.append(vertex)
        print(f"[{graph.readline()}]")

    if N > 1:
        res = True
        for head in range(N):
            search = [(head, {head})]
            while len(search):
                vertex_index, visited = search.pop()
                vertex = adjacency_matrix[vertex_index]
                for i in range(N):
                    if vertex[i] == 1:
                        if i == head:
                            if len(visited) % 2 != 0:
                                res = False
                        elif i not in visited:
                            new = set(visited)
                            new.add(i)
                            search.append((i, new))
    else:
        res = False

    print(res)
    print("-----------------------------------------------------------------")


for i in range(6):
    task_1(i)
