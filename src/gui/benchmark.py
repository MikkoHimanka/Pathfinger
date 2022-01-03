from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QWidget, QLabel
from PyQt6.QtCharts import QBarSeries, QBarSet, QChart, QChartView, QValueAxis
from PyQt6.QtCore import Qt

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
        self.saved_results = set()
        self.parent.parent.data_manager.dictUpdated.connect(self.add_result)
        self.bar_series = QBarSeries()

    def start_benchmark(self):
        self.start_button.hide()
        self.chart = QChart()
        self.chart.addSeries(self.bar_series)
        self.chart_view = QChartView(self.chart)
        self.value_axis = QValueAxis()
        self.chart.addAxis(self.value_axis, Qt.AlignmentFlag.AlignLeft)
        self.bar_series.attachAxis(self.value_axis)
        self.max_value = 0
        self.layout.addWidget(self.chart_view)
        self.parent.start_benchmark()

    def add_result(self, results: dict):
        for result in results.keys():
            if result not in self.saved_results:
                self.saved_results.add(result)
                bar_set = QBarSet(result)
                value = results[result].time / 1000000000
                bar_set.append(value)
                self.bar_series.append(bar_set)
                if value > self.max_value:
                    self.max_value = value
                    self.value_axis.setRange(0, self.max_value)
        chart = QChart()
        value_axis = QValueAxis()
        value_axis.setRange(0, self.max_value)
        chart.addAxis(value_axis, Qt.AlignmentFlag.AlignLeft)
        self.bar_series.attachAxis(value_axis)
        chart.addSeries(self.bar_series)
        self.chart = chart
        self.chart_view.setChart(self.chart)
        