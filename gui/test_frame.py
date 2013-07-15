#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import QString
from PyQt4.QtGui import QFrame, QMessageBox

from commons import CLICKED_SIGNAL, NotImplementedException, RightFrame
from consts import *
from py_ui.test_params_ui import Ui_TestParamsFrame
from py_ui.test_translate_ui import Ui_TestTranslateFrame
from gui.custom_widgets.portuguese_qlineedit import make_portuguese_line_edit


class TestParamsFrame(QFrame, Ui_TestParamsFrame, RightFrame):
    MIN_TESTS = 1
    MAX_TESTS = 999999

    def __init__(self, model, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.testsCountSpinBox.setRange(self.MIN_TESTS, self.MAX_TESTS)
        self.connect(self.checkAllPosPushButton, CLICKED_SIGNAL, self.check_all)
        self.connect(self.uncheckAllPosPushButton, CLICKED_SIGNAL, self.uncheck_all)
        self.connect(self.startPushButton, CLICKED_SIGNAL, self.start_test)

        self.model = model
        self.type_radios = [
            self.plPtTypeRadioButton,
            self.ptPlTypeRadioButton,
        ]
        self.date_constraint_radios = {
            self.noDateConstraintRadioButton,
            self.yesDateConstraintRadioButton,
        }
        self.pos_checkboxes = {
            self.nounCheckBox: NOUN,
            self.verbCheckBox: VERB,
            self.adjectiveCheckBox: ADJECTIVE,
            self.pronounCheckBox: PRONOUN,
        }

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
        if types_checked != 1:
            QMessageBox.warning(self, u'Błąd', u'Błąd: dokładnie jeden typ testu musi być zaznaczony')
            return False

        dates_checked = sum(btn.isChecked() for btn in self.date_constraint_radios)
        if dates_checked != 1:
            QMessageBox.warning(self, u'Błąd', u'Błąd: dokładnie jedno ustawienie czasu musi być zaznaczone')
            return False

        pos_checked = sum(btn.isChecked() for btn in self.pos_checkboxes)
        if not pos_checked:
            QMessageBox.warning(self, u'Błąd', u'Błąd: przynajmniej jedna część mowy musi być wybrana')
            return False

        return True

    def get_test_type(self):
        if self.plPtTypeRadioButton.isChecked():
            return PL_PT_TEST
        else:
            return PT_PL_TEST

    def get_days_constraint(self):
        if self.noDateConstraintRadioButton.isChecked():
            return None
        else:
            return self.daysAgoSpinBox.value()

    def get_checked_pos(self):
        return [self.pos_checkboxes[box] for box in self.pos_checkboxes if box.isChecked()]

    def get_fields(self):
        return {
            u'test_type': self.get_test_type(),
            u'days': self.get_days_constraint(),
            u'pos': self.get_checked_pos(),
            u'count': self.testsCountSpinBox.value(),
        }

    def start_test(self):
        if self.validate():
            fields = self.get_fields()
            self.model.generate_test_words(**fields)
            word = self.model.get_next_test_word()
            new_frame = TestTranslateFrame(word, 1, fields[u'count'], self.parent())
            self.main_window.show_frame(new_frame)


class TestTranslateFrame(QFrame, Ui_TestTranslateFrame):
    def __init__(self, word, current_count, total_count, parent):
        QFrame.__init__(self, parent)
        self.setupUi(self)
        self.wordLabel.setText(word)
        self.current_count = current_count
        self.total_count = total_count
        self.progressBar.setValue(self.current_count)
        self.progressBar.setMaximum(self.total_count)

        self.connect(self.nextPushButton, CLICKED_SIGNAL, self.next_word)
        self.connect(self.endPushButton, CLICKED_SIGNAL, self.end_test)

    def next_word(self):
        raise NotImplementedException()

    def end_test(self):
        raise NotImplementedException()
