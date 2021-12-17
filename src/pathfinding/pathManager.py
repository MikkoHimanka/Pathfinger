from math import sqrt
from sys import maxsize

from pathfinding.dijkstra import Dijkstra
from pathfinding.aStar import AStar
from pathfinding.greedyBF import GreedyBF
from pathfinding.idaStar import IdaStar
from pathfinding.jps import JPS


class Node:
    def __init__(self, origin, max_size):
        self.origin = origin
        self.visited = False
        self.connections = []
        self.distance = maxsize
        self.max_size = max_size
        self.previous_node = None

    def __repr__(self) -> str:
        delimiter = ', '
        return (
            '(' + delimiter.join([str(value) for value in self.origin]) + ')'
        )

    def __gt__(self, other):
        return self.origin > other.origin

    def add_neighbors(self, origin, map_as_list, nodes, allow_diagonal):
        '''Lisaa Noden naapurit connections listaan'''

        x = origin[0]
        y = origin[1]

        neighbor_deltas = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1)
        ]

        if allow_diagonal:
            neighbor_deltas += [
                (x-1, y-1),
                (x+1, y-1),
                (x-1, y+1),
                (x+1, y+1)
            ]

        if (x + y) % 2 == 0:
            neighbor_deltas.reverse()

        neighbor_deltas = list(
            filter(lambda x: (x[0] >= 0 and x[1] >= 0), neighbor_deltas)
        )
        neighbor_deltas = list(
            filter(lambda x: (x[0] < self.max_size and x[1] < self.max_size), neighbor_deltas)
        )

        for coord in neighbor_deltas:
            self.insert_neighbour(
                coord,
                map_as_list,
                nodes,
                self.max_size
            )

    def insert_neighbour(self, coord, map_as_list, nodes, upper_limit):
        map_value = map_as_list[
            (coord[1] * upper_limit) + coord[0]
        ]

        if map_value == "0":
            if coord in nodes.keys():
                neighbour_node = nodes[coord]
            else:
                neighbour_node = Node(coord, upper_limit)
                nodes[coord] = neighbour_node

            self.connections.append(neighbour_node)


class Graph:
    def __init__(self, map_as_list, allow_diagonal):
        self.nodes = {}
        self.allow_diagonal = allow_diagonal
        length = int(sqrt(len(map_as_list)))
        for y in range(length):
            for x in range(length):
                if (x, y) in self.nodes.keys():
                    node = self.nodes[(x, y)]
                else:
                    node = Node((x, y), length)
                    self.nodes[(x, y)] = node

                node.add_neighbors(
                    (x, y),
                    map_as_list,
                    self.nodes,
                    allow_diagonal
                )

    def clean_up(self):
        for node in self.nodes.values():
            node.distance = maxsize
            node.visited = False
            node.previous_node = None
            # try:
            #     del node.previous_node
            # except AttributeError:
            #     continue


class PathManager:
    def __init__(self, map_as_list, allow_diagonal):
        self.algorithms = {
            "Dijkstra": Dijkstra(),
            "Greedy Best-First": GreedyBF(),
            "A*": AStar(),
            "IDA*": IdaStar(),
            "JPS": JPS()
        }
        self.diagonal = allow_diagonal
        self.init_graph(map_as_list, allow_diagonal)

    def init_graph(self, map_as_list, allow_diagonal=None):
        if allow_diagonal is None:
            from_graph = self.graph.allow_diagonal
            self.graph = Graph(map_as_list, from_graph)
            return

        self.diagonal = allow_diagonal
        self.graph = Graph(map_as_list, allow_diagonal)

    def get_path(self, algorithm, points):
        start_node = self.graph.nodes[points[0]]
        end_node = self.graph.nodes[points[1]]
        result = self.algorithms[algorithm].get_path(
            start_node,
            end_node,
            self.graph.allow_diagonal
        )
        self.graph.clean_up()
        return result
