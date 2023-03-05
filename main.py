import sys
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.widgetMain import WidgetMain
from slot.slot import Slot
from widgets.widgetMenus import WidgetMenus
from widgets.widgetHome import WidgetHome
from widgets.widgetSettings import WidgetSettings


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.widgetMain = WidgetMain()
        self.setCentralWidget(self.widgetMain)
        self.setWindowOpacity(0.8)
        self.resize(800, 600)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        widgetMenu = self.findChild(WidgetMenus, 'page_menu')
        widgetHome = self.findChild(WidgetHome, 'page_home')
        widgetSettings = self.findChild(WidgetSettings, 'page_settings')
        modifiers = a0.modifiers()
        if modifiers == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier):
            if widgetMenu.isHidden():
                logging.debug('显示菜单')
                widgetMenu.show()
            else:
                logging.debug('隐藏菜单')
                widgetMenu.hide()
        elif modifiers == QtCore.Qt.ControlModifier and a0.key() == QtCore.Qt.Key_H:
            logging.debug('切换到主页')
            widgetMenu.hide()
            widgetHome.show()
            widgetSettings.hide()
        elif modifiers == QtCore.Qt.ControlModifier and a0.key() == QtCore.Qt.Key_S:
            logging.debug('切换到设置')
            widgetMenu.hide()
            widgetHome.hide()
            widgetSettings.show()
        elif modifiers == QtCore.Qt.ControlModifier and a0.key() == QtCore.Qt.Key_Right:
            opccity = self.windowOpacity()
            self.setWindowOpacity(min(opccity + 0.1, 1))
        elif modifiers == QtCore.Qt.ControlModifier and a0.key() == QtCore.Qt.Key_Left:
            opccity = self.windowOpacity()
            self.setWindowOpacity(max(opccity - 0.1, 0.2))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        reply = QtWidgets.QMessageBox.question(self, '退出', '是否退出？',
                                               QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()

    def set_slot(self, slot):
        self.widgetMain.set_slot(slot)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    slot = Slot()
    slot.set_window(window)
    window.set_slot(slot)
    window.show()
    sys.exit(app.exec_())
