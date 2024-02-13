# Дана система двусторонних дорог.
# N-периферией называется множество городов, расстояние от которых до выделенного города (столицы) больше N. Для данного N определите N-периферию.

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

def n_periphery(adj, start, N):
    dist = deijkstra(len(adj), adj, start)
    return [city for city in range(len(adj)) if dist[city] > N]

# def matrix_to_adj(matrix):
#     adj = {}
#     for i in range(len(matrix)):
#         adj[i] = set()
#         for j in range(len(matrix[0])):
#             if matrix[i][j] > 0:
#                 adj[i].add((j, matrix[i][j]))
#     return adj

# n, s, f = map(int, input().split())
# s -= 1
# f -= 1
# matrix = []
# for i in range(n):
#     matrix.append([int(a) for a in input().split()])
# adj = matrix_to_adj(matrix)
# dist = shortest_paths(n, adj, s)
# print(dist[f] if not math.isinf(dist[f]) else -1)