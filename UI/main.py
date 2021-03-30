import os, sys, shutil, csv, datetime
import numpy as np
import pyqtgraph as pg
import pyqtgraph.exporters
from PyQt5 import QtWidgets as qtw
import scipy.signal

from PDF import PDF
from about import Ui_Form
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
        self.PDF_DIR = 'PDFs'

        # GUI Components to Manipulate
        self.graphChannels = [self.ui.signal1Graph, self.ui.signal2Graph, self.ui.signal3Graph]
        self.spectrogramChannels = [self.ui.spectrogram1Graph, self.ui.spectrogram2Graph, self.ui.spectrogram3Graph]
        self.timers = [self.ui.timer1, self.ui.timer2, self.ui.timer3]
        self.setChannelChecked = [self.ui.showChannel1, self.ui.showChannel2, self.ui.showChannel3]
        self.channelComponents = [self.ui.channel1, self.ui.channel2, self.ui.channel3]
        

        # GUI Compenents to be Triggered or Clicked
        self.openChannels = [self.ui.actionOpenChannel1, self.ui.actionOpenChannel2, self.ui.actionOpenChannel3]
        self.playBtns = [self.ui.playBtn1, self.ui.playBtn2, self.ui.playBtn3]
        self.pauseBtns = [self.ui.pauseBtn1, self.ui.pauseBtn2, self.ui.pauseBtn3]
        self.autoRanges = [self.ui.focusBtn1, self.ui.focusBtn2, self.ui.focusBtn3]
        self.zoomIns = [self.ui.zoomInBtn1, self.ui.zoomInBtn2, self.ui.zoomInBtn3]
        self.zoomOuts = [self.ui.zoomOutBtn1, self.ui.zoomOutBtn2, self.ui.zoomOutBtn3]
        self.clearGraphs = [self.ui.clearBtn1, self.ui.clearBtn2, self.ui.clearBtn3]

        def fun(connections):
            for connection in connections:
                connection

        
        
        # The Filenames of the data Read from the File system
        self.filenames = ['', '', '']

        # The pen variable corresponding with each plot
        self.pen = [pg.mkPen(color=(255, 0, 0), width=2), pg.mkPen(
            color=(0, 255, 0), width=2), pg.mkPen(color=(0, 0, 255), width=2)]

        self.y = [[], [], []]
        self.x = [[], [], []]

        self.data_line = [[], [], []]
        # self.data = [[], [], []]
        self.pointsToAppend = [0, 0, 0]
        self.isResumed = [False, False, False]

        for channel in self.channelComponents:
            channel.show()
        for channelToCheck in self.setChannelChecked:
            channelToCheck.setChecked(True)

        fun(map(lambda showGraph, CHANNEL: showGraph.stateChanged.connect(lambda: self.hide(CHANNEL)), self.setChannelChecked, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        fun(map(lambda open, CHANNEL: open.triggered.connect(lambda: self.browse(CHANNEL)), self.openChannels, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        fun(map(lambda playBtn, CHANNEL: playBtn.clicked.connect(lambda: self.play(CHANNEL)), self.playBtns, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        fun(map(lambda pauseBtn, CHANNEL: pauseBtn.clicked.connect(lambda: self.pause(CHANNEL)), self.pauseBtns, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        fun(map(lambda autoRange, CHANNEL: autoRange.clicked.connect(lambda: self.graphChannels[CHANNEL].getPlotItem().enableAutoRange()), self.autoRanges, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        fun(map(lambda zoomIn, CHANNEL: zoomIn.clicked.connect(lambda: self.zoomin(CHANNEL)), self.zoomIns, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        fun(map(lambda zoomOut, CHANNEL: zoomOut.clicked.connect(lambda: self.zoomout(CHANNEL)), self.zoomOuts, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        fun(map(lambda clearGraph, CHANNEL: clearGraph.clicked.connect(lambda: self.clear(CHANNEL)), self.clearGraphs, [self.CHANNEL1, self.CHANNEL2, self.CHANNEL3]))
        self.ui.actionAbout.triggered.connect(lambda: self.showAbout())
        self.ui.actionExit.triggered.connect(lambda: self.close())
        self.ui.actionNew.triggered.connect(lambda: self.create_new_window())
        self.ui.generatePDF.clicked.connect(lambda: self.generatePDF())

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
            self.setChannelChecked[channel].setChecked(False)
            self.clear(channel)
        else:
            self.setChannelChecked[channel].setChecked(True)
            self.channelComponents[channel].show()

    def create_new_window(self):
        self.newWindow = MainWindow()
        self.newWindow.show()

    def browse(self, channel: int) -> None:
        self.hide(channel)

        # self.clear(channel)
        self.filenames[channel] = qtw.QFileDialog.getOpenFileName(None, 'Load Signal', './', "Raw Data(*.csv)")
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
        self.data_line[channel] = self.graphChannels[channel].plot(self.x[channel], self.y[channel], name='CH1', pen=self.pen[channel])
        self.graphChannels[channel].plotItem.setLimits(xMin=0, xMax=6, yMin=-(np.mean(self.y[channel]) - min(self.y[channel])), yMax=np.mean(self.y[channel]) - min(self.y[channel]))

        self.pointsToAppend[channel] = 0
        self.timers[channel].setInterval(150)
        self.timers[channel].timeout.connect(lambda: self.updatePlot(channel))
        self.timers[channel].start()

    def updatePlot(self, channel: int) -> None:
        xaxis = self.x[channel][:self.pointsToAppend[channel]]
        yaxis = self.y[channel][:self.pointsToAppend[channel]]
        self.pointsToAppend[channel] += 20
        if self.pointsToAppend[channel] > len(self.x[channel]):
            self.timers[channel].stop()

        if self.x[channel][self.pointsToAppend[channel]] > 1.0:
            self.graphChannels[channel].setLimits(xMin=min(xaxis, default=0), xMax=max(xaxis, default=0))
        self.graphChannels[channel].plotItem.setXRange(max(xaxis, default=0)-1.0, max(xaxis, default=0))

        self.data_line[channel].setData(xaxis, yaxis)

    def plotSpectrogram(self, channel: int) -> None:
        fs = 1 / (self.x[channel][1] - self.x[channel][0])
        yaxis = np.array(self.y[channel])
        f, t, Sxx = scipy.signal.spectrogram(yaxis, fs)
        p1 = self.spectrogramChannels[channel].addPlot()

        img = pg.ImageItem()
        p1.addItem(img)
        hist = pg.HistogramLUTItem()
        hist.setImageItem(img)
        self.spectrogramChannels[channel].addItem(p1)
        self.spectrogramChannels[channel].show()
        hist.setLevels(np.min(Sxx), np.max(Sxx))
        hist.gradient.restoreState(
            {'mode': 'rgb',
             'ticks': [(0.5, (0, 182, 188, 255)),
                       (1.0, (246, 111, 0, 255)),
                       (0.0, (75, 0, 113, 255))]
             })
        hist.gradient.showTicks(False)
        hist.shape
        hist.layout.setContentsMargins(0, 0, 0, 0)
        hist.vb.setMouseEnabled(x=False, y=False)
        hist.vb.setMenuEnabled(False)
        img.setImage(Sxx)
        img.scale(t[-1]/np.size(Sxx, axis=1), f[-1]/np.size(Sxx, axis=0))
        p1.setLimits(xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        # Add labels to the axis
        # p1.setLabel('bottom', "Time", units='s')
        # If you include the units, Pyqtgraph automatically scales the axis and adjusts the SI prefix (in this case kHz)
        # p1.setLabel('left', "Frequency", units='Hz')

    def zoomin(self, channel: int) -> None:
        self.graphChannels[channel].plotItem.getViewBox().scaleBy((0.75, 0.75))

    def zoomout(self, channel: int) -> None:
        self.graphChannels[channel].plotItem.getViewBox().scaleBy((1.25, 1.25))

    def generatePDF(self):
        try:
            shutil.rmtree(self.PLOT_DIR)
            os.mkdir(self.PLOT_DIR)
        except FileNotFoundError:
            os.mkdir(self.PLOT_DIR)

        images = [0, 0, 0]
        for i in range(3):
            if self.y[i]:
                images[i] = 1
            else:
                self.hide(i)

        for i in range(3):
            if images[i]:
                exporter = pg.exporters.ImageExporter(self.graphChannels[i].plotItem)
                exporter.parameters()['width'] = 470
                exporter.export(f'{self.PLOT_DIR}/plot-{i}.png')

                exporter = pg.exporters.ImageExporter(self.spectrogramChannels[i].scene())
                exporter.export(f'{self.PLOT_DIR}/spec-{i}.png')

        pdf = PDF()
        plots_per_page = pdf.construct(self.PLOT_DIR)

        for elem in plots_per_page:
            pdf.print_page(elem, self.PLOT_DIR)
        try:
            os.mkdir(self.PDF_DIR)
        except:
            pass
        outFileName = qtw.QFileDialog.getSaveFileName(None, 'Load Signal', './', "Document(*.pdf)")
        pdf.output(f'{outFileName[0]}', 'F')
        try:
            shutil.rmtree(self.PLOT_DIR)
        except:
            pass

        qtw.QMessageBox.information(self, 'success', 'PDF has been created')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
