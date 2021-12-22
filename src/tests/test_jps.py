import unittest
from unittest.case import TestCase
from pathfinding.aStar import AStar

from utils.FileManager import FileManager
from pathfinding.pathManager import PathManager
from pathfinding.jps import JPS


class TestJPS(unittest.TestCase):
    def setUp(self):
        self.dummy_jps = JPS()
        self.file_man = FileManager()

    def test_jps_finds_jump_points(self):
        loaded_map = self.file_man.open_file(
            "assets/maps/tests/jps_jump_points.csv"
        )
        correct_jump_points = [
            (4, 0),
            (0, 14),
            (2, 2),
        ]

        path_man = PathManager(loaded_map, True)
        start_node = path_man.graph.nodes[(0, 0)]
        end_node = path_man.graph.nodes[(15, 15)]        
        
        self.dummy_jps.start_node_origin = (0, 0)
        self.dummy_jps.a_star = AStar()
        self.dummy_jps.jump_point_directions = {}

        result = self.dummy_jps.identify_successors(start_node, end_node)

        connection_origins = list(map(lambda x: x.origin, result))

        self.assertCountEqual(correct_jump_points, connection_origins)