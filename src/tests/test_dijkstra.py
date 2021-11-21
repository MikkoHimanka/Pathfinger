import unittest

from utils.CSVManager import CSVManager
from pathfinding.pathManager import PathManager


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.csv_man = CSVManager()

    def test_get_path_returns_correct_simple(self):
        correct_path = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
        map_as_list = self.csv_man.open_file("assets/maps/tests/8x8_simple_map.csv")
        path_man = PathManager(map_as_list)

        # print(map_as_list)
        for c in path_man.graph.nodes[(5, 6)].connections:
            print(c.origin)

        assert False
