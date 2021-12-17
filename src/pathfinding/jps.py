from sys import maxsize
from utils.mathTools import distance

from pathfinding.aStar import AStar


def vector_add(point_a, point_b):
    return (point_a[0] + point_b[0], point_a[1] + point_b[1])


def vector_subtract(point_a, point_b):
    return (point_a[0] - point_b[0], point_a[1] - point_b[1])


class Filter:
    def __init__(self, possible_values):
        self.possible_values = possible_values

    def node_filter(self, nodes_to_filter):
        return list(
            filter(lambda x: x in self.possible_values, nodes_to_filter)
        )


class JPS:
    def get_path(self, start_node, end_node, allow_diagonal):
        self.a_star = AStar()
        self.forced_neighbors = set()

        self.previous = {}
        self.previous[start_node] = None

        queue = [start_node]

        while len(queue) > 0:
            current = queue.pop()
            successors = self.identify_successors(
                current,
                start_node,
                end_node
            )
            if end_node in successors:
                break
            queue += successors

        resulting_path = []
        current = end_node

        while self.previous.get(current):
            resulting_path.append(current.origin)
            current = self.previous[current]

        if len(resulting_path) > 0:
            resulting_path.append(current.origin)

        return [resulting_path, []]

    def identify_successors(self, node, start, end):
        successors = []
        neighbors = []

        neighbors = self.prune_neighbors(node)
        for n in neighbors:
            n = self.jump(
                node,
                vector_subtract(n.origin, node.origin),
                start,
                end
            )
            if n is not None:
                successors.append(n)

        return successors

    def jump(self, initial_node, direction, start, end):
        next_node_origin = vector_add(initial_node.origin, direction)
        next_node = None
        for _ in initial_node.connections:
            if _.origin == next_node_origin:
                next_node = _
        if next_node is None:
            return None
        self.previous[next_node] = initial_node
        if next_node == end:
            return next_node
        if next_node in self.forced_neighbors:
            return next_node
        if abs(direction[0] - direction[1]) != 1:
            for i in [(direction[0], 0), (0, direction[1])]:
                if self.jump(next_node, i, start, end) is not None:
                    return next_node
        return self.jump(next_node, direction, start, end)

    def is_natural_neighbor(self, target, node, direction):
        natural_coordinates = [
            vector_add(node.origin, (direction[0], 0)),
            vector_add(node.origin, (0, direction[1])),
            vector_add(node.origin, direction),
        ]
        if target.origin in natural_coordinates:
            return True
        return False

    def path_length_via(self, start, end, node):
        return (
            distance(start.origin, node.origin) +
            distance(node.origin, end.origin)
        )

    def path_length_skip(self, start, end, node):
        filter_object = Filter(node.connections)
        path = self.a_star.get_path(
            start,
            end,
            True,
            filter_object.node_filter
        )

        for n in node.connections:
            n.distance = maxsize
            n.previous_node = None

        return path.distance

    def is_pruned(self, node, target, direction):
        path_cost = self.path_length_via(self.previous.get(node), target, node)
        skipped_path_cost = self.path_length_skip(self.previous.get(node), target, node)
        diagonal = abs(direction[0] - direction[1]) != 1

        if diagonal:
            result = skipped_path_cost < path_cost
        else:
            result = skipped_path_cost <= path_cost

        if result and not (node in self.forced_neighbors):
            if not self.is_natural_neighbor(target, node, direction):
                self.forced_neighbors.add(node)

        return result

    def prune_neighbors(self, node):
        if self.previous.get(node) is None:
            return node.connections

        direction = (
            node.origin[0] - self.previous.get(node).origin[0],
            node.origin[1] - self.previous.get(node).origin[1]
        )
        left_overs = []

        for neighbor in node.connections:
            pruned = self.is_pruned(
                node,
                neighbor,
                direction
            )
            if not pruned:
                left_overs.append(neighbor)

        return left_overs
