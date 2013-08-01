# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/test_results.ui'
#
# Created: Thu Aug  1 23:58:38 2013
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

class Ui_TestResultsFrame(object):
    def setupUi(self, TestResultsFrame):
        TestResultsFrame.setObjectName(_fromUtf8("TestResultsFrame"))
        TestResultsFrame.resize(276, 292)
        TestResultsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        TestResultsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(TestResultsFrame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(TestResultsFrame)
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.resultsLabel = QtGui.QLabel(TestResultsFrame)
        self.resultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultsLabel.setObjectName(_fromUtf8("resultsLabel"))
        self.verticalLayout.addWidget(self.resultsLabel)
        self.line = QtGui.QFrame(TestResultsFrame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.wrongAnswersLabel = QtGui.QLabel(TestResultsFrame)
        self.wrongAnswersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.wrongAnswersLabel.setObjectName(_fromUtf8("wrongAnswersLabel"))
        self.verticalLayout.addWidget(self.wrongAnswersLabel)
        self.wrongAnswersTableView = QtGui.QTableView(TestResultsFrame)
        self.wrongAnswersTableView.setObjectName(_fromUtf8("wrongAnswersTableView"))
        self.verticalLayout.addWidget(self.wrongAnswersTableView)

        self.retranslateUi(TestResultsFrame)
        QtCore.QMetaObject.connectSlotsByName(TestResultsFrame)

    def retranslateUi(self, TestResultsFrame):
        TestResultsFrame.setWindowTitle(_translate("TestResultsFrame", "Frame", None))
        self.headerLabel.setText(_translate("TestResultsFrame", "Wyniki:", None))
        self.resultsLabel.setText(_translate("TestResultsFrame", "poprawnych odpowiedzi", None))
        self.wrongAnswersLabel.setText(_translate("TestResultsFrame", "Błędne odpowiedzi:", None))

