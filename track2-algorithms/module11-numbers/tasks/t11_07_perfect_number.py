"""
Задача 11-07. Совершенное число

Напишите функцию perfect_number(n), которая возвращает True, если n равно
сумме своих делителей, меньших n (например, 6 = 1 + 2 + 3).

Примеры
--------
perfect_number(6)  → True
perfect_number(28) → True
perfect_number(12) → False
"""


def perfect_number(n):
    # TODO: сумма делителей из задачи 11-06 без самого числа
    if n < 2:
        return False
    return sum(d for d in range(1, n) if n % d == 0) == n
