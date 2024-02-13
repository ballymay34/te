# 34. Найти минимальное покрывающее дерево для заданного графа. Вывести список его ребер и суммарный вес.

# ejudge: https://informatics.msk.ru/mod/statements/view.php?id=53495&chapterid=185#1
class DisjSet:  # source: Lection 9
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1


def kruskalMST(n, edges):
    disj_set = DisjSet(n)
    edges = sorted(edges, reverse=True, key=lambda e: e[2])
    n_included = 0
    result = []
    while n_included < n - 1:
        a, b, w = edges.pop()
        if disj_set.find(a) != disj_set.find(b):
            n_included += 1
            result.append([a, b, w])
            disj_set.union(a, b)
    return result, sum(map(lambda e: e[2], result))


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append([a - 1, b - 1, w])

mst, total_w = kruskalMST(n, edges)
print(total_w)