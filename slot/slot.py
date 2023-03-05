import logging
from widgets.widgetPages import WidgetPages
from widgets.widgetMenus import WidgetMenus


class Slot:
    def __init__(self):
        self.window = None

    def set_window(self, window):
        self.window = window

    def menu_switch(self, menu_name):
        # 1.切换页面。
        widgetPages = self.window.findChild(WidgetPages, 'pages')
        for i in range(0, widgetPages.stack_pages.count() - 1):
            widget = widgetPages.stack_pages.layout().itemAt(i).widget()
            if widget.objectName().split('_')[1] == menu_name.split('_')[1]:
                widget.show()
            else:
                widget.hide()
        # 2.改变菜单按键颜色。
        widgetMenus = self.window.findChild(WidgetMenus, 'page_menu')
        for i in range(widgetMenus.widgetMenusLayout.layout().count()):
            menu = widgetMenus.widgetMenusLayout.layout().itemAt(i).widget()
            if menu.objectName() == menu_name:
                menu.setStyleSheet('background-color:red')
            else:
                menu.setStyleSheet('background-color:white')

    @staticmethod
    def slot_home(msg):
        logging.debug(msg)

    @staticmethod
    def slot_settings(msg):
        logging.debug(msg)
