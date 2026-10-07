"""
Задача 06-06. Частоты букв

Прочитайте строку и посчитайте частоты букв (без учёта регистра, пробелы
не считать). Выведите «буква: количество» построчно, буквы — по алфавиту.

Пример
------
Ввод:
мама
Вывод:
а: 2
м: 2
"""

# TODO: частоты букв словарём, вывод по отсортированным ключам
n = input().lower()
word = {}
for letter in n:
    if letter == " ":
        continue
    if letter in word:
        word[letter] += 1
    else:
        word[letter] = 1
for letter in sorted(word):
    print(f"{letter}: {word[letter]}")

