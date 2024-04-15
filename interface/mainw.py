# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMdiArea, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindowWaveleter(object):
    def setupUi(self, MainWindowWaveleter):
        if not MainWindowWaveleter.objectName():
            MainWindowWaveleter.setObjectName(u"MainWindowWaveleter")
        MainWindowWaveleter.resize(1092, 850)
        MainWindowWaveleter.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	border: 1px solid #ababab;\n"
"	height: 20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.454545, y1:0, x2:0.454545, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0.454545, y1:0, x2:0.454545, y2:1, stop:0 rgba(254, 254, 254, 255), stop:1 rgba(248, 248, 248, 255));\n"
"}")
        self.actionViewSideBar = QAction(MainWindowWaveleter)
        self.actionViewSideBar.setObjectName(u"actionViewSideBar")
        self.centralwidget = QWidget(MainWindowWaveleter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout.addWidget(self.mdiArea)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.homeButton = QPushButton(self.frame_3)
        self.homeButton.setObjectName(u"homeButton")

        self.horizontalLayout.addWidget(self.homeButton)

        self.backButton = QPushButton(self.frame_3)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)

        self.forwardButton = QPushButton(self.frame_3)
        self.forwardButton.setObjectName(u"forwardButton")

        self.horizontalLayout.addWidget(self.forwardButton)

        self.panButton = QPushButton(self.frame_3)
        self.panButton.setObjectName(u"panButton")

        self.horizontalLayout.addWidget(self.panButton)

        self.zoomButton = QPushButton(self.frame_3)
        self.zoomButton.setObjectName(u"zoomButton")

        self.horizontalLayout.addWidget(self.zoomButton)

        self.configureSubPlots = QPushButton(self.frame_3)
        self.configureSubPlots.setObjectName(u"configureSubPlots")

        self.horizontalLayout.addWidget(self.configureSubPlots)

        self.editButton = QPushButton(self.frame_3)
        self.editButton.setObjectName(u"editButton")

        self.horizontalLayout.addWidget(self.editButton)

        self.saveButton = QPushButton(self.frame_3)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindowWaveleter.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowWaveleter)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1092, 21))
        self.menuSidebar = QMenu(self.menubar)
        self.menuSidebar.setObjectName(u"menuSidebar")
        MainWindowWaveleter.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowWaveleter)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowWaveleter.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindowWaveleter)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMinimumSize(QSize(250, 320))
        self.dockWidget.setMaximumSize(QSize(524287, 524287))
        self.dockWidget.setStyleSheet(u"QDockWidget::title {\n"
"    background: #f7f7f7;\n"
"}")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout_2 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 230, 767))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: #f7f7f7;\n"
"	border: 1px solid #f0f0f0;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.waveletSelector = QComboBox(self.frame_2)
        self.waveletSelector.setObjectName(u"waveletSelector")
        font = QFont()
        font.setPointSize(12)
        self.waveletSelector.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.waveletSelector)

        self.highFreqLabel = QLabel(self.frame_2)
        self.highFreqLabel.setObjectName(u"highFreqLabel")
        self.highFreqLabel.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.highFreqLabel)

        self.highFreqInput = QLineEdit(self.frame_2)
        self.highFreqInput.setObjectName(u"highFreqInput")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.highFreqInput)

        self.lowFreqLabel = QLabel(self.frame_2)
        self.lowFreqLabel.setObjectName(u"lowFreqLabel")
        self.lowFreqLabel.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.lowFreqLabel)

        self.lowFreqInput = QLineEdit(self.frame_2)
        self.lowFreqInput.setObjectName(u"lowFreqInput")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.lowFreqInput)

        self.labelf3 = QLabel(self.frame_2)
        self.labelf3.setObjectName(u"labelf3")
        self.labelf3.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"}")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.labelf3)

        self.frequency3Input = QLineEdit(self.frame_2)
        self.frequency3Input.setObjectName(u"frequency3Input")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.frequency3Input)

        self.labelf4 = QLabel(self.frame_2)
        self.labelf4.setObjectName(u"labelf4")
        self.labelf4.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"}")

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.labelf4)

        self.frequency4Input = QLineEdit(self.frame_2)
        self.frequency4Input.setObjectName(u"frequency4Input")

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.frequency4Input)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"}")

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.label_4)

        self.samplesInput = QLineEdit(self.frame_2)
        self.samplesInput.setObjectName(u"samplesInput")

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.samplesInput)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	border: None;\n"
"}")

        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.label_5)

        self.timeInput = QLineEdit(self.frame_2)
        self.timeInput.setObjectName(u"timeInput")

        self.formLayout.setWidget(13, QFormLayout.SpanningRole, self.timeInput)

        self.plotWavButton = QPushButton(self.frame_2)
        self.plotWavButton.setObjectName(u"plotWavButton")
        self.plotWavButton.setEnabled(True)
        self.plotWavButton.setFont(font)

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.plotWavButton)


        self.horizontalLayout_4.addLayout(self.formLayout)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindowWaveleter.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        QWidget.setTabOrder(self.highFreqInput, self.lowFreqInput)
        QWidget.setTabOrder(self.lowFreqInput, self.frequency3Input)
        QWidget.setTabOrder(self.frequency3Input, self.frequency4Input)
        QWidget.setTabOrder(self.frequency4Input, self.samplesInput)
        QWidget.setTabOrder(self.samplesInput, self.timeInput)
        QWidget.setTabOrder(self.timeInput, self.plotWavButton)
        QWidget.setTabOrder(self.plotWavButton, self.homeButton)
        QWidget.setTabOrder(self.homeButton, self.backButton)
        QWidget.setTabOrder(self.backButton, self.forwardButton)
        QWidget.setTabOrder(self.forwardButton, self.panButton)
        QWidget.setTabOrder(self.panButton, self.zoomButton)
        QWidget.setTabOrder(self.zoomButton, self.configureSubPlots)
        QWidget.setTabOrder(self.configureSubPlots, self.editButton)
        QWidget.setTabOrder(self.editButton, self.saveButton)
        QWidget.setTabOrder(self.saveButton, self.waveletSelector)
        QWidget.setTabOrder(self.waveletSelector, self.scrollArea)

        self.menubar.addAction(self.menuSidebar.menuAction())
        self.menuSidebar.addAction(self.actionViewSideBar)

        self.retranslateUi(MainWindowWaveleter)

        QMetaObject.connectSlotsByName(MainWindowWaveleter)
    # setupUi

    def retranslateUi(self, MainWindowWaveleter):
        MainWindowWaveleter.setWindowTitle(QCoreApplication.translate("MainWindowWaveleter", u"Waveleter", None))
        self.actionViewSideBar.setText(QCoreApplication.translate("MainWindowWaveleter", u"Sidebar", None))
