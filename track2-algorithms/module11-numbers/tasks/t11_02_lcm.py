"""
Задача 11-02. НОК

Напишите функцию lcm(a, b), которая возвращает наименьшее общее кратное,
используя вашу же формулу через НОД: lcm = a * b // gcd(a, b).

Примеры
--------
lcm(4, 6)  → 12
lcm(7, 13) → 91
"""


def lcm(a, b):
    # TODO: a * b // gcd(a, b); gcd можно взять из задачи 11-01
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
