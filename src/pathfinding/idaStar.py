from utils.mathTools import distance, manhattan_distance

from sys import maxsize

class IdaStar:
    def __init__(self):
        self.path = []
        self.visited = []
        self.h = None
        self.start_node = None
        self.end_node = None

    def reset(self):
        self.path = []
        self.visited = []

    def get_h_score(self, node):
        return self.h(node.origin, self.end_node.origin)

    def get_path(self, start_node, end_node, allow_diagonal):
        self.reset()
        self.h = distance if allow_diagonal else manhattan_distance
        self.start_node = start_node
        self.end_node = end_node

        self.path.append(start_node)
        h_score = self.get_h_score(start_node)

        while True:
            t_score = self.search(0, h_score)
            if t_score == -1 or t_score == maxsize:
                return self.get_return_value()
            h_score = t_score

    def search(self, g_score, to_goal):
        node = self.path[len(self.path) - 1]
        self.visited.append(node.origin)
        f_score = g_score + self.get_h_score(node)
        if f_score > to_goal:
            return f_score
        if node == self.end_node:
            return -1
        minimum = maxsize

        neighbors = sorted(
            node.connections.copy(),
            key=lambda x: g_score + self.get_h_score(x)
        )

        for neighbor in neighbors:
            if neighbor not in self.path:
                self.path.append(neighbor)
                t_score = self.search(
                    g_score + self.h(node.origin, neighbor.origin),
                    to_goal
                )
                if t_score == -1:
                    return -1
                if t_score < minimum:
                    minimum = t_score
                self.path.pop()

        return minimum

    def get_return_value(self):
        resulting_path = []
        for node in self.path:
            resulting_path.append(node.origin)

        return [resulting_path, self.visited]
