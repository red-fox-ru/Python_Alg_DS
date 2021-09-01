# Les 06
# Author: Red-F0X (Panin Stanislav)
# Data create: 28.08.2021

# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

from memory_profiler import profile
from guppy import hpy
from sys import getsizeof

# -- x64 Win10 --
# ---------------------------------------------------------------------------------------------------------------------
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     15     19.7 MiB     19.7 MiB           1   @profile
#     16                                         def hexadecimal_sum(first, second):
#     23     19.7 MiB      0.0 MiB           1       hex_num
#     24     19.7 MiB      0.0 MiB           7       one
#     25     19.7 MiB      0.0 MiB           7       two
#     26     19.7 MiB      0.0 MiB           1       result_sum
#     28     19.7 MiB      0.0 MiB           1       if len(first) < len(second):
#     29                                                 first, second = second, first
#     30                                                 one, two = two, one
#     32     19.7 MiB      0.0 MiB           1       one_index = one.copy()
#     33     19.7 MiB      0.0 MiB           1       step = len(second)
#     34     19.7 MiB      0.0 MiB           1       rate = 0
#     35     19.7 MiB      0.0 MiB           4       for el_sum in range(0, len(first)):
#     36     19.7 MiB      0.0 MiB           4           one_index[el_sum] += two[el_sum] + rate
#     37     19.7 MiB      0.0 MiB           4           if one_index[el_sum] > 15:
#     38     19.7 MiB      0.0 MiB           3               one_index[el_sum] = one_index[el_sum] % 16
#     39     19.7 MiB      0.0 MiB           3               rate
#     40                                                 else:
#     41     19.7 MiB      0.0 MiB           1               rate
#     43     19.7 MiB      0.0 MiB           4           step -= 1
#     44     19.7 MiB      0.0 MiB           4           if step == 0:
#     45     19.7 MiB      0.0 MiB           1               break
#     47     19.7 MiB      0.0 MiB           1       if rate > 0:
#     48     19.7 MiB      0.0 MiB           1           one_index.append(rate)
#     49     19.7 MiB      0.0 MiB           6       for inx in one_index[::-1]:
#     50     19.7 MiB      0.0 MiB           5           result_sum.append(hex_num[inx])
#     52     19.7 MiB      0.0 MiB           1       return result_sum
# ---------------------------------------------------------------------------------------------------------------------

# -- x64 GNU/Linux --
# ---------------------------------------------------------------------------------------------------------------------
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     44     27.3 MiB     27.3 MiB           1   @profile
#     45                                         def hexadecimal_sum(first, second):
#     46                                             """
#     47                                             Find sum two hex value.
#     48                                             :param first:
#     49                                             :param second:
#     50                                             :return:
#     51                                             """
#     52     27.3 MiB      0.0 MiB           1       hex_num
#     53     27.3 MiB      0.0 MiB           7       one = [int(el, 16) for el in first][::-1]
#     54     27.3 MiB      0.0 MiB           7       two = [int(el, 16) for el in second][::-1]
#     55     27.3 MiB      0.0 MiB           1       result_sum = []
#     56
#     57     27.3 MiB      0.0 MiB           1       if len(first) < len(second):
#     58                                                 first, second = second, first
#     59                                                 one, two = two, one
#     60
#     61     27.3 MiB      0.0 MiB           1       one_index = one.copy()
#     62     27.3 MiB      0.0 MiB           1       step = len(second)
#     63     27.3 MiB      0.0 MiB           1       rate = 0
#     64     27.3 MiB      0.0 MiB           4       for el_sum in range(0, len(first)):
#     65     27.3 MiB      0.0 MiB           4           one_index[el_sum] += two[el_sum] + rate
#     66     27.3 MiB      0.0 MiB           4           if one_index[el_sum] > 15:
#     67     27.3 MiB      0.0 MiB           3               one_index[el_sum] = one_index[el_sum] % 16
#     68     27.3 MiB      0.0 MiB           3               rate = 1
#     69                                                 else:
#     70     27.3 MiB      0.0 MiB           1               rate = 0
#     71
#     72     27.3 MiB      0.0 MiB           4           step -= 1
#     73     27.3 MiB      0.0 MiB           4           if step == 0:
#     74     27.3 MiB      0.0 MiB           1               break
#     75
#     76     27.3 MiB      0.0 MiB           1       if rate > 0:
#     77     27.3 MiB      0.0 MiB           1           one_index.append(rate)
#     78     27.3 MiB      0.0 MiB           6       for inx in one_index[::-1]:
#     79     27.3 MiB      0.0 MiB           5           result_sum.append(hex_num[inx])
#     80
#     81     27.3 MiB      0.0 MiB           1       return result_sum

@profile
def hexadecimal_sum(first, second):
    """
    Find sum two hex value.
    :param first:
    :param second:
    :return:
    """
    hex_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
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


# Второй метод подсчёта памяти c getsizeof
# -- x64 Win10 -- и -- x64 GNU/Linux --
# [28, 57, 28] байт
def hexadecimal_mul(first, second):

    loop = int(second, 16)
    result = hex(int(first, 16) + int(first, 16)).replace('0x', '')  # второй вариант суммы 16-ой системы счисления

    for el in range(loop - 2):
        result = hex(int(result, 16) + int(first, 16)).replace('0x', '')

    mem_list = []
    mem_list.append(getsizeof(loop))
    mem_list.append(getsizeof(result))
    mem_list.append(getsizeof(el))
    print(f'Занимаемая память перменными равна {mem_list} байт')
    print('================\n')
    return list(result)


if __name__ == '__main__':
    statistic = hpy()
    print(hexadecimal_sum('ADF0', '9FA2'), '\n')
    print(hexadecimal_mul('ADF0', '9FA2'))

    # 3-й способ
    # x64 Win10
    # Partition of a set of 77224 objects. Total size = 8955176 bytes.
#  Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
#      0  23127  30  2130564  24   2130564  24 str
#      1  17581  23  1223640  14   3354204  37 tuple
#      2   5441   7   961223  11   4315427  48 types.CodeType
#      3    907   1   804704   9   5120131  57 type
#      4  10628  14   779285   9   5899416  66 bytes
#      5   5272   7   716992   8   6616408  74 function
#      6    907   1   471816   5   7088224  79 dict of type
#      7    816   1   356704   4   7444928  83 dict (no owner)
#      8    193   0   333544   4   7778472  87 dict of module
#      9    103   0    94440   1   7872912  88 set

# -- x64 GNU/Linux --
# Partition of a set of 105743 objects. Total size = 12379156 bytes.
    #  Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
    #      0  32873  31  3052727  25   3052727  25 str
    #      1  23727  22  1699240  14   4751967  38 tuple
    #      2   7434   7  1313219  11   6065186  49 types.CodeType
    #      3   1262   1  1148456   9   7213642  58 type
    #      4  14795  14  1136451   9   8350093  67 bytes
    #      5   7191   7   977976   8   9328069  75 function
    #      6   1262   1   632272   5   9960341  80 dict of type
    #      7    272   0   471496   4  10431837  84 dict of module
    #      8   1012   1   467400   4  10899237  88 dict (no owner)
    #      9   1659   2   119448   1  11018685  89 builtins.weakref
    print('\n\n', statistic.heap())
