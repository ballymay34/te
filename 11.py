# Дан сортированный список целых чисел arr и число x. Найти индекс, на котором будет
# расположено число x в списке, после его добавления в список в порядке сортировки.

def find(arr, x):
    arr.append(x)
    n = len(arr)

    for run in range(n-1):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    for c in range(0,n):
        if arr[c] == x:
            return c

b = find([1,3,4], 2)
print(b)