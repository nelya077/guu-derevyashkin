"""
Задача 11-04. Простые числа до N

Напишите функцию primes_up_to(n), которая возвращает список всех простых
чисел от 2 до n включительно. Способ на выбор: перебор делителей
или решето Эратосфена.

Примеры
--------
primes_up_to(10) → [2, 3, 5, 7]
primes_up_to(2)  → [2]
"""


def primes_up_to(n):
    # TODO: перебор или решето
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    d = 2
    while d * d <= n:
        if sieve[d]:
            for m in range(d * d, n + 1, d):
                sieve[m] = False
        d += 1
    return [i for i in range(2, n + 1) if sieve[i]]
