from math import sqrt

from pathfinding.dijkstra import Dijkstra

class Node():
    def __init__(self, origin):
        self.origin = origin
        self.visited = False
        self.connections = []

    def addNeighbors(self, origin, map_as_list, nodes: dict):
        neighborDeltas = [-1, 0, 1]
        for xDelta in neighborDeltas:
            for yDelta in neighborDeltas:
                if (xDelta, yDelta) == (0, 0):
                    continue

                neighbour_coord = (origin[0] + xDelta, origin[1] + yDelta)
                max_size = int(sqrt(len(map_as_list)))
                if (neighbour_coord[0] >= max_size or
                        neighbour_coord[0] < 0):
                    continue
                if (neighbour_coord[1] >= max_size or
                        neighbour_coord[1] < 0):
                    continue

                map_value = map_as_list[(neighbour_coord[1] * max_size) + neighbour_coord[0]]
                
                if map_value == '0':
                    if neighbour_coord in nodes.keys():
                        neighbour_node = nodes[neighbour_coord]
                    else:
                        neighbour_node = Node(neighbour_coord)
                        nodes[neighbour_coord] = neighbour_node

                    self.connections.append(neighbour_node)

class Graph():
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

                node.addNeighbors((x, y), map_as_list, self.nodes)
                

class PathManager():
    def __init__(self, map_as_list):
        self.algorithms = {
            "Dijkstra": Dijkstra()
        }
        self.graph = Graph(map_as_list)

    def getPath(self, algorithm, points):
        return self.algorithms[algorithm].getPath(points)