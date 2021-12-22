from PyQt6.QtCore import QObject, pyqtSignal
from pathfinding.pathManager import PathManager
from utils.FileManager import FileManager

from time import time_ns


class DataManager(QObject):
    dictUpdated = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.file_manager = FileManager()
        self.path_changed = False
        self.current_map = []
        self.current_path = None
        self.path_manager = PathManager(self.current_map, False)

    def open_file(self, filename, infobar):
        try:
            self.current_map = self.file_manager.open_file(filename)
            self.clear_path()
            return True
        except Exception as e:
            infobar.set_warning(e.args[0])
            return False

    def create_empty(self, width, height):
        self.clear_path()
        new_map = ['0' for x in range(width) for y in range(height)]
        self.current_map = new_map

    def clear_path(self):
        self.current_path = None
        self.path_changed = False

    def init_graph(self):
        self.path_manager.init_graph(self.current_map)

    def set_path(self, algorithm, points):
        found_path = self.path_manager.get_path(algorithm, points)
        self.current_path = found_path
        self.path_changed = True

    def set_diagonal(self, value):
        self.path_manager.init_graph(self.current_map, value)

    def run_benchmark(self, points):
        self.benchmark_results = {}
        algorithms = [
            "Dijkstra",
            "Greedy Best-First",
            "A*",
            "JPS"
        ]
        self.clear_path()
        for algo in algorithms:
            self.path_manager.init_graph(self.current_map, True)
            time_start = time_ns()
            self.benchmark_results[algo] = self.path_manager.get_path(algo, points)
            self.benchmark_results[algo].time = time_ns() - time_start
            self.dictUpdated.emit(self.benchmark_results)
