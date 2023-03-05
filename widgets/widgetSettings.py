import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.widgetBase import WidgetBase


class WidgetSettingsPage(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(WidgetSettingsPage, self).__init__(parent)
        self.dial = QtWidgets.QDial()
        self.dial.setRange(0, 100)
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.dial)
        self.setLayout(layout)
        self.setStyleSheet('background-color:#999999')

    def set_slot(self, slot):
        self.dial.valueChanged.connect(lambda: slot.slot_settings(self.dial.value()))


class WidgetSettings(WidgetBase):
    def __init__(self, parent=None):
        super(WidgetSettings, self).__init__(parent)
        self.label.setText('设置')
        self.widgetSettingsPage = WidgetSettingsPage()
        self.layout.addWidget(self.widgetSettingsPage)

    def set_slot(self, slot):
        self.widgetSettingsPage.set_slot(slot)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetSettings()
    window.show()
    sys.exit(app.exec_())
