# Найти кол-во простых чисел в диапазоне от 0 до n

n = int(input())
a = [i for i in range(n + 1)]


a[1] = 0
i = 2

while i <= n / 2:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1
a = [i for i in a if a[i] != 0]
print(len(a))