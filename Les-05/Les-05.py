# Les 05
# Author: Red-F0X (Panin Stanislav)
# Data create: 25.08.2021


# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

def statistic_enterprise():
    """
    Search for a business where the annual report differs from the average.
    :return:
    """
    enterprise = {}
    mean_year = 0
    low_mean = []
    high_mean = []
    count_shops = int(input('Enter count shops: '))
    store_names = []
    for item in range(1, count_shops + 1):
        store_names.append(input(f'Enter name {item} shop: '))

    for store in store_names:
        year_quarterly = []
        for quarterly in range(1, 5):
            year_quarterly.append(float(input(f'Enter value {quarterly} quarterly {store}: ')))
        mean_year += sum(year_quarterly) / len(year_quarterly)
        enterprise[store] = year_quarterly

    mean_year = mean_year / count_shops

    for el in enterprise:
        if sum(enterprise[el]) / 4 > mean_year:
            high_mean.append(el)
        elif sum(enterprise[el]) / 4 < mean_year:
            low_mean.append(el)

    print(f'Store above-average: {high_mean}')
    print(f'Store below-average: {low_mean}')


def statistic_enterprise_collection():
    """
    User enter keyboard for find average report enterprise. With use collection.
    :return:
    """
    import collections

    Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

    base_enterprise = {}

    count_ent = int(input("Количество предприятий: "))

    for item in range(count_ent):
        name = input(str(item + 1) + '-е предприятие: ')
        profit_q1 = int(input('Прибыль за 1-й квартал: '))
        profit_q2 = int(input('Прибыль за 2-й квартал: '))
        profit_q3 = int(input('Прибыль за 3-й квартал: '))
        profit_q4 = int(input('Прибыль за 4-й квартал: '))
        base_enterprise[name] = Enterprise(
            q1=profit_q1,
            q2=profit_q2,
            q3=profit_q3,
            q4=profit_q4
        )

    total_profit = []
    for profit in base_enterprise.items():
        total_profit.append(sum(profit[1]))

    avg_profit_total = sum(total_profit) / 4 / len(base_enterprise)
    print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

    print('Предприятия, прибыль выше среднего:')
    for name, profit in base_enterprise.items():
        if sum(profit) > avg_profit_total:
            print(name)
    print('Предприятия, прибыль ниже среднего:')
    for name, profit in base_enterprise.items():
        if sum(profit) < avg_profit_total:
            print(name)


# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

hex_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def hexadecimal_sum(first, second):
    """
    Find sum two hex value.
    :param first:
    :param second:
    :return:
    """
    one = [int(el, 16) for el in first][::-1]
    two = [int(el, 16) for el in second][::-1]
    result_sum = []

    if len(first) < len(second):
        first, second = second, first
        one, two = two, one

    one_index = one.copy()
    step = len(second)
    rate = 0
    for el_sum in range(0, len(first)):
        one_index[el_sum] += two[el_sum] + rate
        if one_index[el_sum] > 15:
            one_index[el_sum] = one_index[el_sum] % 16
            rate = 1
        else:
            rate = 0

        step -= 1
        if step == 0:
            break

    if rate > 0:
        one_index.append(rate)
    for inx in one_index[::-1]:
        result_sum.append(hex_num[inx])

    return result_sum


def hexadecimal_mul(first, second):
    loop = int(second, 16)
    result = hex(int(first, 16) + int(first, 16)).replace('0x', '')  # второй вариант суммы 16-ой системы счисления

    for _ in range(loop - 2):
        result = hex(int(result, 16) + int(first, 16)).replace('0x', '')
    return list(result)


if __name__ == '__main__':
    statistic_enterprise()
    statistic_enterprise_collection()
    print(hexadecimal_sum('F4240', '1E480'))
    print(hexadecimal_mul('F4240', 'FFFFF'))
