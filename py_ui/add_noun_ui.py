# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add_noun.ui'
#
# Created: Sat Jun 29 23:25:47 2013
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

class Ui_AddNounFrame(object):
    def setupUi(self, AddNounFrame):
        AddNounFrame.setObjectName(_fromUtf8("AddNounFrame"))
        AddNounFrame.resize(240, 320)
        AddNounFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        AddNounFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(AddNounFrame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(AddNounFrame)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(AddNounFrame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(AddNounFrame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(AddNounFrame)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.groupBox = QtGui.QGroupBox(AddNounFrame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_3.addWidget(self.radioButton)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(AddNounFrame)
        QtCore.QMetaObject.connectSlotsByName(AddNounFrame)

    def retranslateUi(self, AddNounFrame):
        AddNounFrame.setWindowTitle(_translate("AddNounFrame", "Frame", None))
        self.label.setText(_translate("AddNounFrame", "polski", None))
        self.label_2.setText(_translate("AddNounFrame", "portugaski", None))
        self.groupBox.setTitle(_translate("AddNounFrame", "Rodzaj:", None))
        self.radioButton_2.setText(_translate("AddNounFrame", "męski", None))
        self.radioButton.setText(_translate("AddNounFrame", "żeński", None))

