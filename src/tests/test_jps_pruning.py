import unittest

from utils.FileManager import FileManager
from pathfinding.pathManager import PathManager
from pathfinding.jps import JPS
from pathfinding.aStar import AStar


class TestJPSPruning(unittest.TestCase):
    def setUp(self):
        self.dummy_jps = JPS()
        self.file_man = FileManager()

    def test_forced_neighbors_going_up_both_sides(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_vert_both.csv"
        )
        correct_neighbor_coords = [
            (0, 0),
            (1, 0),
            (2, 0),
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(1, 2)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_going_up(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_vert.csv"
        )
        correct_neighbor_coords = [
            (0, 0),
            (1, 0),
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(1, 2)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_going_down_both_sides(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_vert_both.csv"
        )
        correct_neighbor_coords = [
            (0, 2),
            (1, 2),
            (2, 2),
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(1, 0)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_going_down(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_vert.csv"
        )
        correct_neighbor_coords = [
            (0, 2),
            (1, 2),
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(1, 0)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_ne_both(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_diag_ne_both.csv"
        )
        correct_neighbor_coords = [
            (1, 0),
            (2, 0),
            (2, 1),
            (0, 0),
            (2, 2)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(0, 2)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_ne(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_diag_ne.csv"
        )
        correct_neighbor_coords = [
            (1, 0),
            (2, 0),
            (2, 1),
            (0, 0),
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(0, 2)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_nw_both(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_diag_nw_both.csv"
        )
        correct_neighbor_coords = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (0, 2)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(2, 2)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_nw(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_diag_nw.csv"
        )
        correct_neighbor_coords = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(2, 2)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_se_both(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_diag_se_both.csv"
        )
        correct_neighbor_coords = [
            (2, 0),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(0, 0)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_se(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_diag_se.csv"
        )
        correct_neighbor_coords = [
            (2, 0),
            (2, 1),
            (1, 2),
            (2, 2)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(0, 0)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_sw_both(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_diag_sw_both.csv"
        )
        correct_neighbor_coords = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(2, 0)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_sw(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_diag_sw.csv"
        )
        correct_neighbor_coords = [
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(2, 0)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_empty_se(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_empty.csv"
        )
        correct_neighbor_coords = [
            (2, 1),
            (2, 2),
            (1, 2)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(0, 0)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_hor(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_empty.csv"
        )
        correct_neighbor_coords = [
            (2, 1)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(0, 1)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)

    def test_forced_neighbors_diagonal_vert(self):
        jps_forced_vert = self.file_man.open_file(
            "assets/maps/tests/jps_forced_empty.csv"
        )
        correct_neighbor_coords = [
            (1, 0)
        ]
        path_man = PathManager(jps_forced_vert, True)
        node = path_man.graph.nodes[(1, 1)]

        self.dummy_jps.a_star = AStar()
        self.dummy_jps.forced_neighbors = set()
        self.dummy_jps.previous = {}
        self.dummy_jps.previous[node] = path_man.graph.nodes[(1, 2)]

        pruned = self.dummy_jps.prune_neighbors(node)
        pruned = list(map(lambda x: x.origin, pruned))

        self.assertCountEqual(correct_neighbor_coords, pruned)
