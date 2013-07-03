from PyQt4 import QtCore, QtGui

from model import pl_to_br_layout

class PortugueseQLineEdit(QtGui.QLineEdit):
    def __init__(self, parent):
        QtGui.QLineEdit.__init__(self, parent)
        self.connect(self, QtCore.SIGNAL('textEdited(QString)'), self.text_pl_to_br)

    def text_pl_to_br(self, qtext):
        self.setText(QtCore.QString(pl_to_br_layout(qtext)))
