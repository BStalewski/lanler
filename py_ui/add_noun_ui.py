# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add_noun.ui'
#
# Created: Sun Jun 30 20:02:45 2013
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

class Ui_AddNounDialog(object):
    def setupUi(self, AddNounDialog):
        AddNounDialog.setObjectName(_fromUtf8("AddNounDialog"))
        AddNounDialog.resize(240, 320)
        self.verticalLayout = QtGui.QVBoxLayout(AddNounDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.polishLabel = QtGui.QLabel(AddNounDialog)
        self.polishLabel.setObjectName(_fromUtf8("polishLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.polishLabel)
        self.portugueseLabel = QtGui.QLabel(AddNounDialog)
        self.portugueseLabel.setObjectName(_fromUtf8("portugueseLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.portugueseLabel)
        self.polishLineEdit = QtGui.QLineEdit(AddNounDialog)
        self.polishLineEdit.setObjectName(_fromUtf8("polishLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.polishLineEdit)
        self.portugueseLineEdit = QtGui.QLineEdit(AddNounDialog)
        self.portugueseLineEdit.setObjectName(_fromUtf8("portugueseLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.portugueseLineEdit)
        self.genderGroupBox = QtGui.QGroupBox(AddNounDialog)
        self.genderGroupBox.setObjectName(_fromUtf8("genderGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.genderGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.masculineRadioButton = QtGui.QRadioButton(self.genderGroupBox)
        self.masculineRadioButton.setChecked(True)
        self.masculineRadioButton.setObjectName(_fromUtf8("masculineRadioButton"))
        self.verticalLayout_2.addWidget(self.masculineRadioButton)
        self.FeminineRadioButton = QtGui.QRadioButton(self.genderGroupBox)
        self.FeminineRadioButton.setObjectName(_fromUtf8("FeminineRadioButton"))
        self.verticalLayout_2.addWidget(self.FeminineRadioButton)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.genderGroupBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddNounDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddNounDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddNounDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddNounDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddNounDialog)

    def retranslateUi(self, AddNounDialog):
        AddNounDialog.setWindowTitle(_translate("AddNounDialog", "Dialog", None))
        self.polishLabel.setText(_translate("AddNounDialog", "polski", None))
        self.portugueseLabel.setText(_translate("AddNounDialog", "portugalski", None))
        self.genderGroupBox.setTitle(_translate("AddNounDialog", "Rodzaj:", None))
        self.masculineRadioButton.setText(_translate("AddNounDialog", "męski", None))
        self.FeminineRadioButton.setText(_translate("AddNounDialog", "żeński", None))

