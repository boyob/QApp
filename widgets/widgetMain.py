import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.widgetLog import WidgetLog
from widgets.widgetPages import WidgetPages


class WidgetMain(QtWidgets.QSplitter):
    def __init__(self, parent=None):
        super(WidgetMain, self).__init__(parent)
        self.ratio = [50, 300, 100, 20]
        # 创建页面。
        empty = QtWidgets.QWidget()
        self.pages = WidgetPages()
        self.log = WidgetLog()
        self.copyright = QtWidgets.QLabel()
        self.copyright.setFixedHeight(20)
        self.copyright.setText('HelloWord 2023 @ All Rights Reserved.')
        self.copyright.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignBottom)
        self.addWidget(empty)
        self.addWidget(self.pages)
        self.addWidget(self.log)
        self.addWidget(self.copyright)
        # 设置。
        for i in range(self.count()):
            self.widget(i).setMinimumHeight(self.ratio[i])
        self.setStyleSheet('background-color:#333333')
        self.setHandleWidth(0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setChildrenCollapsible(False)
        self.setOrientation(QtCore.Qt.Orientation.Vertical)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setSizes(self.ratio)

    def set_slot(self, slot):
        self.pages.set_slot(slot)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetMain()
    window.show()
    sys.exit(app.exec_())
