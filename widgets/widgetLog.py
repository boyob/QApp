import os
import sys
import glob
import time
import logging
from PyQt5 import QtCore, QtGui, QtWidgets


class WidgetPlainTextEdit(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        super(WidgetPlainTextEdit, self).__init__(parent)
        self.action_debug = QtWidgets.QAction('调试')
        self.action_debug.setCheckable(True)
        self.action_debug.setChecked(False)
        self.action_clear = QtWidgets.QAction('清空')
        self.action_clear.triggered.connect(self.clear)
        self.contexMenu = QtWidgets.QMenu(self)
        self.contexMenu.addAction(self.action_debug)
        self.contexMenu.addAction(self.action_clear)

    def contextMenuEvent(self, e: QtGui.QContextMenuEvent) -> None:
        self.contexMenu.exec_(e.globalPos())

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.buttons() == QtCore.Qt.LeftButton:
            logging.debug('debug')
            logging.info('info')
            logging.warning('warning')
            logging.error('error')
            logging.critical('critical')


class WidgetHandler(logging.Handler):
    def __init__(self):
        super(WidgetHandler, self).__init__()
        self.widget = WidgetPlainTextEdit()
        self.widget.setReadOnly(True)
        self.widget.action_debug.triggered.connect(self.debug)
        notset = QtGui.QTextCharFormat()
        notset.setForeground(QtGui.QColor(QtCore.Qt.gray))
        debug = QtGui.QTextCharFormat()
        debug.setForeground(QtGui.QColor(QtCore.Qt.white))
        info = QtGui.QTextCharFormat()
        info.setForeground(QtGui.QColor(QtCore.Qt.green))
        warning = QtGui.QTextCharFormat()
        warning.setForeground(QtGui.QColor(QtCore.Qt.yellow))
        error = QtGui.QTextCharFormat()
        error.setForeground(QtGui.QColor(QtCore.Qt.red))
        critical = QtGui.QTextCharFormat()
        critical.setForeground(QtGui.QColor('#990000'))
        self.fmt = [notset, debug, info, warning, error, critical]

    def debug(self):
        if self.widget.action_debug.isChecked():
            self.setLevel(logging.DEBUG)
        else:
            self.setLevel(logging.INFO)

    def emit(self, record):
        level = record.levelno
        self.widget.mergeCurrentCharFormat(self.fmt[level // 10])
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class WidgetLog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetLog, self).__init__(parent)
        self.init()
        # 变量。
        date_fmt = '%Y/%m/%d %H:%M:%S'
        widg_fmt = '%(asctime)s %(levelname)-5.5s: %(message)s'
        file_fmt = '%(name)s %(pathname)s, line %(lineno)d, %(asctime)s %(levelname)s: %(message)s'
        path_log = os.path.join(os.getcwd(), time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.log')
        # logging.basicConfig(level=logging.NOTSET)
        logging.getLogger().setLevel(level=logging.NOTSET)
        # 1.部件日志。
        widgetHandler = WidgetHandler()
        widgetHandler.setLevel(level=logging.INFO)
        widgetHandler.setFormatter(logging.Formatter(fmt=widg_fmt, datefmt=date_fmt))
        logging.getLogger().addHandler(widgetHandler)
        # 2.终端日志。
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logging.Formatter(fmt=widg_fmt, datefmt=date_fmt))
        logging.getLogger().addHandler(consoleHandler)
        # 3.文件日志。
        fileHandler = logging.FileHandler(filename=path_log, mode='a', encoding='utf-8')
        fileHandler.setFormatter(logging.Formatter(fmt=file_fmt, datefmt=date_fmt))
        logging.getLogger().addHandler(fileHandler)
        # 4.布局。
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 0)
        layout.addWidget(widgetHandler.widget)
        self.setLayout(layout)

    @staticmethod
    def init():
        logs = glob.glob('*.log')
        for log in logs:
            os.remove(log)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetLog()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
