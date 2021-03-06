#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QFrame, QMessageBox

from commons import CLICKED_SIGNAL, RightFrame
from consts import *
from model.main_model import ModelException, TestResultsModel
from py_ui.test_params_ui import Ui_TestParamsFrame
from py_ui.test_translate_ui import Ui_TestTranslateFrame
from py_ui.test_results_ui import Ui_TestResultsFrame
from custom_widgets.portuguese_qlineedit import make_portuguese_line_edit


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
            self.adverbCheckBox: ADVERB,
            self.pronounCheckBox: PRONOUN,
            self.numeralCheckBox: NUMERAL,
            self.conjunctionCheckBox: CONJUNCTION,
        }

    def set_all_pos_checkboxes(self, checked):
        for checkbox in self.pos_checkboxes:
            checkbox.setChecked(checked)

    def check_all(self):
        self.set_all_pos_checkboxes(True)

    def uncheck_all(self):
        self.set_all_pos_checkboxes(False)

    def validate(self):
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
            try:
                self.model.generate_test_words(**fields)
            except ModelException:
                QMessageBox.warning(self, u'Błąd', u'Błąd: brak słów w słowniku spełniających zadane kryteria.')
            else:
                test_type = fields['test_type']
                new_frame = TestTranslateFrame(self.model, 1, fields[u'count'], [], test_type, self.main_window)
                self.main_window.show_frame(new_frame)


class TestTranslateFrame(QFrame, Ui_TestTranslateFrame, RightFrame):
    def __init__(self, model, current_count, total_count, quest_answers, test_type, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.model = model
        self.current_count = current_count
        self.total_count = total_count
        self.quest_answers = quest_answers
        self.test_type = test_type
        self.word = self.model.get_next_test_word()

        self.wordLabel.setText(self.word)
        self.progressBar.setValue(self.current_count)
        self.progressBar.setMaximum(self.total_count)
        if self.test_type == PL_PT_TEST:
            make_portuguese_line_edit(self.translationLineEdit)
        self.connect(self.nextPushButton, CLICKED_SIGNAL, self.next_word)
        self.connect(self.endPushButton, CLICKED_SIGNAL, self.end_test)

    def next_word(self):
        self.quest_answers.append((self.word, self.translationLineEdit.text().trimmed()))
        if self.current_count < self.total_count:
            new_frame = TestTranslateFrame(self.model, self.current_count + 1, self.total_count,
                                           self.quest_answers, self.test_type, self.main_window)
            self.main_window.show_frame(new_frame)
        else:
            return self.end_test()

    def end_test(self):
        def add_translations(question_answer):
            question = question_answer[0]
            translations = self.model.get_word_translations(question, self.test_type)
            return question_answer + (translations, )

        full_question_answers = [add_translations(q_a) for q_a in self.quest_answers]
        new_frame = TestResultsFrame(full_question_answers, self.main_window)
        self.main_window.show_frame(new_frame)

    def showEvent(self, e):
        self.translationLineEdit.setFocus()
        QFrame.showEvent(self, e)


class TestResultsFrame(QFrame, Ui_TestResultsFrame, RightFrame):
    COLUMN_WIDTH = 300

    def __init__(self, question_answers, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.question_answers = question_answers
        tablemodel = TestResultsModel(self.question_answers, parent)
        incorrect_count = len(tablemodel.get_incorrect_questions_answers())
        self.correct_answers_count = len(self.question_answers) - incorrect_count
        self.wrongAnswersTableView.setModel(tablemodel)
        self.set_correct_answers_label()

        for i in range(tablemodel.columnCount(None)):
            self.wrongAnswersTableView.setColumnWidth(i, self.COLUMN_WIDTH)

    def set_correct_answers_label(self):
        current_text = self.resultsLabel.text()
        all_answers_count = len(self.question_answers)
        new_text = '{}/{} {}'.format(self.correct_answers_count, all_answers_count, current_text)
        self.resultsLabel.setText(new_text)
