from collections import deque

from utils.mathTools import distance


class Dijkstra:
    def get_path(self, start_node, end_node):
        start_node.distance = 0

        queue = deque()
        queue.append(start_node)

        visited_points = []

        while len(queue) != 0:
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

        resulting_path = [end_node.origin]
        current = end_node
        while True:
            try:
                resulting_path.append(current.previous_node.origin)
                current = current.previous_node
            except AttributeError:
                break
        resulting_path.reverse()

        return [resulting_path, visited_points]
