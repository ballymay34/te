# 27. Дан неориентированный невзвешенный граф.
# Необходимо посчитать количество его компонент связности и вернуть их в виде двумерного списка, количество строк которого соответствует количеству компонент, а в строках содержится множество вершин каждой компоненты.

# source: https://ru.algorithmica.org/cs/graph-traversals/connectivity/?ysclid=lqp4forpqf991113985
def components(adj):
    def dfs(adj, start, component, num):
        component[start] = num
        for end in adj[start]:
            if end not in component:
                dfs(adj, end, component, num)

    num = 0
    component = {}
    for a in adj:
        if a not in component:
            dfs(adj, a, component, num)
            num += 1

    return [{a for a, c_num in component.items() if c_num == i} for i in range(num)]


print(components({1: {4}, 4: {1}, 0: {2}, 2: {5, 3}, 3: {5}, 5: {2}}))