from pathfinding.pathManager import PathManager
from utils.CSVManager import CSVManager


class DataManager:
    def __init__(self):
        self.csv_manager = CSVManager()
        self.map_changed = True
        self.path_changed = True
        self.current_map = []
        self.current_path = []
        self.current_visited = []
        self.path_manager = PathManager(self.current_map, False)

    def open_file(self, filename, infobar):
        try:
            self.current_map = self.csv_manager.open_file(filename)
            self.map_changed = True
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
        self.current_path.clear()
        self.current_visited.clear()
        self.path_changed = True

    def init_graph(self):
        if self.map_changed:
            self.path_manager.init_graph(self.current_map)
            self.map_changed = False

    def set_path(self, algorithm, points):
        found_path = self.path_manager.get_path(algorithm, points)
        self.current_path = found_path[0]
        self.current_visited = found_path[1]
        self.path_changed = True

    def set_diagonal(self, value):
        self.path_manager.init_graph(self.current_map, value)
