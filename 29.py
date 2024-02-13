# 29. Даны `N` процессов. Каждый процесс может быть запущен сразу, а может быть только после выполнения некоторого количества предыдущих процессов. Список зависимостей дан в списке `depend`. `depend[i]` - список процессов, от которых зависит процесс `i`. Найти порядок, в котором необходимо выполнять процессы, чтобы зависимый процесс начинался после выполнения предыдущих. Если таких порядков несколько, верните любой. Гарантируется, что существует хотя бы один процесс, который не имеет зависимостей.

def topological_sort(adj): # source: https://ru.algorithmica.org/cs/graph-traversals/topological-sorting/?ysclid=lqp83ys8q1434368187
    if not is_asyclic(adj):
        raise ValueError('graph must be asyclic in order to have a topological sorting')
    visited = set()
    topo_order = []
    def dfs(a):
        visited.add(a)
        for b in adj.get(a, []):
            if b not in visited:
                dfs(b)
        topo_order.append(a)
    for a in adj:
        if a not in visited:
            dfs(a)
    return topo_order[::-1]


def inverse_adj(adj):
    inv = {}
    for a, neighbors in adj.items():
        for b in neighbors:
            if b not in inv:
                inv[b] = set()
            inv[b].add(a)

    print(inv)
    return inv

def order_processes(depend):
    return topological_sort(inverse_adj(depend))

print(order_processes({5: {}, 4: {}, 0: {4, 5}, 2: {5}, 1: {3, 4}, 3: {2}}))