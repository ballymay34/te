# Найти k-тое по счету простое число. Число 2 считать простым числом с номером 1.

def k_prime(n):
    primes = []
    d = 2
    while len(primes) < n:
        is_prime = True
        square_d = d**0.5
        for p in primes:
            if p > square_d:
                break
            if d % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(d)
        d += 1
    return primes[-1]
