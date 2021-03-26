import sys
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic

from layout3 import Ui_MainWindow
from about import Ui_Form


class About(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.show()


class AnotherWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filenames = ['', '', '']
        self.y = [[], [], []]
        self.data_line = [[], [], []]

        self.ui.actionAbout.triggered.connect(lambda: self.showAbout())
        self.ui.actionExit.triggered.connect(lambda: self.close())
        self.ui.actionNew.triggered.connect(lambda: self.create_new_window())
        self.ui.actionOpenChannel1.triggered.connect(lambda: self.browse(0))
        self.ui.actionOpenChannel2.triggered.connect(lambda: self.browse(1))
        self.ui.actionOpenChannel3.triggered.connect(lambda: self.browse(2))
        self.ui.playBtn1.clicked.connect(self.play, 0)

        self.show()

    def showAbout(self) -> None:
        self.about = About()
        self.about.show()

    def play(self, filenumber: int) -> None:
        if not self.y[filenumber]:
            self.browse(filenumber=filenumber)

    def create_new_window(self) -> None:
        mw = AnotherWindow()
        mw.show()

    def browse(self, filenumber: int) -> None:
        if(len(self.y[filenumber]) > 0):
            return
        self.filenames[filenumber] = qtw.QFileDialog.getOpenFileName(
            None, 'Load Signal', './', "Raw Data(*.csv *.txt *.xls)")
        path = self.filenames[filenumber][0]
        self.openFile(path, filenumber)

    def openFile(self, path: str, filenumber: int) -> None:
        self.y[filenumber] = np.genfromtxt(path, delimiter=',')
        self.plot(filenumber)

    def plot(self, filenumber: int) -> None:
        if filenumber == 0:
            pen1 = pg.mkPen(color=(255, 0, 0), width=2)
            self.data_line[filenumber] = self.ui.signal1Graph.plot(
                list(range(self.y[filenumber].size)), self.y[filenumber], name='CH1', pen=pen1)
        elif filenumber == 1:
            pen2 = pg.mkPen(color=(0, 255, 0), width=2)
            self.data_line[filenumber] = self.ui.signal2Graph.plot(
                list(range(self.y[filenumber].size)), self.y[filenumber], name='CH2', pen=pen2)
        else:
            pen3 = pg.mkPen(color=(0, 0, 255), width=2)
            self.data_line[filenumber] = self.ui.signal3Graph.plot(
                list(range(self.y[filenumber].size)), self.y[filenumber], name='CH3', pen=pen3)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
