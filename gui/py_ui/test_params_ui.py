# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/test_params.ui'
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

class Ui_TestParamsFrame(object):
    def setupUi(self, TestParamsFrame):
        TestParamsFrame.setObjectName(_fromUtf8("TestParamsFrame"))
        TestParamsFrame.resize(224, 516)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TestParamsFrame.sizePolicy().hasHeightForWidth())
        TestParamsFrame.setSizePolicy(sizePolicy)
        TestParamsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        TestParamsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout_2 = QtGui.QVBoxLayout(TestParamsFrame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.typeGroupBox = QtGui.QGroupBox(TestParamsFrame)
        self.typeGroupBox.setObjectName(_fromUtf8("typeGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.typeGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plPtTypeRadioButton = QtGui.QRadioButton(self.typeGroupBox)
        self.plPtTypeRadioButton.setChecked(True)
        self.plPtTypeRadioButton.setObjectName(_fromUtf8("plPtTypeRadioButton"))
        self.verticalLayout.addWidget(self.plPtTypeRadioButton)
        self.ptPlTypeRadioButton = QtGui.QRadioButton(self.typeGroupBox)
        self.ptPlTypeRadioButton.setObjectName(_fromUtf8("ptPlTypeRadioButton"))
        self.verticalLayout.addWidget(self.ptPlTypeRadioButton)
        self.verticalLayout_2.addWidget(self.typeGroupBox)
        self.dateConstraintGroupBox = QtGui.QGroupBox(TestParamsFrame)
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
        self.daysAgoSpinBox = QtGui.QSpinBox(self.dateConstraintGroupBox)
        self.daysAgoSpinBox.setMinimum(1)
        self.daysAgoSpinBox.setMaximum(30)
        self.daysAgoSpinBox.setObjectName(_fromUtf8("daysAgoSpinBox"))
        self.verticalLayout_3.addWidget(self.daysAgoSpinBox)
        self.verticalLayout_2.addWidget(self.dateConstraintGroupBox)
        self.posChooseGroupBox = QtGui.QGroupBox(TestParamsFrame)
        self.posChooseGroupBox.setObjectName(_fromUtf8("posChooseGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.posChooseGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.nounCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.nounCheckBox.setObjectName(_fromUtf8("nounCheckBox"))
        self.verticalLayout_4.addWidget(self.nounCheckBox)
        self.verbCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.verbCheckBox.setObjectName(_fromUtf8("verbCheckBox"))
        self.verticalLayout_4.addWidget(self.verbCheckBox)
        self.adjectiveCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.adjectiveCheckBox.setObjectName(_fromUtf8("adjectiveCheckBox"))
        self.verticalLayout_4.addWidget(self.adjectiveCheckBox)
        self.pronounCheckBox = QtGui.QCheckBox(self.posChooseGroupBox)
        self.pronounCheckBox.setObjectName(_fromUtf8("pronounCheckBox"))
        self.verticalLayout_4.addWidget(self.pronounCheckBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkAllPosPushButton = QtGui.QPushButton(self.posChooseGroupBox)
        self.checkAllPosPushButton.setObjectName(_fromUtf8("checkAllPosPushButton"))
        self.horizontalLayout.addWidget(self.checkAllPosPushButton)
        self.uncheckAllPosPushButton = QtGui.QPushButton(self.posChooseGroupBox)
        self.uncheckAllPosPushButton.setObjectName(_fromUtf8("uncheckAllPosPushButton"))
        self.horizontalLayout.addWidget(self.uncheckAllPosPushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.posChooseGroupBox)
        self.testsCountGroupBox = QtGui.QGroupBox(TestParamsFrame)
        self.testsCountGroupBox.setObjectName(_fromUtf8("testsCountGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.testsCountGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.testsCountSpinBox = QtGui.QSpinBox(self.testsCountGroupBox)
        self.testsCountSpinBox.setMinimum(1)
        self.testsCountSpinBox.setMaximum(999999)
        self.testsCountSpinBox.setObjectName(_fromUtf8("testsCountSpinBox"))
        self.verticalLayout_5.addWidget(self.testsCountSpinBox)
        self.verticalLayout_2.addWidget(self.testsCountGroupBox)
        self.startPushButton = QtGui.QPushButton(TestParamsFrame)
        self.startPushButton.setObjectName(_fromUtf8("startPushButton"))
        self.verticalLayout_2.addWidget(self.startPushButton)

        self.retranslateUi(TestParamsFrame)
        QtCore.QMetaObject.connectSlotsByName(TestParamsFrame)

    def retranslateUi(self, TestParamsFrame):
        TestParamsFrame.setWindowTitle(_translate("TestParamsFrame", "Frame", None))
        self.typeGroupBox.setTitle(_translate("TestParamsFrame", "Typ testu:", None))
        self.plPtTypeRadioButton.setText(_translate("TestParamsFrame", "polski -> portugalski", None))
        self.ptPlTypeRadioButton.setText(_translate("TestParamsFrame", "portugalski -> polski", None))
        self.dateConstraintGroupBox.setTitle(_translate("TestParamsFrame", "Data ostatniej modyfikacji:", None))
        self.noDateConstraintRadioButton.setText(_translate("TestParamsFrame", "Brak ograniczenia", None))
        self.yesDateConstraintRadioButton.setText(_translate("TestParamsFrame", "Niewcześniej niż", None))
        self.daysAgoSpinBox.setSuffix(_translate("TestParamsFrame", " dni temu", None))
        self.posChooseGroupBox.setTitle(_translate("TestParamsFrame", "Części mowy:", None))
        self.nounCheckBox.setText(_translate("TestParamsFrame", "Rzeczowniki", None))
        self.verbCheckBox.setText(_translate("TestParamsFrame", "Czasowniki", None))
        self.adjectiveCheckBox.setText(_translate("TestParamsFrame", "Przymiotniki", None))
        self.pronounCheckBox.setText(_translate("TestParamsFrame", "Zaimki", None))
        self.checkAllPosPushButton.setText(_translate("TestParamsFrame", "Zaznacz", None))
        self.uncheckAllPosPushButton.setText(_translate("TestParamsFrame", "Odznacz", None))
        self.testsCountGroupBox.setTitle(_translate("TestParamsFrame", "Liczba testów:", None))
        self.startPushButton.setText(_translate("TestParamsFrame", "Rozpocznij", None))

