from PyQt5 import QtGui
from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox
import pyqtgraph as pg
import numpy as np


class Window(QWidget):

    def _init_(self):
        super()._init_()

        self.btn = QtGui.QPushButton('Restore plot 1 ')
        self.btn2 = QtGui.QPushButton('Restor plot 2')
        self.plot = pg.PlotWidget()
        self.plot2 = pg.PlotWidget()

        self.name = QLineEdit()
        self.program_type = QLineEdit()
        self.product_code = QLineEdit()
        self.customer = QLineEdit()
        self.vendor = QLineEdit()
        self.n_errors = QSpinBox()
        self.n_errors.setRange(0, 1000)
        self.comments = QTextEdit()

        self.generate_btn = QPushButton("Generate PDF")
        self.generate_btn.clicked.connect(self.generate)
        self.btn.clicked.connect(
            lambda: self.plot.getPlotItem().enableAutoRange())
        self.btn2.clicked.connect(
            lambda: self.plot2.getPlotItem().enableAutoRange())

        layout = QtGui.QGridLayout()

        layout.addWidget(self.btn, 0, 0)
        layout.addWidget(self.btn2, 1, 0)
        layout.addWidget(self.name, 2, 0)
        layout.addWidget(self.program_type, 3, 0)
        layout.addWidget(self.product_code, 4, 0)
        layout.addWidget(self.customer, 5, 0)
        layout.addWidget(self.vendor, 6, 0)
        layout.addWidget(self.n_errors, 7, 0)
        layout.addWidget(self.comments, 8, 0)
        layout.addWidget(self.generate_btn, 9, 0)
        layout.addWidget(self.plot, 0, 1, 5, 1)
        layout.addWidget(self.plot2, 1, 1, 5, 1)
        self.setLayout(layout)

        x = np.random.normal(size=100)
        y = np.random.normal(size=100)
        self.plot.plot(x, y, pen=(2, 3), symbol='o')
        self.plot2.plot(x, y, pen=(2, 3), symbol='x')

        self.show()

    def generate(self):
        data = [self.name.text(), self.program_type.text(), self.product_code.text(),
                self.customer.text(), self.vendor.text(), str(self.n_errors.value()),
                self.comments.toPlainText()]

        print(data[0:])
        return [data]


app = QApplication([])
w = Window()
w.show()
app.exec()
