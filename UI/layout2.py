# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 1146)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Images/MainIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.showChannels = QtWidgets.QHBoxLayout()
        self.showChannels.setObjectName("showChannels")
        self.showChannel1 = QtWidgets.QCheckBox(self.centralwidget)
        self.showChannel1.setObjectName("showChannel1")
        self.showChannels.addWidget(self.showChannel1)
        self.showChannel2 = QtWidgets.QCheckBox(self.centralwidget)
        self.showChannel2.setObjectName("showChannel2")
        self.showChannels.addWidget(self.showChannel2)
        self.showChannel3 = QtWidgets.QCheckBox(self.centralwidget)
        self.showChannel3.setObjectName("showChannel3")
        self.showChannels.addWidget(self.showChannel3)
        self.verticalLayout_4.addLayout(self.showChannels)
        self.Channel1Components = QtWidgets.QHBoxLayout()
        self.Channel1Components.setObjectName("Channel1Components")
        self.channel1Graphs = QtWidgets.QVBoxLayout()
        self.channel1Graphs.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.channel1Graphs.setObjectName("channel1Graphs")
        self.graph1Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graph1Label.setFont(font)
        self.graph1Label.setObjectName("graph1Label")
        self.channel1Graphs.addWidget(self.graph1Label)
        self.signal1Graph = PlotWidget(self.centralwidget)
        self.signal1Graph.setObjectName("signal1Graph")
        self.channel1Graphs.addWidget(self.signal1Graph)
        self.spectrogram1Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spectrogram1Label.setFont(font)
        self.spectrogram1Label.setObjectName("spectrogram1Label")
        self.channel1Graphs.addWidget(self.spectrogram1Label)
        self.sepctrogram1Graph = PlotWidget(self.centralwidget)
        self.sepctrogram1Graph.setObjectName("sepctrogram1Graph")
        self.channel1Graphs.addWidget(self.sepctrogram1Graph)
        self.Channel1Components.addLayout(self.channel1Graphs)
        self.controls1 = QtWidgets.QVBoxLayout()
        self.controls1.setObjectName("controls1")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls1.addItem(spacerItem)
        self.playBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn1.setEnabled(True)
        self.playBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.playBtn1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBtn1.setIcon(icon1)
        self.playBtn1.setObjectName("playBtn1")
        self.controls1.addWidget(self.playBtn1)
        self.pauseBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pauseBtn1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\Images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseBtn1.setIcon(icon2)
        self.pauseBtn1.setObjectName("pauseBtn1")
        self.controls1.addWidget(self.pauseBtn1)
        self.stopBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.stopBtn1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\Images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopBtn1.setIcon(icon3)
        self.stopBtn1.setObjectName("stopBtn1")
        self.controls1.addWidget(self.stopBtn1)
        self.zoomInBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomInBtn1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\Images/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomInBtn1.setIcon(icon4)
        self.zoomInBtn1.setObjectName("zoomInBtn1")
        self.controls1.addWidget(self.zoomInBtn1)
        self.zoonOutBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoonOutBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoonOutBtn1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\Images/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoonOutBtn1.setIcon(icon5)
        self.zoonOutBtn1.setObjectName("zoonOutBtn1")
        self.controls1.addWidget(self.zoonOutBtn1)
        self.clearBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clearBtn1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\Images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearBtn1.setIcon(icon6)
        self.clearBtn1.setObjectName("clearBtn1")
        self.controls1.addWidget(self.clearBtn1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls1.addItem(spacerItem1)
        self.Channel1Components.addLayout(self.controls1)
        self.verticalLayout_4.addLayout(self.Channel1Components)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.Channel2Components = QtWidgets.QHBoxLayout()
        self.Channel2Components.setObjectName("Channel2Components")
        self.Channel2Graphs = QtWidgets.QVBoxLayout()
        self.Channel2Graphs.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Channel2Graphs.setObjectName("Channel2Graphs")
        self.graph2Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graph2Label.setFont(font)
        self.graph2Label.setObjectName("graph2Label")
        self.Channel2Graphs.addWidget(self.graph2Label)
        self.signal2Graph = PlotWidget(self.centralwidget)
        self.signal2Graph.setObjectName("signal2Graph")
        self.Channel2Graphs.addWidget(self.signal2Graph)
        self.spectrogram2Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spectrogram2Label.setFont(font)
        self.spectrogram2Label.setObjectName("spectrogram2Label")
        self.Channel2Graphs.addWidget(self.spectrogram2Label)
        self.spectrogram2Graph = PlotWidget(self.centralwidget)
        self.spectrogram2Graph.setObjectName("spectrogram2Graph")
        self.Channel2Graphs.addWidget(self.spectrogram2Graph)
        self.Channel2Components.addLayout(self.Channel2Graphs)
        self.controls2 = QtWidgets.QVBoxLayout()
        self.controls2.setObjectName("controls2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls2.addItem(spacerItem2)
        self.playBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn2.setEnabled(True)
        self.playBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.playBtn2.setText("")
        self.playBtn2.setIcon(icon1)
        self.playBtn2.setObjectName("playBtn2")
        self.controls2.addWidget(self.playBtn2)
        self.pauseBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pauseBtn2.setText("")
        self.pauseBtn2.setIcon(icon2)
        self.pauseBtn2.setObjectName("pauseBtn2")
        self.controls2.addWidget(self.pauseBtn2)
        self.stopBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.stopBtn2.setText("")
        self.stopBtn2.setIcon(icon3)
        self.stopBtn2.setObjectName("stopBtn2")
        self.controls2.addWidget(self.stopBtn2)
        self.zoomInBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomInBtn2.setText("")
        self.zoomInBtn2.setIcon(icon4)
        self.zoomInBtn2.setObjectName("zoomInBtn2")
        self.controls2.addWidget(self.zoomInBtn2)
        self.zoonOutBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoonOutBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoonOutBtn2.setText("")
        self.zoonOutBtn2.setIcon(icon5)
        self.zoonOutBtn2.setObjectName("zoonOutBtn2")
        self.controls2.addWidget(self.zoonOutBtn2)
        self.clearBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clearBtn2.setText("")
        self.clearBtn2.setIcon(icon6)
        self.clearBtn2.setObjectName("clearBtn2")
        self.controls2.addWidget(self.clearBtn2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls2.addItem(spacerItem3)
        self.Channel2Components.addLayout(self.controls2)
        self.verticalLayout_4.addLayout(self.Channel2Components)
        self.Channel3Components = QtWidgets.QHBoxLayout()
        self.Channel3Components.setObjectName("Channel3Components")
        self.channel3Graphs = QtWidgets.QVBoxLayout()
        self.channel3Graphs.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.channel3Graphs.setObjectName("channel3Graphs")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.channel3Graphs.addWidget(self.line_2)
        self.graph3Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graph3Label.setFont(font)
        self.graph3Label.setObjectName("graph3Label")
        self.channel3Graphs.addWidget(self.graph3Label)
        self.signal3Graph = PlotWidget(self.centralwidget)
        self.signal3Graph.setObjectName("signal3Graph")
        self.channel3Graphs.addWidget(self.signal3Graph)
        self.spectrogram3Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spectrogram3Label.setFont(font)
        self.spectrogram3Label.setObjectName("spectrogram3Label")
        self.channel3Graphs.addWidget(self.spectrogram3Label)
        self.spectrogram3Graph = PlotWidget(self.centralwidget)
        self.spectrogram3Graph.setObjectName("spectrogram3Graph")
        self.channel3Graphs.addWidget(self.spectrogram3Graph)
        self.Channel3Components.addLayout(self.channel3Graphs)
        self.control3 = QtWidgets.QVBoxLayout()
        self.control3.setObjectName("control3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.control3.addItem(spacerItem4)
        self.playBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn3.setEnabled(True)
        self.playBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.playBtn3.setText("")
        self.playBtn3.setIcon(icon1)
        self.playBtn3.setObjectName("playBtn3")
        self.control3.addWidget(self.playBtn3)
        self.pauseBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pauseBtn3.setText("")
        self.pauseBtn3.setIcon(icon2)
        self.pauseBtn3.setObjectName("pauseBtn3")
        self.control3.addWidget(self.pauseBtn3)
        self.stopBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.stopBtn3.setText("")
        self.stopBtn3.setIcon(icon3)
        self.stopBtn3.setObjectName("stopBtn3")
        self.control3.addWidget(self.stopBtn3)
        self.zoomInBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoomInBtn3.setText("")
        self.zoomInBtn3.setIcon(icon4)
        self.zoomInBtn3.setObjectName("zoomInBtn3")
        self.control3.addWidget(self.zoomInBtn3)
        self.zoonOutBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoonOutBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zoonOutBtn3.setText("")
        self.zoonOutBtn3.setIcon(icon5)
        self.zoonOutBtn3.setObjectName("zoonOutBtn3")
        self.control3.addWidget(self.zoonOutBtn3)
        self.clearBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clearBtn3.setText("")
        self.clearBtn3.setIcon(icon6)
        self.clearBtn3.setObjectName("clearBtn3")
        self.control3.addWidget(self.clearBtn3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.control3.addItem(spacerItem5)
        self.Channel3Components.addLayout(self.control3)
        self.verticalLayout_4.addLayout(self.Channel3Components)
        self.ReportComponent = QtWidgets.QHBoxLayout()
        self.ReportComponent.setObjectName("ReportComponent")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ReportComponent.addItem(spacerItem6)
        self.generateReport = QtWidgets.QPushButton(self.centralwidget)
        self.generateReport.setMaximumSize(QtCore.QSize(800, 800))
        self.generateReport.setObjectName("generateReport")
        self.ReportComponent.addWidget(self.generateReport)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ReportComponent.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.ReportComponent)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenChannel1 = QtWidgets.QAction(MainWindow)
        self.actionOpenChannel1.setObjectName("actionOpenChannel1")
        self.actionOpenChannel2 = QtWidgets.QAction(MainWindow)
        self.actionOpenChannel2.setObjectName("actionOpenChannel2")
        self.actionOpenChannel3 = QtWidgets.QAction(MainWindow)
        self.actionOpenChannel3.setObjectName("actionOpenChannel3")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGenerateReport = QtWidgets.QAction(MainWindow)
        self.actionGenerateReport.setObjectName("actionGenerateReport")
        self.menuOpen.addAction(self.actionOpenChannel1)
        self.menuOpen.addAction(self.actionOpenChannel2)
        self.menuOpen.addAction(self.actionOpenChannel3)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionGenerateReport)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SBME - Signal Viewer"))
        self.showChannel1.setText(_translate("MainWindow", "CH1"))
        self.showChannel1.setShortcut(_translate("MainWindow", "Alt+1"))
        self.showChannel2.setText(_translate("MainWindow", "CH2"))
        self.showChannel2.setShortcut(_translate("MainWindow", "Alt+2"))
        self.showChannel3.setText(_translate("MainWindow", "CH3"))
        self.showChannel3.setShortcut(_translate("MainWindow", "Alt+3"))
        self.graph1Label.setText(_translate("MainWindow", "Channel 1 Graph"))
        self.spectrogram1Label.setText(_translate("MainWindow", "Channel 1 Spectrogram"))
        self.graph2Label.setText(_translate("MainWindow", "Channel 2 Graph"))
        self.spectrogram2Label.setText(_translate("MainWindow", "Channel 2 Spectrogram"))
        self.graph3Label.setText(_translate("MainWindow", "Channel 3 Graph"))
        self.spectrogram3Label.setText(_translate("MainWindow", "Channel 3 Spectrogram"))
        self.generateReport.setText(_translate("MainWindow", "Generate PDF"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionOpenChannel1.setText(_translate("MainWindow", "Channel 1"))
        self.actionOpenChannel1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionOpenChannel2.setText(_translate("MainWindow", "Channel 2"))
        self.actionOpenChannel2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionOpenChannel3.setText(_translate("MainWindow", "Channel 3"))
        self.actionOpenChannel3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "F1"))
        self.actionGenerateReport.setText(_translate("MainWindow", "Generate Report"))
        self.actionGenerateReport.setShortcut(_translate("MainWindow", "Ctrl+S"))
from pyqtgraph import PlotWidget
