# Даны два числа a и b, представленные в виде строк.
# Найдите произведение этих чисел и верните его в виде строки.

def num(a: str, b: str):
    return str(int(a) * int(b))


res = num('13','12')
print(res)
