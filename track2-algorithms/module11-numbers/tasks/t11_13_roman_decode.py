"""
Задача 11-13. Из римской записи

Напишите функцию roman_decode(s), которая переводит строку с римской
записью числа (валидной) обратно в целое число. Правило вычитания: буква,
меньшая следующей, вычитается (IV = 4).

Примеры
--------
roman_decode("IX")      → 9
roman_decode("MCMXCIV") → 1994
"""


def roman_decode(s):
    # TODO: обход слева направо с сравнением соседних букв
    values = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        if i + 1 < len(s) and values[ch] < values[s[i + 1]]:
            total -= values[ch]
        else:
            total += values[ch]
    return total
