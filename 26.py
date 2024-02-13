# 26. Дано `N` городов и известны расстояния между ними. Не все города связаны друг с другом дорогой. Найти все возможные маршруты из города А в город В (ни в один город не заходить дважды).
# Определить самый длинный и самый короткий маршрут.

def find_routes(edges, start, target):
    adj = {}
    for a, b, cost in edges:
        if a not in adj:
            adj[a] = set()
        adj[a].add((b, cost))

    routes = []

    def dfs(a, curr_route, curr_length):
        if a == target:
            routes.append((curr_route.copy(), curr_length))
            return
        for b, length in adj[a]:
            if b in curr_route:  # loop
                continue
            curr_length += length
            curr_route.append(b)
            dfs(b, curr_route, curr_length)
            curr_route.pop()
            curr_length -= length

    dfs(start, [start], 0)
    return routes


def get_min_and_max_route(routes):
    min_i = max_i = 0
    for i in range(len(routes)):
        length = routes[i][1]
        if length < routes[min_i][1]:
            min_i = i
        if length > routes[max_i][1]:
            max_i = i
    return routes[min_i], routes[max_i]


routes = find_routes({
    (1, 2, 10),
    (1, 4, 30),
    (1, 5, 100),
    (2, 3, 50),
    (3, 5, 10),
    (4, 3, 20),
    (4, 5, 60),
}, 1, 5)
print(routes)
print(get_min_and_max_route(routes))