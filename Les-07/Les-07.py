# Les 07
# Author: Red-F0X (Panin Stanislav)
# Data create: 01.09.2021

# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
def bubble_sort(ls):
    for val in range(len(ls) - 1, 0, -1):
        flag = True
        for el in range(val):
            if ls[el] > ls[el + 1]:
                ls[el], ls[el + 1] = ls[el + 1], ls[el]
                flag = False

        if flag is True:
            break
    return ls


# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
def interflow_sort(ls, point=50):
    limit_ls = [el for el in ls if el <= point]
    result = []

    if len(limit_ls) < 2:
        return ls

    right_part = interflow_sort(ls[len(limit_ls) // 2:])
    left_part = interflow_sort(ls[:len(limit_ls) // 2])

    step1 = 0
    step2 = 0
    while step1 < len(left_part) and step2 < len(right_part):
        if left_part[step1] <= right_part[step2]:
            result.append(left_part[step1])
            step1 += 1
        else:
            result.append(right_part[step2])
            step2 += 1

    result += left_part[step1:] + right_part[step2:] + [el for el in ls if el > point]
    return result


# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
def median(ls):
    half = len(ls) // 2
    ls.sort()
    if not len(ls) % 2:
        return (ls[half - 1] + ls[half]) // 2
    return ls[half]


if __name__ == '__main__':
    nums = [0, 8, 29, 6, 22, 25, 99, 24, 44, 29, 7, 36,
            10, 98, 40, 31, 32, 11, 8, 19, 25, 97, 15, 27,
            29, 17, 27, 20, 41, 8, 14, 26, 20, 4, 50, 46, 17,
            47, 29, 1, 47, 34, 37, 11, 18, 45, 42, 3, 6, 30, 5,
            39, 36, 0, 32, 42, 96, 20, 5, 26, 19, 12, 36, 34, 22,
            13, 27, 33, 45, 38, 19, 30, 11, 27, 18, 20, 7, 27, 14,
            14, 29, 1, 12, 47, 23, 7, 21, 44, 43, 50, 12, 47, 42, 12,
            35, 29, 14, 31, 10, 49]
    print(bubble_sort([5, 4, 6, 8, 1, 7, 5, 4, 3, 2, 9]))
    print(interflow_sort(nums))
    print(median(nums))
