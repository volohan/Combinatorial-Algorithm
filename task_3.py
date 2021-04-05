import math

transitions = []
lengths = []
previous = []

with open('in.txt', 'r') as graph:
    N = int(graph.readline())
    for _ in range(N):
        transitions.append([])
        previous.append(None)
    for i in range(N):
        data = list(map(int, graph.readline().split(' ')))[:-1]
        for j in range(0, len(data), 2):
            transitions[data[j] - 1].append((i, data[j + 1]))
        lengths.append(math.inf)
    start = int(graph.readline()) - 1
    lengths[start] = 0
    end = int(graph.readline()) - 1

vertexes = {i for i in range(N)}
for _ in range(N-1):
    q = sorted(list(vertexes), key=lambda x: lengths[x]).pop(0)
    vertexes.remove(q)
    for v, weight in transitions[q]:
        if lengths[q] + weight < lengths[v]:
            lengths[v] = lengths[q] + weight
            previous[v] = q

with open('out.txt', 'w') as out:
    if lengths[end] == math.inf:
        out.write('N')
    else:
        out.write('Y\n')
        res = [end + 1]
        current = end
        while current != start:
            current = previous[current]
            res.append(current + 1)
        out.write(str(list(reversed(res))) + '\n')
        out.write(str(lengths[end]) + '\n')
