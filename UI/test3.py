from PyQt5 import QtGui
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
w = QtGui.QWidget()


def generate():
    data = [name.text(), program_type.text(), product_code.text(),
            customer.text(), vendor.text(), str(n_errors.value()),
            comments.toPlainText()]
    print(data[0:])
    return [data]


#btn = QtGui.QPushButton('press me')
#text = QtGui.QLineEdit('enter text')
#listw = QtGui.QListWidget()
#plot = pg.PlotWidget()
btn = QtGui.QPushButton('Restore plot 1 ')
btn2 = QtGui.QPushButton('Restor plot 2')
plot = pg.PlotWidget()
plot2 = pg.PlotWidget()

name = QtGui.QLineEdit('Dr.Name')
program_type = QtGui.QLineEdit('Diagnosis')
product_code = QtGui.QLineEdit('HR')
customer = QtGui.QLineEdit('patient')
vendor = QtGui.QLineEdit('Medicine')
n_errors = QtGui.QSpinBox()
n_errors.setRange(0, 1000)
comments = QtGui.QTextEdit('write comments here')
generate_btn = QtGui.QPushButton("Generate PDF")

#layout = QFormLayout()
#        layout.addRow("Name", self.name)
#        layout.addRow("Program Type", self.program_type)
#        layout.addRow("Product Code", self.product_code)
#        layout.addRow("Customer", self.customer)
#        layout.addRow("Vendor", self.vendor)
#        layout.addRow("No. of Errors", self.n_errors)
#
#        layout.addRow("Comments", self.comments)
#        layout.addRow(self.generate_btn)
#
#        self.setLayout(layout)

generate_btn.clicked.connect(generate)
btn.clicked.connect(lambda: plot.getPlotItem().enableAutoRange())
btn2.clicked.connect(lambda: plot2.getPlotItem().enableAutoRange())


#layout = QtGui.QGridLayout()
# w.setLayout(layout)
#layout.addWidget(btn, 0, 0)
#layout.addWidget(text, 1, 0)
#layout.addWidget(listw, 2, 0)
#layout.addWidget(plot, 0, 1, 3, 1)
#
#x = np.random.normal(size=1000)
#y = np.random.normal(size=1000)
#plot.plot(x, y, pen=(2,3), symbol='d')
#
layout = QtGui.QGridLayout()
w.setLayout(layout)
layout.addWidget(btn, 0, 0)
layout.addWidget(btn2, 1, 0)
layout.addWidget(name, 2, 0)
layout.addWidget(program_type, 3, 0)
layout.addWidget(product_code, 4, 0)
layout.addWidget(customer, 5, 0)
layout.addWidget(vendor, 6, 0)
layout.addWidget(n_errors, 7, 0)
layout.addWidget(comments, 8, 0)
layout.addWidget(generate_btn, 9, 0)
layout.addWidget(plot, 0, 1, 8, 5)
# (rownum in col1, col num  ,fit all above rows  ,corresponsing rows in col -width of col-)
layout.addWidget(plot2, 8, 1, 10, 5)


x = np.random.normal(size=100)
y = np.random.normal(size=100)
plot.plot(x, y, pen=(2, 3), symbol='o')
plot2.plot(x, y, pen=(2, 3), symbol='x')


w.show()

app.exec_()
