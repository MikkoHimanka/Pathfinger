from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLabel

from pathfinding.path import Path

class BenchmarkCell(QWidget):
    def __init__(self):
        super().__init__()


class BenchmarkWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setFixedSize(600, 400)
        self.layout = QHBoxLayout()
        self.start_button = QPushButton("Start benchmark")
        self.start_button.clicked.connect(self.start_benchmark)
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)
        self.saved_results = dict()
        self.parent.parent.data_manager.dictUpdated.connect(lambda x: self.add_result(x))

    def start_benchmark(self):
        self.start_button.hide()
        self.parent.start_benchmark()

    def add_result(self, results: dict):
        for result in results.keys():
            if result not in self.saved_results:
                self.saved_results[result] = 0
                self.layout.addWidget(QLabel(result + ": " + str(results[result].time)))
