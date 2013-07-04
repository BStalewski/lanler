# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/choose_user.ui'
#
# Created: Thu Jul  4 20:45:45 2013
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

class Ui_ChooseUserDialog(object):
    def setupUi(self, ChooseUserDialog):
        ChooseUserDialog.setObjectName(_fromUtf8("ChooseUserDialog"))
        ChooseUserDialog.resize(194, 137)
        self.gridLayout = QtGui.QGridLayout(ChooseUserDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.chooseUserGroupBox = QtGui.QGroupBox(ChooseUserDialog)
        self.chooseUserGroupBox.setObjectName(_fromUtf8("chooseUserGroupBox"))
        self.groupBoxLayout = QtGui.QVBoxLayout(self.chooseUserGroupBox)
        self.groupBoxLayout.setObjectName(_fromUtf8("groupBoxLayout"))
        self.verticalLayout.addWidget(self.chooseUserGroupBox)
        self.newUserButton = QtGui.QPushButton(ChooseUserDialog)
        self.newUserButton.setObjectName(_fromUtf8("newUserButton"))
        self.verticalLayout.addWidget(self.newUserButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ChooseUserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ChooseUserDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChooseUserDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChooseUserDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseUserDialog)

    def retranslateUi(self, ChooseUserDialog):
        ChooseUserDialog.setWindowTitle(_translate("ChooseUserDialog", "Choose user", None))
        self.chooseUserGroupBox.setTitle(_translate("ChooseUserDialog", "Wybierz użytkownika:", None))
        self.newUserButton.setText(_translate("ChooseUserDialog", "Nowy użytkownik", None))

