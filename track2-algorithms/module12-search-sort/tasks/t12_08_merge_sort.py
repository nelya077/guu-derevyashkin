"""
Задача 12-08 ★. Сортировка слиянием

Напишите функцию merge_sort(items), которая сортирует список рекурсивной
сортировкой слиянием: список делится пополам, части сортируются рекурсивно
и сливаются (слияние — как в задаче 12-07). Базовый случай: список длины
0–1 уже отсортирован. Встроенные sort/sorted запрещены.

Примеры
--------
merge_sort([5, 2, 9, 1]) → [1, 2, 5, 9]
"""


def merge_sort(items):
    # TODO: база случая; деление пополам; рекурсия; слияние
    if len(items) <= 1:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
