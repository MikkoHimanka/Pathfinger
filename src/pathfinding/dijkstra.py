from collections import deque

from utils.mathTools import distance


class Dijkstra:
    def get_path(self, start_node, end_node):
        start_node.distance = 0

        queue = deque()
        queue.append(start_node)

        visited_points = []

        while len(queue) > 0:
            node = queue.popleft()

            if not node.visited:
                visited_points.append(node.origin)
                node.visited = True

            if node == end_node:
                break

            for neighbour in node.connections:
                new_distance = (
                    node.distance + distance(node.origin, neighbour.origin)
                )
                if new_distance >= neighbour.distance:
                    continue
                neighbour.distance = new_distance
                neighbour.previous_node = node
                queue.append(neighbour)

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

        return [resulting_path, visited_points]
