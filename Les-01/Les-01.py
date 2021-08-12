# Les 01
# Author: Red-F0X (Panin Stanislav)
# Data create: 11.08.2021


# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def sum_diff_values(value_x: int, value_y: int):
    """
    Sum and difference three-digit two values from user.
    :param value_x:
    :param value_y:
    :return:
    """
    while True:
        if len(str(value_x)) < 3 or len(str(value_y)) < 3 \
                or len(str(value_x)) > 3 or len(str(value_y)) > 3:
            print('Please enter three-digit number!')
            value_x = int(input('Enter first number: '))
            value_y = int(input('Enter second number: '))
        else:
            return f'The sum is {value_x + value_y}. The difference is {value_x - value_y}'


# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.
def bit_operations():
    x = 5
    y = 6

    # резултат будет из бит в позициях операндов "x" вычисляется с битами в позициях второго операндов "y"
    # каждый  операнд рассматривается как набор бит, из которых выполняется побитовая операция
    print(
        f'{x & y} - Результат побитого логического "AND"')  # если бит обоих операндов равен 1 в результат записывается 1 иначе 0
    print(
        f'{x ^ y} - Результат побитого исключающего ИЛИ "XOR"')  # если бит операндов совпадает, результат равен 0 иначе 1
    print(f'{x | y} - Результат побитого ИЛИ "OR"')  # если хотябы один из бит равен 1, результат равен 1

    print(f'{x << 2} - Результата смещения влево на 2 бита ({bin(x << 2)})')
    print(f'{x >> 2} - Результат смещения впрво на 2 бита ({bin(x >> 2)})')


# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
def equation_line(x1: float, y1: float, x2: float, y2: float):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return f'y = {k}*x + {b}'


# Написать программу, которая генерирует в указанных пользователем границах:
#    случайное целое число;
#    случайное вещественное число;
#    случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

def rand_symbol(start, end):
    """
    Generation of a random number or symbol, depending on the range.

    :param start:
    :param end:
    :return:
    """
    import random as r
    if isinstance(start, str) and isinstance(end, str):
        return chr(r.randint(ord(start), ord(end)))
    elif isinstance(start, float) or isinstance(end, float):
        return r.uniform(start, end)
    else:
        return r.randint(start, end)


# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
def num_alphabet(first_val: str, second_val: str):
    """
    On what places of the alphabet are and how many characters between
    :param first_val:
    :param second_val:
    :return:
    """
    el_1 = ord(first_val) - ord('a') + 1
    el_2 = ord(second_val) - ord('a') + 1
    distance = abs(el_2 - el_1 - 1)
    return f'Позиции букв: {el_1} и {el_2}. Между буквами символов: {distance} '


# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def letter_num(num: int):
    """
    Letter from number position on alphabet.
    :param num:
    :return:
    """
    if abs(num) > 26 or num == 0:
        let = ord('a') + 26 - 1
    else:
        let = ord('a') + abs(num) - 1
    return chr(let)


# 7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
def exsist_triangle(a: int, b: int, c: int):
    """
    Determines the existence of a triangle and its type.
    :param a:
    :param b:
    :param c:
    :return:
    """
    if a + b > c and a + c > b and b + c > a:
        print('Триугольник существует')
        if a == b == c:
            print('Триугольник равносторонний')
        elif a == b or a == c or b == c:
            print('Триугольник равнобедренный')
        else:
            print('Триугольник разносторонний')
    else:
        print('Триугольник не существует')


# Определить, является ли год, который ввел пользователем, високосным или невисокосным.\

#     Если год не делится на 4, значит он обычный.
#     Иначе надо проверить не делится ли год на 100.
#     Если не делится, значит это не столетие и можно сделать вывод, что год високосный.
#     Если делится на 100, значит это столетие и его следует проверить его делимость на 400.
def leap_year(year: int):
    if year % 4 != 0:
        print('Not leap year')
    elif year % 100 == 0 and year % 400 != 0:
        print('Not leap year')
    else:
        print('Leap year')


# Вводятся три разных числа. Найти, какое из них является средним.
def medium_num():
    """
    Enter 3 nums in func, for search medium num.
    :return:
    """
    a = int(input('Enter num: '))
    b = int(input('Enter num: '))
    c = int(input('Enter num: '))
    if b < a < c or c < a < b:
        print(f'{a}')
    elif a < b < c or c < b < a:
        print(f'{b}')
    else:
        print(f'{c}')


def medium_2(a: int, b: int, c: int):
    """
    Second variant search medium num.
    :param a:
    :param b:
    :param c:
    :return:
    """
    print(sorted((a, b, c))[1])


if __name__ == '__main__':
    val_one = int(input('Enter first number: '))
    val_two = int(input('Enter second number: '))
    print(sum_diff_values(val_one, val_two), '\n')

    bit_operations()

    print('Enter Point A coordinates')
    pos_x1 = float(input('Enter latitude: '))
    pos_y1 = float(input('Enter longitude: '))
    print('Enter Point B coordinates')
    pos_x2 = float(input('Enter latitude: '))
    pos_y2 = float(input('Enter longitude:: '))
    print(equation_line(pos_x1, pos_y1, pos_x2, pos_y2), '\n')

    print(rand_symbol(22.1, 30), '\n')

    let_1 = str(input('Enter letter: '))
    let_2 = str(input('Enter second letter: '))
    print(num_alphabet(let_1, let_2), '\n')
    print(letter_num(int(input('Enter number letter: '))), '\n')

    side_a = int(input('Enter triangle distance side A: '))
    side_b = int(input('Enter triangle distance side B: '))
    side_c = int(input('Enter triangle distance side C: '))
    exsist_triangle(side_a, side_b, side_c)

    medium_num()
    medium_2(101, 200, 3)
