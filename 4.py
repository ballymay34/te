# Даны два числа a и b. Найдите их наибольший общий делитель
def nod(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


c = nod(18, 24)
print(c)