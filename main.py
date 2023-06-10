from genetic_algoritm import (GeneticAlgoritm, Keys)
import matplotlib.pyplot as plt
import backpack
import door_to_door
import test


# Решение рюкзака при помощи дп и га.
def solve_backpack(numberTest: int = 1):
    if not (1 <= numberTest <= len(test.TestBackpackDp.inputData)):
        print(f'not 1 <= numberTest({numberTest}) <= {len(test.TestBackpackDp.inputData)} (backpack)')
        return None

    n, s, m, c = test.TestBackpackDp.inputData[numberTest - 1]

    maxC, numbersThings = backpack.solve_dp(n, s, m, c)

    print('backpack_dp:')
    print(maxC)
    print(*numbersThings)

    print()

    keysBackpack = Keys.get_keys_backpack(n, s, m, c, countMutation=1, countPointCross=1)
    ga = GeneticAlgoritm(size=10, k1=0.5, k2=0.3, keys=keysBackpack)

    ga.start(20)
    maxC, code = ga.answer
    numbersThings = [i + 1 for i in range(n) if code[i] == 1]

    print('backpack_ga:')
    print(maxC)
    print(*numbersThings)

    plt.title('Рюкзак')
    plt.xlabel('Поколения')
    plt.ylabel('Стоимость')

    plt.plot(range(len(ga.bestFitnesses)), ga.bestFitnesses)
    plt.plot(range(len(ga.worstFitnesses)), ga.worstFitnesses)

    plt.legend(['Стоимость лучшей особи в поколении', 'Стоимость худшей особи в поколении'])

    plt.show()


# Решение коммивояжёры перебором и га.
def solve_door_to_door(numberTest: int = 1):
    if not (1 <= numberTest <= len(test.TestDoorToDoorBust.inputData)):
        print(f'not 1 <= numberTest({numberTest}) <= {len(test.TestDoorToDoorBust.inputData)} (door_to_door)')

    n, d = test.TestDoorToDoorBust.inputData[numberTest - 1]

    minDistance, cities = door_to_door.solve_bust(n, d)

    print('door_to_door_bust:')
    print(minDistance)
    print(*cities)

    print()

    keysDoorToDoor = Keys.get_keys_door_to_door(n, d, countMutation=1, countPointCross=1)

    ga = GeneticAlgoritm(size=5, k1=0.5, k2=0.3, keys=keysDoorToDoor)
    ga.start(100)

    minDistance, code = ga.answer

    minDistance = abs(minDistance)
    cities = [x + 1 for x in code]

    print('door_to_door_ga:')
    print(minDistance)
    print(*cities)

    plt.title('Коммивояжёр')
    plt.xlabel('Поколения')
    plt.ylabel('Путь')

    plt.plot(range(len(ga.bestFitnesses)), list(map(lambda x: -x, ga.bestFitnesses)))
    plt.plot(range(len(ga.worstFitnesses)), list(map(lambda x: -x, ga.worstFitnesses)))

    plt.legend(['Путь лучшей особи в поколении', 'Путь худшей особи в поколении'])

    plt.show()


def main():
    solve_backpack(numberTest=7)
    print()
    solve_door_to_door(numberTest=4)


if __name__ == '__main__':
    main()
