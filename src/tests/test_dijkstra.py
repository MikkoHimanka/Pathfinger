import unittest

from utils.FileManager import FileManager
from pathfinding.pathManager import PathManager


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.file_man = FileManager()
        self.simple_map = self.file_man.open_file(
            "assets/maps/tests/8x8_simple_map.csv"
        )
        self.simple_map_wall = self.file_man.open_file(
            "assets/maps/tests/8x8_simple_map_wall.csv"
        )

    def test_get_path_returns_correct_simple_diagonal(self):
        correct_path = [
            (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)
        ]

        path_man = PathManager(self.simple_map, True)
        result = path_man.get_path("Dijkstra", [(0, 0), (7, 7)])[0]

        assert (result == correct_path)

    def test_get_path_returns_correct_simple_horizontal(self):
        correct_path = [
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)
        ]

        path_man = PathManager(self.simple_map, True)
        result = path_man.get_path("Dijkstra", [(0, 3), (7, 3)])[0]

        assert (result == correct_path)

    def test_dijkstra_dodges_an_obstacle(self):
        correct_path_len = 8

        path_man = PathManager(self.simple_map, True)
        result = path_man.get_path("Dijkstra", [(0, 0), (0, 7)])[0]

        self.assertEqual(len(result), correct_path_len)

    def test_dijkstra_doesnt_return_full_path_when_failing(self):
        correct_path = []

        path_man = PathManager(self.simple_map_wall, True)
        result = path_man.get_path("Dijkstra", [(0, 0), (7, 0)])[0]

        self.assertEqual(result, correct_path)
