from collections import deque


class Dijkstra:
    def get_path(self, points, graph):
        return [(0, 0), (1, 1)]

        start = points[0]
        end = points[1]
        queue = deque(graph.nodes[points[0]])

        while len(queue) != 0:
            node = queue.popleft()[1]
            if node.visited:
                continue
            node.visited = True
            for neighbour in node.connections:
                pass
