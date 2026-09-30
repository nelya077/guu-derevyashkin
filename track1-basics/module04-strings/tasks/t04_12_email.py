"""
Задача 04-12. Проверка e-mail

Прочитайте строку — предполагаемый адрес e-mail — и выведите True,
если она похожа на корректный адрес по правилам ниже, иначе False:

1. символ «@» встречается ровно один раз;
2. «@» стоит не в начале и не в конце строки;
3. после «@» есть хотя бы одна точка.

Пример
------
Ввод:
ivan@mail.ru
Вывод:
True
"""
from selectors import SelectSelector

# TODO: проверьте все три правила (пригодятся count и find)
mail = str(input())

if mail.count("@") == 1 and mail[0] != "@" and mail[-1] != "@" and mail.count(".") > 0:
    print(True)
else:
    print(False)