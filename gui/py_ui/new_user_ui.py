# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/new_user.ui'
#
# Created: Tue Jul 30 23:48:48 2013
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

class Ui_NewUserDialog(object):
    def setupUi(self, NewUserDialog):
        NewUserDialog.setObjectName(_fromUtf8("NewUserDialog"))
        NewUserDialog.resize(274, 146)
        self.gridLayout = QtGui.QGridLayout(NewUserDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.userNameLabel = QtGui.QLabel(NewUserDialog)
        self.userNameLabel.setObjectName(_fromUtf8("userNameLabel"))
        self.verticalLayout.addWidget(self.userNameLabel)
        self.userNameLineEdit = QtGui.QLineEdit(NewUserDialog)
        self.userNameLineEdit.setObjectName(_fromUtf8("userNameLineEdit"))
        self.verticalLayout.addWidget(self.userNameLineEdit)
        self.line = QtGui.QFrame(NewUserDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.importGroupBox = QtGui.QGroupBox(NewUserDialog)
        self.importGroupBox.setObjectName(_fromUtf8("importGroupBox"))
        self.importGroupBoxLayout = QtGui.QVBoxLayout(self.importGroupBox)
        self.importGroupBoxLayout.setObjectName(_fromUtf8("importGroupBoxLayout"))
        self.verticalLayout.addWidget(self.importGroupBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(NewUserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(NewUserDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewUserDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewUserDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewUserDialog)

    def retranslateUi(self, NewUserDialog):
        NewUserDialog.setWindowTitle(_translate("NewUserDialog", "New user", None))
        self.userNameLabel.setText(_translate("NewUserDialog", "Nazwa użytkownika:", None))
        self.importGroupBox.setTitle(_translate("NewUserDialog", "Importuj słownictwo z innych kont:", None))

