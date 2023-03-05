import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class WidgetBase(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetBase, self).__init__(parent)
        self.width_shadow = 2  # 阴影宽度。
        self.is_down = False  # 是否被按下。
        # 1.顶部标题。
        self.label = QtWidgets.QLabel()
        self.label.setContentsMargins(5, 0, 0, 0)
        self.label.setStyleSheet("QLabel{background-color:#333333;color:white;font-size:15px;font-weight:normal}")
        self.label.setFixedHeight(25)
        # 2.总体布局。
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(self.width_shadow, self.width_shadow,
                                       self.width_shadow, self.width_shadow)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setMouseTracking(True)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.is_down = True
        self.repaint()
        ev.ignore()

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.is_down = False
        self.repaint()
        ev.ignore()

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        a0.ignore()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter()
        painter.begin(self)
        pen_1 = QtGui.QPen(QtGui.QColor(0, 0, 0), self.width_shadow)
        pen_2 = QtGui.QPen(QtGui.QColor(110, 110, 110), self.width_shadow)
        if self.is_down:
            painter.setPen(pen_1)
            painter.drawLine(0, 0, 0, self.height())  # 左。
            painter.drawLine(0, 0, self.width(), 0)  # 上。
            painter.setPen(pen_2)
            painter.drawLine(self.width() - 1, 0, self.width() - 1, self.height())  # 右
            painter.drawLine(0, self.height() - 1, self.width(), self.height() - 1)  # 下。
        else:
            painter.setPen(pen_2)
            painter.drawLine(0, 0, 0, self.height())
            painter.drawLine(0, 0, self.width(), 0)
            painter.setPen(pen_1)
            painter.drawLine(self.width() - 1, 0, self.width() - 1, self.height())
            painter.drawLine(0, self.height() - 1, self.width(), self.height() - 1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetBase()
    window.show()
    sys.exit(app.exec_())
