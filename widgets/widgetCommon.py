import logging
from PyQt5 import QtCore, QtGui, QtWidgets


class WidgetPushButton(QtWidgets.QPushButton):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(WidgetPushButton, self).__init__(parent)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.clicked.emit()


class WidgetLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(WidgetLineEdit, self).__init__(parent)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        logging.debug('正在输入...')
        a0.accept()
