#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QFrame

from commons import CLICKED_SIGNAL, NotImplementedException, RightFrame
from py_ui.options_ui import Ui_OptionsFrame


class OptionsFrame(QFrame, Ui_OptionsFrame, RightFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.changeUserButton, CLICKED_SIGNAL, self.change_user)
        self.connect(self.removeUserButton, CLICKED_SIGNAL, self.remove_user)

    def change_user(self):
        print 'change user'
        raise NotImplementedException('change user')

    def remove_user(self):
        print 'remove user'
        raise NotImplementedException('remove user')
