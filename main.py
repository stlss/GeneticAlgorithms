import genetic_algoritm
import test
import backpack_dp


def solve_backpack(numberTest=1):
    if not (1 <= numberTest <= len(test.TestBackpackDp.inputData)):
        print(f'not 1 <= numberTest({numberTest}) <= {len(test.TestBackpackDp.inputData)} (backpack)')
        return None

    n, s, m, c = test.TestBackpackDp.inputData[numberTest - 1]
    maxC, numbersThings = backpack_dp.solve(n, s, m, c)

    print(maxC)
    print(*numbersThings)


def main():
    solve_backpack(5)
    print()


if __name__ == '__main__':
    main()