#if QT_CONFIG(statustip)
        self.homeButton.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Reset original view", None))
#endif // QT_CONFIG(statustip)
        self.homeButton.setText(QCoreApplication.translate("MainWindowWaveleter", u"Home", None))
#if QT_CONFIG(statustip)
        self.backButton.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Back to previous view", None))
#endif // QT_CONFIG(statustip)
        self.backButton.setText(QCoreApplication.translate("MainWindowWaveleter", u"Back", None))
#if QT_CONFIG(statustip)
        self.forwardButton.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Forward to next view", None))
#endif // QT_CONFIG(statustip)
        self.forwardButton.setText(QCoreApplication.translate("MainWindowWaveleter", u"Forward", None))
#if QT_CONFIG(statustip)
        self.panButton.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Left buttons pans, Right button zooms x/y fixes axis, CTRL fixes aspect", None))
#endif // QT_CONFIG(statustip)
        self.panButton.setText(QCoreApplication.translate("MainWindowWaveleter", u"Pan", None))
#if QT_CONFIG(statustip)
        self.zoomButton.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Zoom to rectangle x/y fixes axis", None))
#endif // QT_CONFIG(statustip)
        self.zoomButton.setText(QCoreApplication.translate("MainWindowWaveleter", u"Zoom", None))
#if QT_CONFIG(statustip)
        self.configureSubPlots.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Configure subplots", None))
#endif // QT_CONFIG(statustip)
        self.configureSubPlots.setText(QCoreApplication.translate("MainWindowWaveleter", u"Configure", None))
#if QT_CONFIG(statustip)
        self.editButton.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Edit axis, curve and image parameters", None))
#endif // QT_CONFIG(statustip)
        self.editButton.setText(QCoreApplication.translate("MainWindowWaveleter", u"Edit", None))
#if QT_CONFIG(statustip)
        self.saveButton.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Save the figure", None))
#endif // QT_CONFIG(statustip)
        self.saveButton.setText(QCoreApplication.translate("MainWindowWaveleter", u"Save", None))
        self.menuSidebar.setTitle(QCoreApplication.translate("MainWindowWaveleter", u"View", None))
        self.dockWidget.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("MainWindowWaveleter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Wavelet</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.waveletSelector.setStatusTip(QCoreApplication.translate("MainWindowWaveleter", u"Choose between differents wavelets to plot", None))
#endif // QT_CONFIG(statustip)
        self.highFreqLabel.setText(QCoreApplication.translate("MainWindowWaveleter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">High Frequency</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.highFreqInput.setToolTip(QCoreApplication.translate("MainWindowWaveleter", u"Enter the high frequency or peak frequency of your wavelet", None))
#endif // QT_CONFIG(tooltip)
        self.lowFreqLabel.setText(QCoreApplication.translate("MainWindowWaveleter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Low Frequency</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lowFreqInput.setToolTip(QCoreApplication.translate("MainWindowWaveleter", u"Enter the low frequency, if needed", None))
#endif // QT_CONFIG(tooltip)
        self.labelf3.setText(QCoreApplication.translate("MainWindowWaveleter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">High Cutoff Frequency</span></p></body></html>", None))
        self.labelf4.setText(QCoreApplication.translate("MainWindowWaveleter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Low Cutoff Frequency</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowWaveleter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Samples</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindowWaveleter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Time (ms)</span></p></body></html>", None))
        self.plotWavButton.setText(QCoreApplication.translate("MainWindowWaveleter", u"Plot", None))
    # retranslateUi

