from utils.CSVManager import CSVManager

class DataManager():
    def __init__(self):
        self.csv_manager = CSVManager()
        self.changed = False
        self.current_map = []
        self.current_path = []

    def openFile(self, filename, infobar):
        if self.changed:
            # TODO: confirm dialog
            pass

        try:
            self.current_map = self.csv_manager.openFile(filename)
            return True
        except Exception as e:
            infobar.setWarning(e.args[0])
            return False