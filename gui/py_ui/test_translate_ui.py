# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/test_translate.ui'
#
# Created: Tue Jul 30 23:48:49 2013
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

class Ui_TestTranslateFrame(object):
    def setupUi(self, TestTranslateFrame):
        TestTranslateFrame.setObjectName(_fromUtf8("TestTranslateFrame"))
        TestTranslateFrame.resize(149, 231)
        TestTranslateFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        TestTranslateFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(TestTranslateFrame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.wordLabel = QtGui.QLabel(TestTranslateFrame)
        self.wordLabel.setText(_fromUtf8(""))
        self.wordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.wordLabel.setObjectName(_fromUtf8("wordLabel"))
        self.verticalLayout.addWidget(self.wordLabel)
        self.line_2 = QtGui.QFrame(TestTranslateFrame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.translateLabel = QtGui.QLabel(TestTranslateFrame)
        self.translateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.translateLabel.setObjectName(_fromUtf8("translateLabel"))
        self.verticalLayout.addWidget(self.translateLabel)
        self.translationLineEdit = QtGui.QLineEdit(TestTranslateFrame)
        self.translationLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.translationLineEdit.setObjectName(_fromUtf8("translationLineEdit"))
        self.verticalLayout.addWidget(self.translationLineEdit)
        self.line = QtGui.QFrame(TestTranslateFrame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.nextPushButton = QtGui.QPushButton(TestTranslateFrame)
        self.nextPushButton.setObjectName(_fromUtf8("nextPushButton"))
        self.verticalLayout.addWidget(self.nextPushButton)
        self.endPushButton = QtGui.QPushButton(TestTranslateFrame)
        self.endPushButton.setObjectName(_fromUtf8("endPushButton"))
        self.verticalLayout.addWidget(self.endPushButton)
        self.progressLabel = QtGui.QLabel(TestTranslateFrame)
        self.progressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
        self.verticalLayout.addWidget(self.progressLabel)
        self.progressBar = QtGui.QProgressBar(TestTranslateFrame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(TestTranslateFrame)
        QtCore.QObject.connect(self.translationLineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.nextPushButton.click)
        QtCore.QMetaObject.connectSlotsByName(TestTranslateFrame)

    def retranslateUi(self, TestTranslateFrame):
        TestTranslateFrame.setWindowTitle(_translate("TestTranslateFrame", "Frame", None))
        self.translateLabel.setText(_translate("TestTranslateFrame", "Tłumaczenie:", None))
        self.nextPushButton.setText(_translate("TestTranslateFrame", "Dalej", None))
        self.endPushButton.setText(_translate("TestTranslateFrame", "Zakończ", None))
        self.progressLabel.setText(_translate("TestTranslateFrame", "Postęp:", None))
        self.progressBar.setFormat(_translate("TestTranslateFrame", "%v/%m", None))

