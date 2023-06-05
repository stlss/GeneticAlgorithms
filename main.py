import genetic_algoritm
import test
import backpack_dp


def solve_backpack(numberTest=1):
    n, s, m, c = test.TestBackpackDp.inputData[numberTest - 1]
    maxC, numbersThings = backpack_dp.solve(n, s, m, c)

    print(maxC)
    print(*numbersThings)


def main():
    solve_backpack(3)


if __name__ == '__main__':
    main()
