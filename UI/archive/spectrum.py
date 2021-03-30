from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph
import PyQt5.QtGui as qtg

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

matplotlib.use('Qt5Agg')


class MatplotlibWidget(qtg.QWidget):
    """
    Implements a Matplotlib figure inside a QWidget.
    Use getFigure() and redraw() to interact with matplotlib.

    Example::

        mw = MatplotlibWidget()
        subplot = mw.getFigure().add_subplot(111)
        subplot.plot(x,y)
        mw.draw()
    """

    def __init__(self, size=(5.0, 4.0), dpi=100):
        qtg.QWidget.__init__(self)
        self.fig = Figure(size, dpi=dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.vbox = qtg.QVBoxLayout()
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)

    def getFigure(self):
        return self.fig

    def draw(self):
        self.canvas.draw()


# Create the data
fs = 10e3
N = 1e5
amp = 2 * np.sqrt(2)
noise_power = 0.01 * fs / 2
time = np.arange(N) / float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
carrier = amp * np.sin(2*np.pi*3e3*time + mod)
noise = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
noise *= np.exp(-time/5)
x = carrier + noise
f, t, Sxx = signal.spectrogram(x, fs)

# Interpret image data as row-major instead of col-major
pyqtgraph.setConfigOptions(imageAxisOrder='row-major')

pyqtgraph.mkQApp()
win = pyqtgraph.GraphicsLayoutWidget()
# A plot area (ViewBox + axes) for displaying the image
p1 = win.addPlot()

# Item for displaying image data
img = pyqtgraph.ImageItem()
p1.addItem(img)
# Add a histogram with which to control the gradient of the image
hist = pyqtgraph.HistogramLUTItem()
# Link the histogram to the image
hist.setImageItem(img)
# If you don't add the histogram to the window, it stays invisible, but I find it useful.
win.addItem(hist)
# Show the window
win.show()
# Fit the min and max levels of the histogram to the data available
hist.setLevels(np.min(Sxx), np.max(Sxx))
# This gradient is roughly comparable to the gradient used by Matplotlib
# You can adjust it and then save it using hist.gradient.saveState()
hist.gradient.restoreState(
    {'mode': 'rgb',
     'ticks': [(0.5, (0, 182, 188, 255)),
               (1.0, (246, 111, 0, 255)),
               (0.0, (75, 0, 113, 255))]})
# Sxx contains the amplitude for each pixel
img.setImage(Sxx)
# Scale the X and Y Axis to time and frequency (standard is pixels)
img.scale(t[-1]/np.size(Sxx, axis=1),
          f[-1]/np.size(Sxx, axis=0))
# Limit panning/zooming to the spectrogram
p1.setLimits(xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
# Add labels to the axis
p1.setLabel('bottom', "Time", units='s')
# If you include the units, Pyqtgraph automatically scales the axis and adjusts the SI prefix (in this case kHz)
p1.setLabel('left', "Frequency", units='Hz')

# Plotting with Matplotlib in comparison
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar()
plt.show()

pyqtgraph.Qt.QtGui.QApplication.instance().exec_()
