# 32. За проезд по каждой дороге взымается некоторая пошлина. Найдите путь из города А в город B с минимальной величиной S+P, где S - сумма длин дорог пути, а P - сумма пошлин проезжаемых дорог.

# ejudge: https://informatics.msk.ru/mod/statements/view.php?id=46422&chapterid=5#1
import math

def deijkstra(N, adj, start):
    dist = [float('inf')]*N
    dist[start] = 0
    visited = set()
    while len(visited) != N:
        curr = min(set(range(N)) - visited, key=dist.__getitem__)
        for neighbor, length in adj[curr]:
            new_dist = dist[curr] + length
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
        visited.add(curr)
    return dist

# edges: (start, end, length, tax)

def edges_to_adj(edges):
    adj = {}
    for a, b, length, tax in edges:
        if a not in adj:
            adj[a] = set()
        total_length = length + tax # let's just sum length and tax right away, since they're equal for the target formula
        adj[a].add((b, total_length))

def get_min_total(edges, a, b):
    adj = edges_to_adj(edges)
    dist = deijkstra(len(adj), adj, a)
    return dist[b]

# m, a, b = map(int, input().split())
# edges = [list(map(int, input().split())) for _ in range(m)]
# print(get_min_total(edges, a, b))k