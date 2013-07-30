#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QFrame

from commons import CLICKED_SIGNAL, NotImplementedException, RightFrame
from model.main_model import PtPlDictionaryModel, PlPtDictionaryModel
from py_ui.choose_dictionary_ui import Ui_ChooseDictionaryFrame
from py_ui.pt_pl_dictionary_ui import Ui_PtPlDictionaryFrame, _translate


class ChooseDictionaryFrame(QFrame, Ui_ChooseDictionaryFrame, RightFrame):
    def __init__(self, model, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.plPtDictionaryButton, CLICKED_SIGNAL, self.pl_pt_dictionary)
        self.connect(self.ptPlDictionaryButton, CLICKED_SIGNAL, self.pt_pl_dictionary)
        self.model = model

    def pl_pt_dictionary(self):
        self.main_window.show_frame(PlPtDictionaryFrame(self.model, self.parent()))

    def pt_pl_dictionary(self):
        self.main_window.show_frame(PtPlDictionaryFrame(self.model, self.parent()))


class PtPlDictionaryFrame(QFrame, Ui_PtPlDictionaryFrame, RightFrame):
    COLUMN_WIDTH = 300

    def __init__(self, model, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.backButton, CLICKED_SIGNAL, self.back)

        self.model = model

        tablemodel = PtPlDictionaryModel(self.model.get_current_user(), self)
        self.dictionaryTableView.setModel(tablemodel)

        for i in range(tablemodel.columnCount(None)):
            self.dictionaryTableView.setColumnWidth(i, self.COLUMN_WIDTH)

    def resize(self, *args):
        try:
            self.dictionaryTableView.setVisible(False)
            self.dictionaryTableView.resizeColumnsToContents()
            self.dictionaryTableView.setVisible(True)
        except AttributeError:
            pass

        QFrame.resize(self, *args)

    def back(self):
        raise NotImplementedException('back')


class PlPtDictionaryFrame(PtPlDictionaryFrame):
    def __init__(self, model, parent):
        PtPlDictionaryFrame.__init__(self, model, parent)

        tablemodel = PlPtDictionaryModel(self.model.get_current_user(), self)
        self.dictionaryTableView.setModel(tablemodel)

    def retranslateUi(self, frame):
        Ui_PtPlDictionaryFrame.retranslateUi(self, frame)
        frame.setWindowTitle(_translate("PlPtDictionaryFrame", "Frame", None))
        self.label.setText(_translate("PlPtDictionaryFrame", "Słownik polsko - portugalski", None))

    def back(self):
        raise NotImplementedException('back')
