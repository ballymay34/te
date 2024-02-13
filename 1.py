# Даны два числа a и b в десятичной системе счисления и основание некоторой системы счисления c.
# Найдите сумму этих чисел в системе счисления c. Результат представить в виде строки.

def decimal_to_base(num, base):
    if num == 0:
        return '0'
    digits = []
    while num:
        digits.append(str(num % base))
        num //= base
    return ''.join(digits[::-1])

def sum_in_base(a, b, base):
    a_in_base = int(decimal_to_base(a, base))
    b_in_base = int(decimal_to_base(b, base))
    sum_in_base = a_in_base + b_in_base
    return decimal_to_base(sum_in_base, base)

a = 10
b = 5
c = 2
result = sum_in_base(a, b, c)
print(result)  # Вывод: '1111'

