# 35. В неориентированный взвешенный граф добавляют ребра. Напишите программу, которая, после добавления ребер, находит сумму весов ребер в компоненте связности.
#
#     На вход подаются два числа `n` и `m` - количество вершин в графе и количество производимых добавлений и запросов. Далее следует список `add` из m строк. Каждая строка состоит из трех чисел `x, y, w`. Это означает, что в граф добавляется ребро из вершины x в вершину y веса w. Кратные ребра допустимы. И число `A` - вершина, для компоненты связности которой необходимо найти суммарный вес ребер.

from collections import defaultdict

def dfs(node, graph, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, component)

def find_connected_component_weight(graph, start_node):
    visited = [False] * len(graph)
    component = []
    dfs(start_node, graph, visited, component)
    total_weight = 0
    for node in component:
        for neighbor, weight in graph[node]:
            if neighbor in component:
                total_weight += weight
    return total_weight

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        x, y, w = map(int, input().split())
        graph[x].append((y, w))
        graph[y].append((x, w))

    A = int(input())

    print(find_connected_component_weight(graph, A))

