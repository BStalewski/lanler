#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore

CLICKED_SIGNAL = QtCore.SIGNAL('clicked()')


class NotImplementedException(Exception):
    pass


class RightFrame():
    def __init__(self, main_window):
        self.main_window = main_window
