import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.widgetMenus import WidgetMenus
from widgets.widgetHome import WidgetHome
from widgets.widgetSettings import WidgetSettings


class WidgetPages(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(WidgetPages, self).__init__(parent)
        self.setObjectName('pages')
        self.page_menu = WidgetMenus()
        self.page_menu.setObjectName('page_menu')
        self.page_home = WidgetHome()
        self.page_home.setObjectName('page_home')
        self.page_settings = WidgetSettings()
        self.page_settings.setObjectName('page_settings')
        self.stack_pages = QtWidgets.QStackedLayout()
        self.stack_pages.setStackingMode(QtWidgets.QStackedLayout.StackingMode.StackAll)
        self.stack_pages.insertWidget(0, self.page_menu)
        self.stack_pages.insertWidget(0, self.page_home)
        self.stack_pages.insertWidget(0, self.page_settings)
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(5)
        layout.setContentsMargins(10, 15, 10, 15)
        layout.addLayout(self.stack_pages)
        self.setLayout(layout)
        self.setStyleSheet('background-color:#5a5a5a')
        self.page_menu.hide()
        self.page_settings.hide()

    def set_slot(self, slot):
        self.page_menu.set_slot(slot)
        self.page_home.set_slot(slot)
        self.page_settings.set_slot(slot)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetPages()
    window.show()
    sys.exit(app.exec_())
