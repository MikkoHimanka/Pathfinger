import unittest

from utils.CSVManager import CSVManager
from pathfinding.pathManager import PathManager


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.csv_man = CSVManager()
        self.simple_map = self.csv_man.open_file(
            "assets/maps/tests/8x8_simple_map.csv"
        )
        self.simple_map_wall = self.csv_man.open_file(
            "assets/maps/tests/8x8_simple_map_wall.csv"
        )

    def test_get_path_returns_correct_simple_diagonal(self):
        correct_path = [
            (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)
        ]

        path_man = PathManager(self.simple_map)
        result = path_man.get_path("Dijkstra", [(0, 0), (7, 7)])

        assert (result == correct_path)

    def test_get_path_returns_correct_simple_horizontal(self):
        correct_path = [
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)
        ]

        path_man = PathManager(self.simple_map)
        result = path_man.get_path("Dijkstra", [(0, 3), (7, 3)])

        assert (result == correct_path)

    def test_dijkstra_dodges_an_obstacle(self):
        correct_path = [
            (0, 0), (1, 1), (1, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]

        path_man = PathManager(self.simple_map)
        result = path_man.get_path("Dijkstra", [(0, 0), (0, 7)])

        self.assertEqual(result, correct_path)

    def test_dijkstra_doesnt_return_full_path_when_failing(self):
        correct_path = [
            (7, 0)
        ]

        path_man = PathManager(self.simple_map_wall)
        result = path_man.get_path("Dijkstra", [(0, 0), (7, 0)])

        self.assertEqual(result, correct_path)
