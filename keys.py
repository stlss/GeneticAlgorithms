""" Класс ключей, хранящий ссылки функций для генетического алгоритма. """

from collections.abc import Callable
import random


class Keys(object):
    def __init__(self,
                 keyGeneration: Callable[[], list[int]],  # Случайная генерация кода особи.
                 keyFitness: Callable[[list[int]], int],  # Вычисление приспособленности особи по коду.
                 keyMutation: Callable[[list[int]], None],  # Мутирование кода особи.
                 keyCross: Callable[[list[int], list[int]], list[int]]  # Скрещивание особей.
                 ):
        self.generation = keyGeneration
        self.fitness = keyFitness
        self.mutation = keyMutation
        self.cross = keyCross

    # Возвращает ключи для решения задачи о рюкзаке с ценными предметами.
    @staticmethod
    def get_keys_backpack(n, s, m, c,
                          countMutation,
                          countPointCross):
        def keyGeneration():
            return [random.randint(0, 1) for _ in range(n)]

        def keyFitness(code):
            sumM = sumC = 0

            for i in range(n):
                if code[i] == 1:
                    sumM += m[i]
                    sumC += c[i]

            if sumM > s:
                return 0
            return sumC

        def keyMutation(code):
            indexes = range(n)
            indexesMutation = random.choices(indexes, k=random.randint(1, countMutation))

            for index in indexesMutation:
                code[index] = abs(code[index] - 1)

            return code

        def keyCross(code1, code2):
            code3 = list()

            indexes = range(n + 1)
            indexesMutation = random.choices(indexes, k=random.randint(1, countPointCross))
            indexesMutation.sort()

            firstIndex = 0
            for i in range(len(indexesMutation)):
                secondIndex = indexesMutation[i]
                if i % 2 == 0:
                    code3 += code1[firstIndex:secondIndex]
                else:
                    code3 += code2[firstIndex:secondIndex]
                firstIndex = secondIndex

            if countPointCross % 2 == 0:
                code3 += code1[firstIndex:]
            else:
                code3 += code2[firstIndex:]

            return code3

        return Keys(keyGeneration, keyFitness, keyMutation, keyCross)
