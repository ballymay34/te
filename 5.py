# Даны два числа a и b. Найдите пару чисел x и y, являющуюся решением уравнения вида: НОД

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x