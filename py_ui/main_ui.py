# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Sun Jul 14 01:15:30 2013
#      by: PyQt4 UI code generator 4.10.2-snapshot-74ade0e1faf2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(200, 300)
        MainWindow.setMinimumSize(QtCore.QSize(200, 300))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.addPoSButton = QtGui.QPushButton(self.centralwidget)
        self.addPoSButton.setObjectName(_fromUtf8("addPoSButton"))
        self.verticalLayout.addWidget(self.addPoSButton)
        self.testButton = QtGui.QPushButton(self.centralwidget)
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.verticalLayout.addWidget(self.testButton)
        self.dictionaryButton = QtGui.QPushButton(self.centralwidget)
        self.dictionaryButton.setObjectName(_fromUtf8("dictionaryButton"))
        self.verticalLayout.addWidget(self.dictionaryButton)
        self.optionsButton = QtGui.QPushButton(self.centralwidget)
        self.optionsButton.setObjectName(_fromUtf8("optionsButton"))
        self.verticalLayout.addWidget(self.optionsButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.userName = QtGui.QStatusBar(MainWindow)
        self.userName.setObjectName(_fromUtf8("userName"))
        MainWindow.setStatusBar(self.userName)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Lanler", None))
        self.addPoSButton.setText(_translate("MainWindow", "Dodaj ...", None))
        self.testButton.setText(_translate("MainWindow", "Test", None))
        self.dictionaryButton.setText(_translate("MainWindow", "Słownik", None))
        self.optionsButton.setText(_translate("MainWindow", "Opcje", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

