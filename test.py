import unittest
import backpack_dp


class TestBackpackDp(unittest.TestCase):
    inputData = (
        (4, 6, [2, 4, 1, 2], [7, 2, 5, 1]),
        (1, 597, [18], [16]),
        (7, 30, [4, 11, 10, 9, 5, 18, 4], [12, 2, 10, 7, 24, 1, 14])
    )

    outputData = (
        (13, [1, 3, 4]),
        (16, [1]),
        (60, [1, 3, 5, 7])
    )

    def test1(self):
        indexTest = 0
        n, s, m, c = TestBackpackDp.inputData[indexTest]
        expected = TestBackpackDp.outputData[indexTest]
        result = backpack_dp.solve(n, s, m, c)
        self.assertEqual(expected, result)

    def test2(self):
        indexTest = 1
        n, s, m, c = TestBackpackDp.inputData[indexTest]
        expected = TestBackpackDp.outputData[indexTest]
        result = backpack_dp.solve(n, s, m, c)
        self.assertEqual(expected, result)

    def test3(self):
        indexTest = 2
        n, s, m, c = TestBackpackDp.inputData[indexTest]
        expected = TestBackpackDp.outputData[indexTest]
        result = backpack_dp.solve(n, s, m, c)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
