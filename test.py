import unittest
import backpack_dp


class TestBackpackDp(unittest.TestCase):
    inputData = (
        (4, 6, [2, 4, 1, 2], [7, 2, 5, 1]),
        (1, 597, [18], [16]),
        (7, 30, [4, 11, 10, 9, 5, 18, 4], [12, 2, 10, 7, 24, 1, 14]),
        (3, 100, [10, 10, 10], [100, 100, 100]),
        (1, 10, [100], [100])
    )

    outputData = (
        (13, [1, 3, 4]),
        (16, [1]),
        (60, [1, 3, 5, 7]),
        (300, [1, 2, 3]),
        (0, [])
    )

    @staticmethod
    def get_data_test(indexTest):
        n, s, m, c = TestBackpackDp.inputData[indexTest]
        expected = TestBackpackDp.outputData[indexTest]
        result = backpack_dp.solve(n, s, m, c)
        return expected, result

    def test1(self):
        expected, result = TestBackpackDp.get_data_test(0)
        self.assertEqual(expected, result)

    def test2(self):
        expected, result = TestBackpackDp.get_data_test(1)
        self.assertEqual(expected, result)

    def test3(self):
        expected, result = TestBackpackDp.get_data_test(2)
        self.assertEqual(expected, result)

    def test4(self):
        expected, result = TestBackpackDp.get_data_test(3)
        self.assertEqual(expected, result)

    def test5(self):
        expected, result = TestBackpackDp.get_data_test(4)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
