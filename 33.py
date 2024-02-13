#33. Дан взвешенный ориентированный граф с `n` узлами и `m` ребрами. Узлы пронумерованы от `0` до `n-1`, необходимо проверить, содержит ли граф цикл отрицательного веса.

#   *Примечание:* `edges[i]` состоит из вершин `u`, `v` и веса.

# ejudge: https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1
# source: https://habr.com/ru/companies/otus/articles/484382/

def bellman_ford(v, edges, start):
    """Returns an array with min distances to all vertices from start.
    If graph contains a negative weight cycle, return -1"""
    dist = [float('inf')] * v
    dist[start] = 0
    for _ in range(v - 1):
        for u, v, length in edges:
            if dist[v] > dist[u] + length:
                dist[v] = dist[u] + length
    for u, v, length in edges:
        if dist[v] > dist[u] + length:
            return -1
    return dist


class Solution:
    def isNegativeWeightCycle(self, n, edges):
        return int(any(
            bellman_ford(n, edges, start) == -1 for start in range(n)
        ))