# Реализуйте алгоритм быстрого возведения числа a в степень b.

def fast(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        res = fast(a, b // 2)
        return res * res
    else:
        res = fast(a, (b-1) // 2)
        return a * res * res


c = fast(10, 3)
print(c)