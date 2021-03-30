from PyQt5 import QtGui  
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
w = QtGui.QWidget()
btn = QtGui.QPushButton('press me')
text = QtGui.QLineEdit('enter text')
listw = QtGui.QListWidget()
plot = pg.PlotWidget()

layout = QtGui.QGridLayout()
w.setLayout(layout)
layout.addWidget(btn, 0, 0) 
layout.addWidget(text, 1, 0) 
layout.addWidget(listw, 2, 0) 
layout.addWidget(plot, 0, 1, 3, 1) 

x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
plot.plot(x, y, pen=(2,3), symbol='d')

w.show()

app.exec_()