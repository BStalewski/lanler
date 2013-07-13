# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/test_params.ui'
#
# Created: Sat Jul 13 23:56:04 2013
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

class Ui_TestParamsDialog(object):
    def setupUi(self, TestParamsDialog):
        TestParamsDialog.setObjectName(_fromUtf8("TestParamsDialog"))
        TestParamsDialog.resize(244, 442)
        self.verticalLayout = QtGui.QVBoxLayout(TestParamsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.typeGroupBox = QtGui.QGroupBox(TestParamsDialog)
        self.typeGroupBox.setObjectName(_fromUtf8("typeGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.typeGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.plPtTypeRadioButton = QtGui.QRadioButton(self.typeGroupBox)
        self.plPtTypeRadioButton.setChecked(True)
        self.plPtTypeRadioButton.setObjectName(_fromUtf8("plPtTypeRadioButton"))
        self.verticalLayout_5.addWidget(self.plPtTypeRadioButton)
        self.ptPlTypeRadioButton = QtGui.QRadioButton(self.typeGroupBox)
        self.ptPlTypeRadioButton.setChecked(False)
        self.ptPlTypeRadioButton.setObjectName(_fromUtf8("ptPlTypeRadioButton"))
        self.verticalLayout_5.addWidget(self.ptPlTypeRadioButton)
        self.verticalLayout_2.addWidget(self.typeGroupBox)
        self.dateConstraintGroupBox = QtGui.QGroupBox(TestParamsDialog)
        self.dateConstraintGroupBox.setObjectName(_fromUtf8("dateConstraintGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dateConstraintGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.noDateConstraintRadioButton = QtGui.QRadioButton(self.dateConstraintGroupBox)
        self.noDateConstraintRadioButton.setChecked(True)
        self.noDateConstraintRadioButton.setObjectName(_fromUtf8("noDateConstraintRadioButton"))
        self.verticalLayout_3.addWidget(self.noDateConstraintRadioButton)
        self.yesDateConstraintRadioButton = QtGui.QRadioButton(self.dateConstraintGroupBox)
        self.yesDateConstraintRadioButton.setObjectName(_fromUtf8("yesDateConstraintRadioButton"))
        self.verticalLayout_3.addWidget(self.yesDateConstraintRadioButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.daysAgoLineEdit = QtGui.QLineEdit(self.dateConstraintGroupBox)
        self.daysAgoLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.daysAgoLineEdit.setObjectName(_fromUtf8("daysAgoLineEdit"))
        self.horizontalLayout.addWidget(self.daysAgoLineEdit)
        self.daysAgoLabel = QtGui.QLabel(self.dateConstraintGroupBox)
        self.daysAgoLabel.setObjectName(_fromUtf8("daysAgoLabel"))
        self.horizontalLayout.addWidget(self.daysAgoLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.dateConstraintGroupBox)
        self.posChooseGroupBox = QtGui.QGroupBox(TestParamsDialog)
        self.posChooseGroupBox.setObjectName(_fromUtf8("posChooseGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.posChooseGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.nounCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.nounCheckBox.setChecked(True)
        self.nounCheckBox.setObjectName(_fromUtf8("nounCheckBox"))
        self.verticalLayout_4.addWidget(self.nounCheckBox)
        self.verbCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.verbCheckBox.setChecked(True)
        self.verbCheckBox.setObjectName(_fromUtf8("verbCheckBox"))
        self.verticalLayout_4.addWidget(self.verbCheckBox)
        self.adjectiveCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.adjectiveCheckBox.setChecked(True)
        self.adjectiveCheckBox.setObjectName(_fromUtf8("adjectiveCheckBox"))
        self.verticalLayout_4.addWidget(self.adjectiveCheckBox)
        self.pronounCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.pronounCheckBox.setChecked(True)
        self.pronounCheckBox.setObjectName(_fromUtf8("pronounCheckBox"))
        self.verticalLayout_4.addWidget(self.pronounCheckBox)
        self.allPosCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.allPosCheckBox.setChecked(True)
        self.allPosCheckBox.setObjectName(_fromUtf8("allPosCheckBox"))
        self.verticalLayout_4.addWidget(self.allPosCheckBox)
        self.verticalLayout_2.addWidget(self.posChooseGroupBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(TestParamsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TestParamsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TestParamsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TestParamsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TestParamsDialog)

    def retranslateUi(self, TestParamsDialog):
        TestParamsDialog.setWindowTitle(_translate("TestParamsDialog", "Parametry testu", None))
        self.typeGroupBox.setTitle(_translate("TestParamsDialog", "Typ testu:", None))
        self.plPtTypeRadioButton.setText(_translate("TestParamsDialog", "polski -> portugalski", None))
        self.ptPlTypeRadioButton.setText(_translate("TestParamsDialog", "portugalski -> polski", None))
        self.dateConstraintGroupBox.setTitle(_translate("TestParamsDialog", "Data ostatniej modyfikacji:", None))
        self.noDateConstraintRadioButton.setText(_translate("TestParamsDialog", "Brak ograniczenia", None))
        self.yesDateConstraintRadioButton.setText(_translate("TestParamsDialog", "Niewcześniej niż", None))
        self.daysAgoLineEdit.setText(_translate("TestParamsDialog", "1", None))
        self.daysAgoLabel.setText(_translate("TestParamsDialog", "dni temu", None))
        self.posChooseGroupBox.setTitle(_translate("TestParamsDialog", "Części mowy:", None))
        self.nounCheckBox.setText(_translate("TestParamsDialog", "Rzeczowniki", None))
        self.verbCheckBox.setText(_translate("TestParamsDialog", "Czasowniki", None))
        self.adjectiveCheckBox.setText(_translate("TestParamsDialog", "Przymiotniki", None))
        self.pronounCheckBox.setText(_translate("TestParamsDialog", "Zaimki", None))
        self.allPosCheckBox.setText(_translate("TestParamsDialog", "Wszystkie", None))

