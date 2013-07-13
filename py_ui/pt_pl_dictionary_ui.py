# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/pt_pl_dictionary.ui'
#
# Created: Sun Jul 14 01:09:41 2013
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

class Ui_PtPlDictionaryFrame(object):
    def setupUi(self, PtPlDictionaryFrame):
        PtPlDictionaryFrame.setObjectName(_fromUtf8("PtPlDictionaryFrame"))
        PtPlDictionaryFrame.resize(276, 277)
        PtPlDictionaryFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        PtPlDictionaryFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(PtPlDictionaryFrame)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(PtPlDictionaryFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(PtPlDictionaryFrame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.dictionaryTableView = QtGui.QTableView(PtPlDictionaryFrame)
        self.dictionaryTableView.setMinimumSize(QtCore.QSize(0, 0))
        self.dictionaryTableView.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.dictionaryTableView.setObjectName(_fromUtf8("dictionaryTableView"))
        self.dictionaryTableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.dictionaryTableView)
        self.backButton = QtGui.QPushButton(PtPlDictionaryFrame)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.verticalLayout.addWidget(self.backButton)

        self.retranslateUi(PtPlDictionaryFrame)
        QtCore.QMetaObject.connectSlotsByName(PtPlDictionaryFrame)

    def retranslateUi(self, PtPlDictionaryFrame):
        PtPlDictionaryFrame.setWindowTitle(_translate("PtPlDictionaryFrame", "Frame", None))
        self.label.setText(_translate("PtPlDictionaryFrame", "Słownik portugalsko - polski", None))
        self.backButton.setText(_translate("PtPlDictionaryFrame", "Wstecz", None))

