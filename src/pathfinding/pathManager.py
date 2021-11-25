from math import sqrt
from sys import maxsize
from pathfinding.dijkstra import Dijkstra


class Node:
    def __init__(self, origin):
        self.origin = origin
        self.visited = False
        self.connections = []
        self.distance = maxsize

    def __repr__(self) -> str:
        delimiter = ', '
        return (
            '(' + delimiter.join([str(value) for value in self.origin]) + ')'
        )

    def add_neighbors(self, origin, map_as_list, nodes: dict):
        neighbor_deltas = [-1, 0, 1]
        for x_delta in neighbor_deltas:
            for y_delta in neighbor_deltas:
                if (x_delta, y_delta) == (0, 0):
                    continue

                neighbour_coord = (origin[0] + x_delta, origin[1] + y_delta)
                max_size = int(sqrt(len(map_as_list)))
                if neighbour_coord[0] >= max_size or neighbour_coord[0] < 0:
                    continue
                if neighbour_coord[1] >= max_size or neighbour_coord[1] < 0:
                    continue

                map_value = map_as_list[
                    (neighbour_coord[1] * max_size) + neighbour_coord[0]
                ]

                if map_value == "0":
                    if neighbour_coord in nodes.keys():
                        neighbour_node = nodes[neighbour_coord]
                    else:
                        neighbour_node = Node(neighbour_coord)
                        nodes[neighbour_coord] = neighbour_node

                    self.connections.append(neighbour_node)


class Graph:
    def __init__(self, map_as_list):
        self.nodes = {}
        length = int(sqrt(len(map_as_list)))
        for y in range(length):
            for x in range(length):
                if (x, y) in self.nodes.keys():
                    node = self.nodes[(x, y)]
                else:
                    node = Node((x, y))
                    self.nodes[(x, y)] = node

                node.add_neighbors((x, y), map_as_list, self.nodes)

    def clean_up(self):
        for node in self.nodes.values():
            node.distance = maxsize
            try:
                del node.previous_node
            except AttributeError:
                continue


class PathManager:
    def __init__(self, map_as_list):
        self.algorithms = {"Dijkstra": Dijkstra()}
        self.graph = Graph(map_as_list)

    def get_path(self, algorithm, points):
        start_node = self.graph.nodes[points[0]]
        end_node = self.graph.nodes[points[1]]
        result = self.algorithms[algorithm].get_path(start_node, end_node)
        self.graph.clean_up()
        return result
