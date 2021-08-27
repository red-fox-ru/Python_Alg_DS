# Les 04
# Author: Red-F0X (Panin Stanislav)
# Data create: 21.08.2021


from time import monotonic


# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
def time_work(func):
    def wrapper(*arg):
        print('')
        start = monotonic()
        result = func(*arg)
        print(f'Время выполнения {func.__name__}: {monotonic() - start}s')
        print("================")
        return result

    return wrapper


# Время выполнения 0.0s
# Сложность O(len(N))
@time_work
def even_odd(num: int):
    """
    Enter num for count even and odd in number.
    :param num:
    :return count even, odd:
    """
    even = len([el for el in list(map(int, str(num))) if not el & 1])
    odd = len([el for el in list(map(int, str(num))) if el & 1])
    return even, odd


# Написать два алгоритма нахождения i-го по счёту простого числа.
#   Без использования «Решета Эратосфена»;
#   Используя алгоритм «Решето Эратосфена»

# Время выполнения 0.0s
# Сложность O(n²)
@time_work
def not_eratosthen(num: int):
    lst = []
    for item in range(2, num + 1):
        for el in range(2, item):
            if item % el == 0:
                break
        else:
            lst.append(item)
    return lst


# Время выполнения 0.0s
# Сложность O(n)
@time_work
def sieve_eratosthen(num: int):
    ls = []
    for item in range(num + 1):
        ls.append(item)
    ls[1] = 0

    start = 2
    while start <= num:
        if ls[start] != 0:
            multiplicity = start + start
            while multiplicity <= num:
                ls[multiplicity] = 0
                multiplicity += start
        start += 1

    result = set(ls)
    result.remove(0)
    return result


if __name__ == '__main__':
    count_even, count_odd = even_odd(64557786786871897312)
    print(f'Чётных {count_even} и {count_odd} нечётных чисел.')

    print(sieve_eratosthen(12))
    print(not_eratosthen(12))
