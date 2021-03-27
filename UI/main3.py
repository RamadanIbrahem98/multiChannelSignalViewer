import sys
import os
import csv
import pathlib
import numpy as np
import pandas as pd
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
        self.graphChannels = [self.ui.signal1Graph,
                              self.ui.signal2Graph, self.ui.signal3Graph]
        self.timers = [self.ui.timer1, self.ui.timer2, self.ui.timer3]
        self.pen = [pg.mkPen(color=(255, 0, 0), width=2), pg.mkPen(
            color=(0, 255, 0), width=2), pg.mkPen(color=(0, 0, 255), width=2)]

        self.y = [[], [], []]
        self.x = [[], [], []]

        self.data_line = [[], [], []]
        self.data = [[], [], []]
        self.idx = [0, 0, 0]
        self.isResumed = [False, False, False]
        self.channelComponents = [self.ui.channel1,
                                  self.ui.channel2, self.ui.channel3]

        self.CHANNEL1 = 0
        self.CHANNEL2 = 1
        self.CHANNEL3 = 2

        self.ui.showChannel1.setChecked(True)
        self.ui.channel1.show()
        self.ui.channel2.hide()
        self.ui.channel3.hide()

        self.ui.showChannel1.stateChanged.connect(
            lambda: self.hide(self.CHANNEL1))
        self.ui.showChannel2.stateChanged.connect(
            lambda: self.hide(self.CHANNEL2))
        self.ui.showChannel3.stateChanged.connect(
            lambda: self.hide(self.CHANNEL3))

        self.ui.actionAbout.triggered.connect(lambda: self.showAbout())
        self.ui.actionExit.triggered.connect(lambda: self.close())
        self.ui.actionNew.triggered.connect(lambda: self.create_new_window())

        self.ui.actionOpenChannel1.triggered.connect(
            lambda: self.browse(self.CHANNEL1))
        self.ui.playBtn1.clicked.connect(lambda: self.play(self.CHANNEL1))
        self.ui.pauseBtn1.clicked.connect(lambda: self.pause(self.CHANNEL1))
        self.ui.focusBtn1.clicked.connect(
            lambda: self.graphChannels[self.CHANNEL1].getPlotItem().enableAutoRange())
        self.ui.zoomInBtn1.clicked.connect(lambda: self.zoomin(self.CHANNEL1))
        self.ui.zoomOutBtn1.clicked.connect(
            lambda: self.zoomout(self.CHANNEL1))
        self.ui.clearBtn1.clicked.connect(lambda: self.clear(self.CHANNEL1))

        self.ui.actionOpenChannel2.triggered.connect(
            lambda: self.browse(self.CHANNEL2))
        self.ui.playBtn2.clicked.connect(lambda: self.play(self.CHANNEL2))
        self.ui.pauseBtn2.clicked.connect(lambda: self.pause(self.CHANNEL2))
        self.ui.focusBtn2.clicked.connect(
            lambda: self.graphChannels[self.CHANNEL2].getPlotItem().enableAutoRange())
        self.ui.zoomInBtn2.clicked.connect(lambda: self.zoomin(self.CHANNEL2))
        self.ui.zoomOutBtn2.clicked.connect(
            lambda: self.zoomout(self.CHANNEL2))
        self.ui.clearBtn2.clicked.connect(lambda: self.clear(self.CHANNEL2))

        self.ui.actionOpenChannel3.triggered.connect(
            lambda: self.browse(self.CHANNEL3))
        self.ui.playBtn3.clicked.connect(lambda: self.play(self.CHANNEL3))
        self.ui.pauseBtn3.clicked.connect(lambda: self.pause(self.CHANNEL3))
        self.ui.focusBtn3.clicked.connect(
            lambda: self.graphChannels[self.CHANNEL3].getPlotItem().enableAutoRange())
        self.ui.zoomInBtn3.clicked.connect(lambda: self.zoomin(self.CHANNEL3))
        self.ui.zoomOutBtn3.clicked.connect(
            lambda: self.zoomout(self.CHANNEL3))
        self.ui.clearBtn3.clicked.connect(lambda: self.clear(self.CHANNEL3))

        self.show()

    def showAbout(self) -> None:
        self.about = About()
        self.about.show()

    def play(self, channel: int) -> None:
        if not self.y[channel]:
            self.browse(channel)
        if not self.isResumed[channel]:
            self.timers[channel].start()
            self.isResumed[channel] = True

    def pause(self, channel: int) -> None:
        if not self.y[channel]:
            self.browse(channel)
        if self.isResumed[channel]:
            self.timers[channel].stop()
            self.isResumed[channel] = False

    def clear(self, channel: int) -> None:
        if self.y[channel]:
            self.graphChannels[channel].removeItem(self.data_line[channel])
            self.timers[channel].stop()
            self.isResumed[channel] = False
            self.y[channel] = []
            self.x[channel] = []
            self.data_line[channel] = []

    def hide(self, channel: int) -> None:
        if(self.channelComponents[channel].isVisible()):
            self.channelComponents[channel].hide()
            self.clear(channel)
        else:
            self.channelComponents[channel].show()

    def create_new_window(self):
        mw = AnotherWindow()
        mw.show()

    def browse(self, channel: int) -> None:
        self.filenames[channel] = qtw.QFileDialog.getOpenFileName(
            None, 'Load Signal', './', "Raw Data(*.csv *.txt *.xls)")
        path = self.filenames[channel][0]
        self.openFile(path, channel)

    def openFile(self, path: str, channel: int) -> None:
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                self.y[channel].append(float(line[1]))
                self.x[channel].append(float(line[0]))
        self.isResumed[channel] = True
        self.plotGraph(channel)
        self.plotSpectrogram(channel)

    def plotGraph(self, channel: int) -> None:
        self.data_line[channel] = self.graphChannels[channel].plot(
            self.x[channel], self.y[channel], name='CH1', pen=self.pen[channel])
        self.graphChannels[channel].plotItem.setLimits(
            xMin=0, xMax=6, yMin=-2, yMax=2)

        self.idx[channel] = 0
        self.timers[channel].setInterval(100)
        self.timers[channel].timeout.connect(lambda: self.updatePlot(channel))
        self.timers[channel].start()

    def updatePlot(self, channel: int) -> None:
        xaxis = self.x[channel][:self.idx[channel]]
        yaxis = self.y[channel][:self.idx[channel]]
        self.idx[channel] += 10
        if self.idx[channel] > len(self.x[channel]):
            # self.idx[channel] = 0
            self.timers[channel].stop()

        if self.x[channel][self.idx[channel]] > 1.0:
            self.graphChannels[channel].setLimits(xMin=min(xaxis, default=0), xMax=max(
                xaxis, default=0))  # disable paning over xlimits
        self.graphChannels[channel].plotItem.setXRange(
            max(xaxis, default=0)-1.0, max(xaxis, default=0))

        self.data_line[channel].setData(xaxis, yaxis)

    def plotSpectrogram(self, channel: int) -> None:
        self.data_line[channel] = self.graphChannels[channel].plot(
            list(range(self.y[channel].size)), self.y[channel], name='CH1', pen=self.pen[channel])

    def zoomin(self, channel: int) -> None:
        self.graphChannels[channel].plotItem.getViewBox().scaleBy((0.75, 0.75))

    def zoomout(self, channel: int) -> None:
        self.graphChannels[channel].plotItem.getViewBox().scaleBy((1.25, 1.25))


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
