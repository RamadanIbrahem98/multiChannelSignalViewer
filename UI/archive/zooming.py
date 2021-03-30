import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

win = pg.GraphicsWindow()
win.setWindowTitle('Scroll and Zoomed Plot')

plotScroll = win.addPlot()
plotScroll.setDownsampling(mode='peak')
plotScroll.setClipToView(True)
curveScroll = plotScroll.plot()

dataRnd = np.empty(100)
ptrDataRnd = 0


def updateScroll():
    global dataRnd, ptrDataRnd
    dataRnd[ptrDataRnd] = np.random.normal()
    ptrDataRnd += 1
    if ptrDataRnd >= dataRnd.shape[0]:
        tmp = dataRnd
        dataRnd = np.empty(dataRnd.shape[0] * 2)
        dataRnd[:tmp.shape[0]] = tmp
    curveScroll.setData(dataRnd[:ptrDataRnd])


LinRegionItem = pg.LinearRegionItem([0, 100])
LinRegionItem.setZValue(-10)
plotScroll.addItem(LinRegionItem)

win.nextRow()

plotZoom = win.addPlot(title="Zoomed graph for Random plot ")
plotZoom.plot(dataRnd, pen=(255, 255, 255, 200))


def updatePlot():
    plotZoom.setXRange(*LinRegionItem.getRegion(), padding=0)


def updateRegion():
    LinRegionItem.setRegion(plotZoom.getViewBox().viewRange()[0])


LinRegionItem.sigRegionChanged.connect(updatePlot)
plotZoom.sigXRangeChanged.connect(updateRegion)
updatePlot()

# update all plots


def update():
    updateScroll()


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
