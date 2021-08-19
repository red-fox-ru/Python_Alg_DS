# Les 03
# Author: Red-F0X (Panin Stanislav)
# Data create: 18.08.2021

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def count_multiplicity_nums(start: int, end: int):
    """
    Find the multiplicity of numbers in a range.
    :param start:
    :param end:
    :return:
    """
    result = {}
    for num_multiplicity in range(2, 10):
        result[num_multiplicity] = []
        for nat_num in range(start, end + 1):
            if nat_num % num_multiplicity == 0:
                result[num_multiplicity].append(nat_num)
        print(f'{num_multiplicity} кратны - {len(result[num_multiplicity])} числам.')


# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то
# во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
def even_element_list(ls: list):
    """
    Create list of indices of even elements of the origin list.
    :param ls:
    :return:
    """
    return [ls.index(el) for el in ls if el % 2 == 0]


# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def change_max_min(ls: list):
    """
    Change index max and min nums.
    :param ls:
    :return:
    """
    ls[ls.index(max(ls))], ls[ls.index(min(ls))] = ls[ls.index(min(ls))], ls[ls.index(max(ls))]
    return ls


# Определить, какое число в массиве встречается чаще всего.
def count_max_num(ls: list):
    """
    Find a max num and count repeat.
    :param ls:
    :return:
    """
    return max(ls), ls.count(max(ls))


# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
def count_min_num(ls: list):
    """
    Find a min num and index.
    :param ls:
    :return:
    """
    return min(ls), ls.index(min(ls))


# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
def range_minmax_sum_ls(ls: list):
    """
    Find the sum of elements array in a range.
    :param ls:
    :return:
    """
    step = 1
    min_index, max_index = ls.index(min(ls)), ls.index(max(ls))
    if max_index - min_index < 0:
        step = -1

    sum_ls = sum(ls[min_index + step:max_index:step])

    print(f'Сумма элементов между {ls[min_index]} и {ls[max_index]} элементами: {sum_ls}')


# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def two_min_el(ls: list):
    """
    Find two min nums.
    :param ls:
    :return:
    """
    min_num1 = min(ls)
    ls.pop(ls.index(min(ls)))
    return min_num1, min(ls)


# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
def matrix_from_keyboard():
    """
    Create matrix from keyboard and print him.
    :return:
    """
    matrix = []
    print('Matrix 5x4. Please enter numbers, for sum 4 elements in row.')
    for row in range(0, 4):
        matrix.append([])
        sum_items = 0
        for item in range(1, 5):
            user_num = (int(input(f'Enter {item}\'s number: ')))
            sum_items += user_num
            matrix[row].append(user_num)
        matrix[row].append(sum_items)

    for print_matrix in matrix:
        print(print_matrix)

    return matrix


# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
def max_min_el_matrix(ls: list):
    """
    Find the maximum element among the minimum elements.
    :param ls:
    :return:
    """
    import numpy as np
    return max([min(el) for el in np.transpose(ls)])


if __name__ == '__main__':
    import random as r

    rand_list_num = [r.randint(0, 20) for _ in range(40)]

    count_multiplicity_nums(2, 99)

    print(f'Индексы чётных элементов: {even_element_list([8, 3, 15, 6, 4, 2])}')

    print(f'Список случайных чисел: {rand_list_num}')
    print(change_max_min(rand_list_num))

    max_num, count_max = count_max_num(rand_list_num)
    print(f'Максимальное число {max_num} встречается {count_max} раз.')

    min_num, index_el = count_min_num([-8, -65, -15, -16, -4, -1])
    print(f'Максимально отрицательное число {min_num} находится в {index_el} позиции.')

    range_minmax_sum_ls(rand_list_num)

    print(two_min_el(rand_list_num))

    user_matrix = matrix_from_keyboard()

    print(max_min_el_matrix(user_matrix))
