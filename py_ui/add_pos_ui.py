# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add_pos.ui'
#
# Created: Sat Jul 13 23:56:01 2013
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

class Ui_AddPoSDialog(object):
    def setupUi(self, AddPoSDialog):
        AddPoSDialog.setObjectName(_fromUtf8("AddPoSDialog"))
        AddPoSDialog.resize(240, 320)
        self.verticalLayout = QtGui.QVBoxLayout(AddPoSDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.polishLabel = QtGui.QLabel(AddPoSDialog)
        self.polishLabel.setObjectName(_fromUtf8("polishLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.polishLabel)
        self.portugueseLabel = QtGui.QLabel(AddPoSDialog)
        self.portugueseLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.portugueseLabel.setObjectName(_fromUtf8("portugueseLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.portugueseLabel)
        self.polishLineEdit = QtGui.QLineEdit(AddPoSDialog)
        self.polishLineEdit.setObjectName(_fromUtf8("polishLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.polishLineEdit)
        self.portugueseLineEdit = PortugueseQLineEdit(AddPoSDialog)
        self.portugueseLineEdit.setObjectName(_fromUtf8("portugueseLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.portugueseLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddPoSDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddPoSDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddPoSDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddPoSDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddPoSDialog)

    def retranslateUi(self, AddPoSDialog):
        AddPoSDialog.setWindowTitle(_translate("AddPoSDialog", "Dialog", None))
        self.polishLabel.setText(_translate("AddPoSDialog", "polski", None))
        self.portugueseLabel.setText(_translate("AddPoSDialog", "portugalski", None))

from custom_widgets.portuguese_qlineedit import PortugueseQLineEdit
