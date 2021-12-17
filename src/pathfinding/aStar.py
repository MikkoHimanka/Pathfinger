from sys import maxsize
from utils.mathTools import distance, nudge, manhattan_distance
from heapq import heapify, heappush, heappop


class Path:
    def __init__(self, path, visited, distance):
        self.path = path
        self.visited = visited
        self.distance = distance


class AStar:
    def get_path(self, start_node, end_node, allow_diagonal, node_filter=None):
        h = distance if allow_diagonal else manhattan_distance
        start_node.distance = 0

        heap = []
        heapify(heap)
        visited = [start_node.origin]

        heappush(heap, (0, start_node))

        while len(heap) > 0:
            node = heappop(heap)[1]

            if node == end_node:
                break

            if node_filter is not None:
                neighbors = node_filter(node.connections)
            else:
                neighbors = node.connections

            for neighbor in neighbors:
                new_distance = (
                    node.distance +
                    h(node.origin, neighbor.origin)
                )
                if node_filter is None:
                    new_distance += nudge(node.origin, neighbor.origin)
                if new_distance < neighbor.distance:
                    if neighbor.distance == maxsize:
                        visited.append(neighbor.origin)
                    neighbor.distance = new_distance
                    priority = (
                        new_distance +
                        h(neighbor.origin, end_node.origin)
                    )
                    heappush(heap, (priority, neighbor))
                    neighbor.previous_node = node

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

        resulting_path.reverse()

        # return [resulting_path, visited]
        return Path(resulting_path, visited, end_node.distance)
