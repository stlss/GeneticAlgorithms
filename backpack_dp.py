"""" Задача о рюкзаке с ценным предметами.

Описание:
Дано N предметов массой m1, ..., mN и стоимостью c1, ..., cN соответственно.
Ими наполняют рюкзак, который выдерживает вес не более S. Какую наибольшую стоимость могут иметь предметы в рюкзаке?

Входные данные:
В первой строке вводится натуральное число N и натуральное число S.
Во второй строке вводятся N натуральных чисел mi.
Во третьей строке вводятся N натуральных чисел сi.

Выходные данные:
В первой строке выводится наибольшая возможная стоимость рюкзака.
Во второй строке номера предметов, которые нужно положить в рюкзак,
чтобы получить максимальную стоимость, в порядке возрастания.
"""


def solve(n: int, s: int, m: list[int], c: list[int]) -> tuple[int, list[int]]:
    # Динамика, dp[i] - наибольшая стоимость рюкзака весом i.
    dp = [-1] * (s + 1)
    dp[0] = 0  # Стоимость пустого рюкзака (рюкзак весом 0) - 0.

    # Битовые маски, bs[i] - битовая последовательность предметов рюкзака с весом i.
    # j-ый бит последовательности i - находится ли j-ый предмет в рюкзаке весом i.
    bs = [0] * (s + 1)

    for i in range(n):
        # Кортежи рюкзаков, которые нужно обновить.
        lstTpl: list[tuple[int, int, int]] = list()

        for j in range(s - m[i] + 1):
            if dp[j] != -1 and dp[j] + c[i] > dp[j + m[i]]:
                k = j + m[i]  # Вес рюкзака, который нужно обновить.
                newC = dp[j] + c[i]  # Новая стоимость рюкзака весом k.
                newB = bs[j] | (1 << i)  # Новая битовая последовательность рюкзака весом k.
                lstTpl.append((k, newC, newB))

        for tpl in lstTpl:
            k, newC, newB = tpl
            dp[k] = newC
            bs[k] = newB

    # Получаем максимальную стоимость рюкзака и его вес.
    maxC = index = 0
    for i in range(s + 1):
        if dp[i] > maxC:
            maxC = dp[i]
            index = i

    # Получаем номера вещей, которые лежат в рюкзаке весом index.
    numbersThings: list[int] = list()
    for i in range(n):
        if (bs[index] >> i & 1) == 1:
            numbersThings.append(i + 1)

    return maxC, numbersThings


def main():
    with open('input.txt', 'r') as file:
        n, s = map(int, file.readline().split())
        m = list(map(int, file.readline().split()))
        c = list(map(int, file.readline().split()))

    maxC, numbersThings = solve(n, s, m, c)

    with open('output.txt', 'w') as file:
        file.write(str(maxC) + '\n')
        # file.write(' '.join(list(map(str, numbersThings))) + '\n')

    # https://contest.yandex.ru/contest/49078/problems/B/


if __name__ == '__main__':
    main()
