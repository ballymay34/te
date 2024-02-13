# Дан список целых чисел arr. Реализовать сортировку простыми обменами,
# в качестве результата вернуть количество перестановок выполненных в процессе сортировки.

def sorter(arr):
    count = 0
    n = len(arr)

    for run in range(n-1):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1

    return count


c = sorter([5,7,4,3,8,2])
print(c)