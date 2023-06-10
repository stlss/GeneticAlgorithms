""" Класс ключей, хранящий ссылки функций для генетического алгоритма. """

from collections.abc import Callable
from random import (randint, choices, shuffle)
from copy import deepcopy


class Keys(object):
    def __init__(self,
                 keyGeneration: Callable[[], list[int]],  # Случайная генерация кода особи.
                 keyFitness: Callable[[list[int]], int],  # Вычисление приспособленности особи по коду.
                 keyMutation: Callable[[list[int]], list[int]],  # Мутирование кода особи.
                 keyCross: Callable[[list[int], list[int]], list[int]]  # Скрещивание особей.
                 ):
        self.generation = keyGeneration
        self.fitness = keyFitness
        self.mutation = keyMutation
        self.cross = keyCross

    @staticmethod
    # Возвращает ключи для решения задачи о рюкзаке с ценными предметами.
    def get_keys_backpack(n, s, m, c,
                          countMutation,
                          countPointCross
                          ):

        def keyGeneration():
            return [randint(0, 1) for _ in range(n)]

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
            indexesMutation = choices(indexes, k=randint(1, countMutation))

            for index in indexesMutation:
                code[index] = abs(code[index] - 1)

            return code

        def keyCross(code1, code2):
            code3 = list()

            indexes = range(n + 1)
            indexesPointsCross = choices(indexes, k=randint(1, countPointCross))
            indexesPointsCross.sort()

            firstIndex = 0
            for i in range(len(indexesPointsCross)):
                secondIndex = indexesPointsCross[i]
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

    @staticmethod
    # Возвращает ключи для решения задачи коммивояжёра.
    def get_keys_door_to_door(n, d,
                              countMutation,
                              countPointCross
                              ):

        def keyGeneration():
            code = list(range(n))
            shuffle(code)
            return code

        def keyFitness(code):
            distance = 0

            for i in range(1, n):
                distance -= d[code[i - 1]][code[i]]
            distance -= d[code[-1]][code[0]]

            return distance

        def keyMutation(code):
            indexes = range(n)
            indexesMutation = choices(indexes, k=2 * randint(1, countMutation))

            for i in range(0, len(indexesMutation), 2):
                code[i], code[i + 1] = code[i + 1], code[i]

            return code

        def get_alternative_code(code):
            code = deepcopy(code)[::-1]
            p = list(range(n))

            codeAltertanive = list()

            while len(code) != 0:
                index = p.index(code[-1])
                codeAltertanive.append(index)

                p.remove(code[-1])
                code.pop()

            return codeAltertanive

        def get_natural_code(code):
            code = deepcopy(code)[::-1]
            p = list(range(n))

            codeNatural = list()

            while len(code) != 0:
                index = code[-1]
                codeNatural.append(p[index])

                p.remove(p[index])
                code.pop()

            return codeNatural

        def keyCross(code1, code2):
            code1 = get_alternative_code(code1)
            code2 = get_alternative_code(code2)

            code3 = list()

            indexes = range(n + 1)
            indexesMutation = choices(indexes, k=randint(1, countPointCross))
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

            code3 = get_natural_code(code3)

            return code3

        return Keys(keyGeneration, keyFitness, keyMutation, keyCross)
