# Дан ориентированный невзвешенный граф. Определить является ли данный граф ациклическим.

from collections import deque

def bfs_has_cycle(adj, start):
    visited = {start}
    queue = deque([start])a

    while queue:
        node = queue.popleft()
        for neighbor in adj.get(node, []):
            if neighbor in visited:
                return True
            visited.add(neighbor)
            queue.append(neighbor)
    return False

def is_asyclic(adj):
    for start in adj:
        if bfs_has_cycle(adj, start):
            return False
    return True

assert not is_asyclic({1: {2}, 2: {3}, 3: {1}})
assert is_asyclic({1: {2}, 2: {3}, 3: {4, 5}})