from pathfinder.dijkstra import Dijkstra

class PathManager():
    def __init__(self):
        self.algorithms = {
            "Dijkstra": Dijkstra()
        }

    def getPath(self, algorithm, points):
        return self.algorithms[algorithm].getPath(points)