# 31. Система двусторонних дорог такова, что для любой пары городов можно указать соединяющий их путь. Найдите такой город, сумма расстояний от которого до остальных городов минимальна.

def find_city_with_max_neighbor_dist_sum(adj):
    res, max_sum = 0, 0
    for a, neighbors:
        s = sum([length for b, length in neighbors])
        if s >= max_sum:
            res, max_sum = a, s
    return res, max_sum
