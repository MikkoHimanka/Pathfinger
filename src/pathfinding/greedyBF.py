from utils.mathTools import distance, manhattan_distance
from time import time_ns

from pathfinding.path import Path


class KeyOrderedDict:
    def __init__(self):
        self.dict = {}
        self.keys = []

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        if key not in self.keys:
            self.keys.append(key)
            self.dict[key] = [value]
            self.keys.sort()
        else:
            self.dict[key] += [value]

    def __iter__(self):
        return iter(self.keys)

    def __len__(self):
        return len(self.keys)

    def popleft(self):
        if len(self.keys) == 0:
            return None

        key = self.keys[0]
        value = self.dict[key][0]
        self.dict[key].remove(value)
        if len(self.dict[key]) == 0:
            del self.dict[key]
            self.keys.remove(key)

        return value


class GreedyBF:
    def get_path(self, start_node, end_node, allow_diagonal):
        time_start = time_ns()
        h = distance if allow_diagonal else manhattan_distance
        memory = None

        start_node.distance = 0

        queue = KeyOrderedDict()
        visited_points = [start_node.origin]

        queue[0] = start_node

        while len(queue) > 0:
            node = queue.popleft()
            visited_points.append(node.origin)

            if node == end_node:
                break

            for neighbor in node.connections:
                new_distance = (
                    node.distance + h(node.origin, neighbor.origin)
                )
                if new_distance >= neighbor.distance:
                    continue
                neighbor.distance = new_distance
                neighbor.previous_node = node

                neighbour_to_goal = h(neighbor.origin, end_node.origin)
                queue[neighbour_to_goal] = neighbor

        time = time_ns() - time_start

        resulting_path = []
        current = end_node

        try:
            while current.previous_node:
                resulting_path.append(current.origin)
                current = current.previous_node
        except AttributeError:
            pass

        if len(resulting_path) > 0:
            resulting_path.append(current.origin)

        return Path(resulting_path, visited_points, time, memory)
