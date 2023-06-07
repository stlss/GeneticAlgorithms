""" Задача коммивояжёра

Описание:
Дано n городов, даны расстояния между городами.
Необходимо найти кратчайший путь, проходящий через все города и возврающийся в исходный город.

Входные данные:
В первой строке вводится число N - число городов.
В следующих n строках вводится n не отрицательных чисел.
j-ое число в i-ой строке - расстояние между i-ым и j-ым городами.
0 - расстояния между городами нет.

Выходные данные:
В первой строке длина кратчайшего пути.
Во второй строке описание кратчайшего пути - последовательность городов (исходный город в конце не дублируется).
"""

from itertools import permutations


def solve(n: int, d: list[list[int]]):
    ps = list(permutations(range(n), n))

    minDistance = float('inf')
    cities = list()

    for p in ps:
        distance = 0
        for i in range(n - 1):
            distance += d[p[i]][p[i + 1]]
        distance += d[p[-1]][p[0]]

        if distance < minDistance:
            minDistance = distance
            cities = p

    cities = list(map(lambda city: city + 1, cities))

    return minDistance, cities


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline())
        d = [[int(x) for x in file.readline().split()] for _ in range(n)]

    minDistance, cities = solve(n, d)

    with open('output.txt', 'w') as file:
        file.write(str(minDistance) + '\n')
        file.write(' '.join(list(map(str, cities))))


if __name__ == '__main__':
    main()
