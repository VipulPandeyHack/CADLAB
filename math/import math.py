import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes

def analyze_primes(primes):
    total = sum(primes)
    avg = total / len(primes) if primes else 0
    return total, avg, len(primes)

primes = generate_primes(500)
total, avg, count = analyze_primes(primes)

print(count)
print(total)
print(avg)