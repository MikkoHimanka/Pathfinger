from sys import maxsize
from math import sqrt
from collections import deque

class Dijkstra():
    def getPath(self, points, graph):
        start = points[0]
        end = points[1]
        queue = deque(graph.nodes[points[0]])

        while len(queue) != 0:
            node = queue.popleft()[1]
            if not node.visited:

