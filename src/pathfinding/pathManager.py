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

    def add_neighbors(self, origin, map_as_list, nodes: dict, allow_diagonal: bool):
        '''Lisaa Noden naapurit connections listaan'''
        
        max_size = int(sqrt(len(map_as_list)))
        
        if allow_diagonal:
            neighbor_deltas = [-1, 0, 1]
            
            for x_delta in neighbor_deltas:
                for y_delta in neighbor_deltas:
                    if (x_delta, y_delta) == (0, 0):
                        continue

                    neighbour_coord = (origin[0] + x_delta, origin[1] + y_delta)
                    if neighbour_coord[0] >= max_size or neighbour_coord[0] < 0:
                        continue
                    if neighbour_coord[1] >= max_size or neighbour_coord[1] < 0:
                        continue

                    self.insert_neighbour(
                        neighbour_coord,
                        map_as_list,
                        nodes,
                        max_size
                    )

        else:
            for delta in [-1, 1]:
                new_x = origin[0] + delta
                new_y = origin[1] + delta
                if not (new_x >= max_size or new_x < 0):
                    self.insert_neighbour(
                        (new_x, origin[1]),
                        map_as_list,
                        nodes,
                        max_size
                    )
                if not (new_y >= max_size or new_y < 0):
                    self.insert_neighbour(
                        (origin[0], new_y),
                        map_as_list,
                        nodes,
                        max_size
                    )

    def insert_neighbour(self, coord, map_as_list, nodes, upper_limit):
        map_value = map_as_list[
            (coord[1] * upper_limit) + coord[0]
        ]

        if map_value == "0":
            if coord in nodes.keys():
                neighbour_node = nodes[coord]
            else:
                neighbour_node = Node(coord)
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
                    node = Node((x, y))
                    self.nodes[(x, y)] = node

                node.add_neighbors((x, y), map_as_list, self.nodes, allow_diagonal)

    def clean_up(self):
        for node in self.nodes.values():
            node.distance = maxsize
            node.visited = False
            try:
                del node.previous_node
            except AttributeError:
                continue


class PathManager:
    def __init__(self, map_as_list, allow_diagonal):
        self.algorithms = {
            "Dijkstra": Dijkstra(),
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
        result = self.algorithms[algorithm].get_path(start_node, end_node)
        self.graph.clean_up()
        return result
