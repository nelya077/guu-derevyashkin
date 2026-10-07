"""
Задача 06-10. Группировка по длине

Прочитайте слова через пробел и сгруппируйте их по длине. Выведите строки
«длина: слова через пробел» — длины по возрастанию, слова внутри группы
в порядке появления.

Пример
------
Ввод:
кот дом дерево
Вывод:
3: кот дом
6: дерево
"""

# TODO: словарь «длина → список слов», вывод по возрастанию длин
words = input().split()
dictionary = {}
for word in words:
    if len(word) in dictionary:
        dictionary[len(word)].append(word)
    else:
        dictionary[len(word)] = [word]

for length in sorted(dictionary):
    print(f"{length}:", *dictionary[length])