# Даны два сортированных списка arr1 и arr2.
# Выполнить их слияние так, чтобы полученный список так же был сортирован.

def sort_add(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = j = 0
    c = []

    while i<n and j<m:
        if arr1[i] > arr2[j]:
            c.append(arr2[j])
            j += 1
        else:
            c.append(arr1[i])
            i += 1

    while i<n:
        c.append(arr1[i])
        i += 1

    while j<m:
        c.append(arr2[j])
        j += 1
    return c

x = sort_add([1,3,5],[2,8,10,11])
print(x)
