import unittest

from utils.mathTools import distance


class TestMathTools(unittest.TestCase):
    def test_distance_returns_correct_values_diagonals(self):
        points = [
            [(1, 1), (2, 0)],
            [(1, 1), (2, 2)],
            [(1, 1), (0, 2)],
            [(1, 1), (0, 0)],
        ]

        correct_diagonal_distance = 1.414

        for diagonal in points:
            res = distance(diagonal[0], diagonal[1])
            self.assertAlmostEqual(correct_diagonal_distance, res, 3)

    def test_distance_returns_correct_values_nondiagonal(self):
        points = [
            [(1, 1), (1, 0)],
            [(1, 1), (1, 2)],
            [(1, 1), (0, 1)],
            [(1, 1), (2, 1)],
        ]

        correct_distance = 1

        for nondiagonal in points:
            res = distance(nondiagonal[0], nondiagonal[1])
            self.assertEqual(correct_distance, res)
