import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.widgetCommon import WidgetPushButton


class WidgetMenusLayout(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(WidgetMenusLayout, self).__init__(parent)
        self.menu_home = WidgetPushButton()
        self.menu_settings = WidgetPushButton()
        self.menu_home.setObjectName('menu_home')
        self.menu_settings.setObjectName('menu_settings')
        self.menu_home.setStyleSheet('background-color:red')
        self.menu_settings.setStyleSheet('background-color:white')
        self.menu_home.setText('主页')
        self.menu_settings.setText('设置')
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 0, 0, 0)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.menu_home)
        layout.addWidget(self.menu_settings)
        self.setLayout(layout)

    def set_slot(self, slot):
        self.menu_home.clicked.connect(lambda: slot.menu_switch(self.menu_home.objectName()))
        self.menu_settings.clicked.connect(lambda: slot.menu_switch(self.menu_settings.objectName()))


class WidgetMenus(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetMenus, self).__init__(parent)
        self.widgetMenusLayout = WidgetMenusLayout()
        self.widgetMenusLayout.setFixedWidth(50)
        empty = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.widgetMenusLayout)
        layout.addWidget(empty)
        self.setLayout(layout)
        self.setStyleSheet('background-color:rgba(0,0,0,200)')

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        # 让页面出现点击阴影效果。
        a0.ignore()

    def set_slot(self, slot):
        self.widgetMenusLayout.set_slot(slot)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetMenus()
    window.show()
    sys.exit(app.exec_())
