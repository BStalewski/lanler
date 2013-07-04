# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options.ui'
#
# Created: Thu Jul  4 20:45:46 2013
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

class Ui_OptionsFrame(object):
    def setupUi(self, OptionsFrame):
        OptionsFrame.setObjectName(_fromUtf8("OptionsFrame"))
        OptionsFrame.resize(263, 176)
        OptionsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        OptionsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(OptionsFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.changeUserButton = QtGui.QPushButton(OptionsFrame)
        self.changeUserButton.setObjectName(_fromUtf8("changeUserButton"))
        self.verticalLayout_2.addWidget(self.changeUserButton)
        self.removeUserButton = QtGui.QPushButton(OptionsFrame)
        self.removeUserButton.setObjectName(_fromUtf8("removeUserButton"))
        self.verticalLayout_2.addWidget(self.removeUserButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(OptionsFrame)
        QtCore.QMetaObject.connectSlotsByName(OptionsFrame)

    def retranslateUi(self, OptionsFrame):
        OptionsFrame.setWindowTitle(_translate("OptionsFrame", "Frame", None))
        self.changeUserButton.setText(_translate("OptionsFrame", "Zmień użytkownika", None))
        self.removeUserButton.setText(_translate("OptionsFrame", "Usuń użytkownika", None))

