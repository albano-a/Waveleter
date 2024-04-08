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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QHBoxLayout,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindowWaveleter(object):
    def setupUi(self, MainWindowWaveleter):
        if not MainWindowWaveleter.objectName():
            MainWindowWaveleter.setObjectName(u"MainWindowWaveleter")
        MainWindowWaveleter.resize(1004, 788)
        self.centralwidget = QWidget(MainWindowWaveleter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: #fff;\n"
"	border: 1px solid #212121\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        MainWindowWaveleter.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowWaveleter)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1004, 21))
        MainWindowWaveleter.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowWaveleter)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowWaveleter.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindowWaveleter)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMinimumSize(QSize(150, 150))
        self.dockWidget.setMaximumSize(QSize(524287, 524287))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindowWaveleter.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)

        self.retranslateUi(MainWindowWaveleter)

        QMetaObject.connectSlotsByName(MainWindowWaveleter)
    # setupUi

    def retranslateUi(self, MainWindowWaveleter):
        MainWindowWaveleter.setWindowTitle(QCoreApplication.translate("MainWindowWaveleter", u"MainWindow", None))
    # retranslateUi

