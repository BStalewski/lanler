#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QFrame

from commons import CLICKED_SIGNAL, NotImplementedException, RightFrame
from py_ui.test_params_ui import Ui_TestParamsFrame


class TestParamsFrame(QFrame, Ui_TestParamsFrame):
    MIN_TESTS = 1
    MAX_TESTS = 999999

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setupUi(self)
        self.type_radios = [
            self.plPtTypeRadioButton,
            self.ptPlTypeRadioButton,
        ]
        self.date_constraint_radios = [
            self.noDateConstraintRadioButton,
            self.yesDateConstraintRadioButton,
        ]
        self.pos_checkboxes = [
            self.nounCheckBox,
            self.verbCheckBox,
            self.adjectiveCheckBox,
            self.pronounCheckBox,
        ]
        self.connect(self.checkAllPosPushButton, CLICKED_SIGNAL, self.check_all)
        self.connect(self.uncheckAllPosPushButton, CLICKED_SIGNAL, self.uncheck_all)

    def set_all_pos_checkboxes(self, checked):
        for checkbox in self.pos_checkboxes:
            checkbox.setChecked(checked)

    def check_all(self):
        self.set_all_pos_checkboxes(True)

    def uncheck_all(self):
        self.set_all_pos_checkboxes(False)

    def validate(self):
        types_radio_checked = 0
        types_checked = sum(btn.isChecked() for btn in self.type_radios)
        dates_checked = sum(btn.isChecked() for btn in self.date_constraint_radios)
        pos_checked = sum(btn.isChecked() for btn in self.pos_checkboxes)
        raise NotImplementedException()

    def get_fields(self):
        raise NotImplementedException()
