# Les 02
# Author: Red-F0X (Panin Stanislav)
# Data create: 14.08.2021

# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
def calculate():
    while True:
        val = input('Enter math operation: ')
        if '+' in val:
            val = val.split('+')
            print(int(val[0]) + int(val[1]))
        elif '-' in val:
            val = val.split('-')
            print(int(val[0]) - int(val[1]))
        elif '*' in val:
            val = val.split('*')
            print(int(val[0]) * int(val[1]))
        elif '/' in val:
            val = val.split('/')
            try:
                print(int(val[0]) / int(val[1]))
            except ZeroDivisionError:
                print('You cannot divide by zero')
        elif '0' in val:
            print('END')
            break
        else:
            print('Error, to finish enter \'0\' or enter symbol math operator.')


# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def even_odd(num: int):
    """
    Enter num for count even and odd in number.
    :param num:
    :return count even, odd:
    """
    even = len([el for el in list(map(int, str(num))) if not el & 1])
    odd = len([el for el in list(map(int, str(num))) if el & 1])
    return even, odd


# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
def reverse_num(num: int):
    """
    Enter num for reverse.
    :param num:
    :return:
    """
    while True:
        try:
            return int(str(num)[::-1])
        except ValueError:
            print('Please, enter number: ')


# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры
def sum_elements():
    """
    Input in func. Find sum elements.
    :return:
    """
    print('To start just enter the number. To complete enter "=" .')
    res = 0
    while True:
        item = input('Enter your next number: ')
        try:
            item = float(item)
            res += item
        except ValueError:
            if '=' in item:
                return round(res, 2)
            else:
                print('Error, enter number or "=" ')


# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
def ASCII_symbols(start, end):
    for el in range(start, end + 1):
        print(f'{el}-{chr(el)}', end=' ')
        if el % 10 == 0:
            print('\n')


# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число
def game_guess_num(start: int, end: int):
    import random as r
    end_step = 10
    step = 1
    hide_num = r.randint(start, end)
    print('Угадай число, у тебя 10 попыток.')
    while step <= end_step:
        player = int(input('Введите число: '))
        if player == hide_num:
            print(f'Win! Совершено {step} попыток.')
            break
        elif player > hide_num:
            print(f'Число меньше  Это {step} попытка.')
        else:
            print(f'Число больше. Это {step} попытка.')
        step += 1
        if step == end_step + 1:
            print(f'Это {hide_num}, вы проиграли!')


# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
def equality_nat_num(*nums):
    """
    Сheck that for the set of natural numbers the equality.
    :param nums:
    :return:
    """

    # Вычислить отдельно левую и правую части и сравнить их.
    nums = sum(nums)
    left_sum = 0
    for item in range(1, nums + 1):
        left_sum += item
    res_right = nums * (nums + 1) // 2
    if left_sum == res_right:
        print('Равенство выполняется')
    else:
        print('Нет равенства')


# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
def count_choice_num():
    """
    In func input. Enter nums for find user num in list.
    :return:
    """
    while True:
        try:
            enter_nums = list(map(int, input('Enter your numbers through a space: ').split()))
            break
        except ValueError:
            print('Please, enter numbers through a space')
    find_num = input('Enter num for find: ')

    count_repeat_num = 0
    for item in enter_nums:
        if find_num in str(item):
            count_repeat_num += 1
    print(count_repeat_num)


#  Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#  Вывести на экран это число и сумму его цифр
def max_num_sum_opds(nums: list):
    return max(nums), sum(list(map(int, str(max(nums)))))


if __name__ == '__main__':
    calculate()

    count_even, count_odd = even_odd(645897312)
    print(f'Чётных {count_even} и {count_odd} нечётных чисел.')

    print(reverse_num(11651))

    print(sum_elements())

    ASCII_symbols(32, 127)

    game_guess_num(0, 100)

    equality_nat_num(141, 142)

    count_choice_num()

    el_ls = int(input('Enter count elements: '))
    arrays = []
    for el in range(1, el_ls + 1):
        arrays.append(int(input(f'Enter {el}\'s number: ')))

    max_number, sum_opd = max_num_sum_opds(arrays)
    print(f'Greatest number {max_number}, sum of numbers is {sum_opd}')
