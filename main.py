import matplotlib.pyplot as plt
from genetic_algoritm import GeneticAlgoritm
from keys import Keys
import test
import backpack_dp


def solve_backpack(numberTest=1):
    if not (1 <= numberTest <= len(test.TestBackpackDp.inputData)):
        print(f'not 1 <= numberTest({numberTest}) <= {len(test.TestBackpackDp.inputData)} (backpack)')
        return None

    n, s, m, c = test.TestBackpackDp.inputData[numberTest - 1]
    maxC, numbersThings = backpack_dp.solve(n, s, m, c)

    print('backpack_dp:')
    print(maxC)
    print(*numbersThings)

    print()
    keys = Keys.get_keys_backpack(n, s, m, c, countMutation=1, countPointCross=1)
    ga = GeneticAlgoritm(
        size=10,
        k1=0.5,
        k2=0.5,
        keys=keys
    )

    ga.start(1000)
    maxC, code = ga.answer
    numbersThings = [i + 1 for i in range(n) if code[i] == 1]

    print('backpack_ga:')
    print(maxC)
    print(*numbersThings)

    plt.plot(range(len(ga.bestFitnesses)), ga.bestFitnesses)
    plt.show()


def main():
    solve_backpack(6)
    print()


if __name__ == '__main__':
    main()
