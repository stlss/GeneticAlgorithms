""" Задача коммивояжёра. """

from itertools import permutations


# Решение полным перебором за О(2 ^ n).
def solve_bust(n: int,  # Число городов .
               d: list[list[int]]  # Матрица не отрицательных расстояний (0 - пути нет).
               ) -> tuple[int, list[int]]:  # Минимальная длина пути, список городов.

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

    minDistance, cities = solve_bust(n, d)

    with open('output.txt', 'w') as file:
        file.write(str(minDistance) + '\n')
        file.write(' '.join(list(map(str, cities))))


if __name__ == '__main__':
    main()
