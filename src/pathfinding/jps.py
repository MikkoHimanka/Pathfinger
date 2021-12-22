from sys import maxsize
from heapq import heapify, heappush, heappop
from utils.mathTools import distance

from pathfinding.path import Path


def vector_add(point_a, point_b):
    return (point_a[0] + point_b[0], point_a[1] + point_b[1])


def vector_subtract(point_a, point_b):
    return (point_a[0] - point_b[0], point_a[1] - point_b[1])

def get_adjacent_corners(point, direction):
    return [
        (point[0] + (2 * direction[0]), point[1]),
        (point[0], point[1] + (2 * direction[1]))
    ]

class Filter:
    def __init__(self, possible_values):
        self.possible_values = possible_values

    def node_filter(self, nodes_to_filter):
        return list(
            filter(lambda x: x in self.possible_values, nodes_to_filter)
        )


class JPS:
    def get_path(self, start_node, end_node, allow_diagonal):
        time = None
        memory = None
        self.distances = {}
        self.distances[start_node] = 0
        self.jump_point_directions = {}
        self.start_node_origin = start_node.origin
        self.jump_point_directions[start_node.origin] = ((0,0), 0)

        heap = []
        heapify(heap)
        visited = [start_node.origin]

        heappush(heap, (0, start_node))

        while len(heap) > 0:
            node = heappop(heap)[1]

            visited.append(node.origin)    
            successors = self.identify_successors(node, end_node)

            for successor in successors:
                new_distance = self.distances.get(node) + distance(node.origin, successor.origin)
                self.distances[successor] = new_distance
                priority = (
                    new_distance +
                    distance(successor.origin, end_node.origin)
                )
                if successor == end_node:
                    heap.clear()
                    break
                heappush(heap, (priority, successor))

        resulting_path = []
        current = end_node.origin
        current_dir = self.jump_point_directions.get(end_node.origin)

        if current_dir is not None:
            current_dir = vector_subtract((0, 0), current_dir[0])
            while True:
                resulting_path.append(current)
                if current == start_node.origin:
                    break
                current = vector_add(current_dir, current)
                new_dir = self.jump_point_directions.get(current)
                if new_dir is not None:
                    current_dir = vector_subtract((0, 0), new_dir[0])

        return Path(resulting_path, visited, time, memory)

    def identify_successors(self, node, end):
        successors = []

        node.connections = self.prune_neighbors(node, node.connections)[0]

        for i in range(len(node.connections)):
            direction = vector_subtract(node.connections[i].origin, node.origin)
            successor = self.jump(
                node,
                direction,
                end
            )
            
            if successor is not None:
                cost = self.jump_point_directions[node.origin][1] + distance(node.origin, successor.origin)
                old_cost = self.jump_point_directions.get(successor.origin)
                if old_cost is None or cost < old_cost[1]:
                    self.jump_point_directions[successor.origin] = (direction, cost)
                node.connections[i] = successor
                successors.append(successor)

        return successors

    def jump(self, initial_node, direction, end):
        next_node_origin = vector_add(initial_node.origin, direction)
        next_node = None
        for _ in initial_node.connections:
            if _.origin == next_node_origin:
                next_node = _
                break
        if next_node is None:
            return None
        if next_node == end:
            return next_node
        pruned = self.prune_neighbors(next_node, next_node.connections, direction)
        if pruned[1]:
            return next_node
        if abs(direction[0] - direction[1]) != 1:
            for _dir in [(direction[0], 0), (0, direction[1])]:
                if self.jump(next_node, _dir, end) is not None:
                    return next_node
        return self.jump(next_node, direction, end)

    def is_natural_neighbor(self, target, node, direction):
        natural_coordinates = [
            vector_add(node.origin, direction)
        ]
        diagonal = abs(direction[0] - direction[1]) != 1
        if diagonal:
            natural_coordinates += [
                vector_add(node.origin, (direction[0], 0)),
                vector_add(node.origin, (0, direction[1])),
            ]
        if target.origin in natural_coordinates:
            return True
        return False

    def prune_neighbors(self, node, neighbors, direction=None):
        if node.origin == self.start_node_origin:
            return [node.connections, False]

        if direction == None:
            direction = self.jump_point_directions[node.origin][0]

        diagonal = abs(direction[0] - direction[1]) != 1
        forced_neighbors = []
        has_forced = False
        previous_origin = vector_subtract(
            node.origin,
            direction
        )
        neighbor_origins = list(map(lambda x: x.origin, neighbors))
        if diagonal:
            forced = get_adjacent_corners(previous_origin, direction)
            origins_to_check = [
                vector_add(previous_origin, (direction[0], 0)),
                vector_add(previous_origin, (0, direction[1]))
                ]
        elif abs(direction[0]) == 1:
            forced = [
                vector_add(node.origin, (direction[0], 1)),
                vector_add(node.origin, (direction[0], -1))
            ]
            origins_to_check = [
                vector_add(node.origin, (0, 1)),
                vector_add(node.origin, (0, -1))
            ]
        elif abs(direction[1]) == 1:
            forced = [
                vector_add(node.origin, (1, direction[1])),
                vector_add(node.origin, (-1, direction[1]))
            ]
            origins_to_check = [
                vector_add(node.origin, (1, 0)),
                vector_add(node.origin, (-1, 0))
            ]
        for i in range(len(origins_to_check)):
            if origins_to_check[i] not in neighbor_origins:
                if forced[i] in neighbor_origins:
                    forced_neighbors.append(forced[i])
                    has_forced = True
        left_overs = []
        for n in neighbors:
            if self.is_natural_neighbor(n, node, direction) or n.origin in forced_neighbors:
                left_overs.append(n)
        
        return [left_overs, has_forced]
