import sys
import csv
import numpy as np
import pyqtgraph as pg
import pyqtgraph.exporters
from PyQt5 import QtWidgets as qtw
import scipy.signal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.gridspec import GridSpec

from PDF import PDF
from about import Ui_Form
# from layout import Ui_MainWindow
from layout import Ui_MainWindow


class About(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.show()


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.CHANNEL1 = 0
        self.CHANNEL2 = 1
        self.CHANNEL3 = 2
        self.PLOT_DIR = 'Plots'
        self.filenames = ['', '', '']
        self.amplitude = [[], [], []]
        self.time = [[], [], []]
        self.timeIdx = [[0, 0], [0, 0], [0, 0]]
        self.upToDateGraph = [[], [], []]
        self.spectrogramData = [None, None, None]
        self.pointsToAppend = [0, 0, 0]
        self.isResumed = [False, False, False]

        # GUI Components to Manipulate
        self.graphChannels = [self.ui.signal1Graph,
                              self.ui.signal2Graph, self.ui.signal3Graph]
        self.spectrogramChannels = [
            self.ui.spectrogram1Graph, self.ui.spectrogram2Graph, self.ui.spectrogram3Graph]
        self.timers = [self.ui.timer1, self.ui.timer2, self.ui.timer3]
        self.setChannelChecked = [self.ui.showChannel1,
                                  self.ui.showChannel2, self.ui.showChannel3]
        self.channelComponents = [self.ui.channel1,
                                  self.ui.channel2, self.ui.channel3]

        # GUI Compenents to be Triggered or Clicked
        self.openChannels = [self.ui.actionOpenChannel1,
                             self.ui.actionOpenChannel2, self.ui.actionOpenChannel3]
        self.playBtns = [self.ui.playBtn1, self.ui.playBtn2, self.ui.playBtn3]
        self.pauseBtns = [self.ui.pauseBtn1,
                          self.ui.pauseBtn2, self.ui.pauseBtn3]
        self.autoRanges = [self.ui.focusBtn1,
                           self.ui.focusBtn2, self.ui.focusBtn3]
        self.zoomIns = [self.ui.zoomInBtn1,
                        self.ui.zoomInBtn2, self.ui.zoomInBtn3]
        self.zoomOuts = [self.ui.zoomOutBtn1,
                         self.ui.zoomOutBtn2, self.ui.zoomOutBtn3]
        self.clearGraphs = [self.ui.clearBtn1,
                            self.ui.clearBtn2, self.ui.clearBtn3]

        # The pen variable corresponding with each plot
        self.pen = [pg.mkPen(color=(255, 0, 0), width=2), pg.mkPen(
            color=(0, 255, 0), width=2), pg.mkPen(color=(0, 0, 255), width=2)]

        def mappingSlotsAndSignals(connections):
            for connection in connections:
                connection

        for channel in self.channelComponents:
            channel.show()
        for channelToCheck in self.setChannelChecked:
            channelToCheck.setChecked(True)

        mappingSlotsAndSignals(map(lambda showGraph, CHANNEL: showGraph.stateChanged.connect(
            lambda: self.hide(CHANNEL)), self.setChannelChecked, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        mappingSlotsAndSignals(map(lambda open, CHANNEL: open.triggered.connect(lambda: self.browse(
            CHANNEL)), self.openChannels, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        mappingSlotsAndSignals(map(lambda playBtn, CHANNEL: playBtn.clicked.connect(
            lambda: self.play(CHANNEL)), self.playBtns, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        mappingSlotsAndSignals(map(lambda pauseBtn, CHANNEL: pauseBtn.clicked.connect(
            lambda: self.pause(CHANNEL)), self.pauseBtns, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        mappingSlotsAndSignals(map(lambda autoRange, CHANNEL: autoRange.clicked.connect(
            lambda: self.graphChannels[CHANNEL].getPlotItem().enableAutoRange()), self.autoRanges, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        mappingSlotsAndSignals(map(lambda zoomIn, CHANNEL: zoomIn.clicked.connect(
            lambda: self.zoomin(CHANNEL)), self.zoomIns, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        mappingSlotsAndSignals(map(lambda zoomOut, CHANNEL: zoomOut.clicked.connect(
            lambda: self.zoomout(CHANNEL)), self.zoomOuts, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        mappingSlotsAndSignals(map(lambda clearGraph, CHANNEL: clearGraph.clicked.connect(
            lambda: self.clear(CHANNEL)), self.clearGraphs, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        self.ui.actionAbout.triggered.connect(lambda: self.showAbout())
        self.ui.actionExit.triggered.connect(lambda: self.close())
        self.ui.actionNew.triggered.connect(lambda: self.create_new_window())
        self.ui.generatePDF.clicked.connect(lambda: self.generatePDF())

        self.show()

    def create_new_window(self):
        self.newWindow = MainWindow()
        self.newWindow.show()

    def showAbout(self) -> None:
        self.about = About()
        self.about.show()

    def hide(self, channel: int) -> None:
        if(self.channelComponents[channel].isVisible()):
            self.channelComponents[channel].hide()
            self.setChannelChecked[channel].setChecked(False)
            self.clear(channel)
            self.resize(self.minimumSize())
        else:
            self.setChannelChecked[channel].setChecked(True)
            self.channelComponents[channel].show()
            self.resize(self.minimumSize())

    def browse(self, channel: int) -> None:
        self.hide(channel)

        # self.clear(channel)
        self.filenames[channel] = qtw.QFileDialog.getOpenFileName(
            None, 'Load Signal', './', "Raw Data(*.csv)")
        path = self.filenames[channel][0]
        self.openFile(path, channel)

    def openFile(self, path: str, channel: int) -> None:
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                self.amplitude[channel].append(float(line[1]))
                self.time[channel].append(float(line[0]))
        self.isResumed[channel] = True

        self.plotGraph(channel)
        self.plotSpectrogram(channel)

    def play(self, channel: int) -> None:
        if not self.amplitude[channel]:
            self.browse(channel)
        if not self.isResumed[channel]:
            self.timers[channel].start()
            self.isResumed[channel] = True

    def pause(self, channel: int) -> None:
        if not self.amplitude[channel]:
            self.browse(channel)
        if self.isResumed[channel]:
            self.timers[channel].stop()
            self.isResumed[channel] = False

    def zoomin(self, channel: int) -> None:
        self.graphChannels[channel].plotItem.getViewBox().scaleBy((0.75, 0.75))

    def zoomout(self, channel: int) -> None:
        self.graphChannels[channel].plotItem.getViewBox().scaleBy((1.25, 1.25))

    def clear(self, channel: int) -> None:
        if self.amplitude[channel]:
            self.graphChannels[channel].removeItem(self.upToDateGraph[channel])
            self.spectrogramChannels[channel].removeItem(
                self.spectrogramData[channel])
            self.timers[channel].stop()
            self.isResumed[channel] = False
            self.amplitude[channel] = []
            self.time[channel] = []
            self.upToDateGraph[channel] = []

    def plotGraph(self, channel: int) -> None:
        self.upToDateGraph[channel] = self.graphChannels[channel].plot(
            self.time[channel], self.amplitude[channel], name='CH1', pen=self.pen[channel])
        self.graphChannels[channel].plotItem.setLimits(xMin=0, xMax=6, yMin=-(np.mean(
            self.amplitude[channel]) - min(self.amplitude[channel])), yMax=np.mean(self.amplitude[channel]) - min(self.amplitude[channel]))

        self.pointsToAppend[channel] = 0
        print()
        self.timers[channel].setInterval(150)
        self.timers[channel].timeout.connect(lambda: self.updatePlot(channel))
        if self.pointsToAppend[channel] < len(self.time[channel]):
            self.timers[channel].start()

    def updatePlot(self, channel: int) -> None:
        xaxis = self.time[channel][:self.pointsToAppend[channel]]
        yaxis = self.amplitude[channel][:self.pointsToAppend[channel]]
        self.pointsToAppend[channel] += 20
        if self.pointsToAppend[channel] > len(self.time[channel]):
            self.timers[channel].stop()

        if self.time[channel][self.pointsToAppend[channel]] > 1.0:
            self.graphChannels[channel].setLimits(
                xMin=min(xaxis, default=0), xMax=max(xaxis, default=0))
        self.graphChannels[channel].plotItem.setXRange(
            max(xaxis, default=0)-1.0, max(xaxis, default=0))

        self.upToDateGraph[channel].setData(xaxis, yaxis)

    def plotSpectrogram(self, channel: int) -> None:
        pyqtgraph.setConfigOptions(imageAxisOrder='row-major')
        fs = 1 / (self.time[channel][1] - self.time[channel][0])
        yaxis = np.array(self.amplitude[channel])
        f, t, Sxx = scipy.signal.spectrogram(yaxis, fs)
        self.spectrogramData[channel] = self.spectrogramChannels[channel].addPlot(
        )

        img = pg.ImageItem()
        self.spectrogramData[channel].addItem(img)
        hist = pg.HistogramLUTItem()
        hist.setImageItem(img)
        self.spectrogramChannels[channel].addItem(
            self.spectrogramData[channel])
        self.spectrogramChannels[channel].show()
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState(
            {'mode': 'rgb',
             'ticks': [(0.5, (0, 182, 188, 255)),
                       (1.0, (246, 111, 0, 255)),
                       (0.0, (75, 0, 113, 255))]})
        hist.gradient.showTicks(False)

        img.setImage(Sxx)
        img.scale(t[-1]/np.size(Sxx, axis=1), f[-1]/np.size(Sxx, axis=0))
        self.spectrogramData[channel].setLimits(
            xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        # self.spectrogramData[channel].setLabel('bottom', "Time", units='s')
        # self.spectrogramData[channel].setLabel('left', "Frequency", units='Hz')

    def generatePDF(self):
        images = [0, 0, 0]
        rows = 0
        xmax = [self.pointsToAppend[0],
                self.pointsToAppend[1], self.pointsToAppend[2]]
        for channel in range(3):
            if self.amplitude[channel]:
                images[channel] = 1
                self.pause(channel)
                rows += 1
            else:
                self.hide(channel)

        if not rows:
            qtw.QMessageBox.information(
                self, 'failed', 'You have to input a signal first')
            return
        outFile = qtw.QFileDialog.getSaveFileName(
            None, 'Load Signal', './', "Document(*.pdf)")
        report = PdfPages(outFile[0])
        fig = plt.figure(figsize=(12, 16))
        G = GridSpec(2, 1)
        for channel in range(3):
            if images[channel]:
                fig = plt.figure(figsize=(12, 16))
                G = GridSpec(2, 1)
                axes1 = plt.subplot(G[0, 0])
                self.getFigure(axes1, channel, xmax[channel])
                axes2 = plt.subplot(G[1, 0])
                self.getSpectrogram(axes2, channel)
                report.savefig(fig)
        report.close()
        qtw.QMessageBox.information(self, 'success', 'PDF has been created')

    def getFigure(self, fig, channel, xmax) -> None:
        xRange = round(1 / (self.time[channel][1] - self.time[channel][0]))
        if(xmax - xRange > 0):
            xmin = xmax - xRange
        else:
            xmin = 0

        fig.plot(self.time[channel][xmin:xmax],
                 self.amplitude[channel][xmin:xmax])
        fig.set_xlabel('time (sec)')
        fig.set_ylabel('amplitude (v)')
        fig.set_title(f'plot - {channel + 1}')

    def getSpectrogram(self, fig, channel):
        fs = 1/(self.time[channel][1] - self.time[channel][0])
        f, t, Sxx = scipy.signal.spectrogram(
            np.array(self.amplitude[channel]), fs)
        fig.pcolormesh(t, f, Sxx, shading='gouraud')
        fig.specgram(np.array(self.amplitude[channel]).astype(float), Fs=fs)
        fig.set_xlabel('time (sec)')
        fig.set_ylabel('frequency (Hz)')
        fig.set_title(f'spectrogram - {channel + 1}')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
