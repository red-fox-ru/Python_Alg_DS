# Les 08
# Author: Red-F0X (Panin Stanislav)
# Data create: 06.09.2021


# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
def hash_substing(text):
    import hashlib

    sum_substring = set()
    for start in range(len(text)):
        for decrease in range(len(text), start, -1):
            hash_str = hashlib.sha1(text[start:decrease].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)

    return len(sum_substring) - 1


# Закодируйте любую строку из трех слов по алгоритму Хаффмана
import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    head = []
    for el, freq in Counter(s).items():
        head.append((freq, len(head), Leaf(el)))
    heapq.heapify(head)
    count = len(head)
    while len(head) > 1:
        freq1, _count1, left = heapq.heappop(head)
        freq2, _count2, right = heapq.heappop(head)
        heapq.heappush(head, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if head:
        [(_freq, _count, root)] = head
        root.walk(code, "")
    return code


if __name__ == '__main__':
    print(hash_substing('abracadabra'))
    print(huffman_encode('hello world huffman'))
