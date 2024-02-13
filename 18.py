# 17. Дано `N` золотых слитков массой $m_1, …, m_N$.
# Ими наполняют рюкзак, который выдерживает вес не более `M`.
# Можно ли набрать вес в точности `M`?

def can_get_weight(arr, m):
    can_get = [True] + [0]*m
    for new in arr:
        can_get = [can_get[weight] or weight - new >= 0 and can_get[weight-new] for weight in range(m+1)]
    return can_get[m]
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# print('YES' if can_get_weight(arr, m) else 'NO')