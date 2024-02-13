# Проверить, является ли число а простым

def isprime(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


c = isprime(27)
print(c)