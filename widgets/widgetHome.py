import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.widgetBase import WidgetBase
from widgets.widgetCommon import WidgetLineEdit


class WidgetHomePage(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(WidgetHomePage, self).__init__(parent)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName('home-pushButton')
        self.pushButton.setText('home-pushButton')
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem('a')
        self.comboBox.addItem('b')
        self.lineEdit = WidgetLineEdit()
        self.lineEdit.setPlaceholderText('请输入...')
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        self.setStyleSheet('background-color:#999999')

    def set_slot(self, slot):
        self.pushButton.clicked.connect(lambda: slot.slot_home(self.pushButton.objectName()))
        self.comboBox.activated.connect(lambda: slot.slot_home(self.comboBox.currentText()))
        self.lineEdit.selectionChanged.connect(lambda: slot.slot_home(self.lineEdit.text()))


class WidgetHome(WidgetBase):
    def __init__(self, parent=None):
        super(WidgetHome, self).__init__(parent)
        self.label.setText('主页')
        self.widgetHomePage = WidgetHomePage()
        self.layout.addWidget(self.widgetHomePage)

    def set_slot(self, slot):
        self.widgetHomePage.set_slot(slot)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetHome()
    window.show()
    sys.exit(app.exec_())
