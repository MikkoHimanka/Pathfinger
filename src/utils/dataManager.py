from utils.CSVManager import CSVManager


class DataManager:
    def __init__(self):
        self.csv_manager = CSVManager()
        self.changed = False
        self.current_map = []
        self.current_path = []

    def open_file(self, filename, infobar):
        if self.changed:
            # TODO: confirm dialog
            pass

        try:
            self.current_map = self.csv_manager.open_file(filename)
            return True
        except Exception as e:
            infobar.set_warning(e.args[0])
            return False

    def clear_path(self):
        self.current_path.clear()
