# class inheriting from QMainWindow
# add menu bar

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

from PyQt5.QtGui import QIcon


class GUI(QMainWindow):  # inherit from QmainWindow
    def __init__(self):
        super().__init__()  # initialize super class, which creates the Window

        self.initUI()

    def initUI(self):  # set properties and add widgets
        self.setWindowTitle('POyQt5 GUI')  # refer to window as self
        self.resize(400, 300)  # resize window (width, height)

        self.add_menus_and_status()


    def add_menus_and_status(self):
        self.statusBar().showMessage('Text in statusbar')

        menubar = self.menuBar()  # create menu bar

        file_menu = menubar.addMenu('File')  # add menu to menu bar
        new_icon = QIcon('icons/new_icon.png')  # create icon
        new_action = QAction(new_icon, 'New', self)  # create an Action

        file_menu.addAction(new_action)  # add Action to menu
        new_action.setStatusTip('New File')  # statusBar updated

        file_menu.addSeparator()  # add separator line between menu items

        exit_icon = QIcon('icons/exit_icon.png')  # create icon
        exit_action = QAction(exit_icon, 'Click', self)  # create an action for the exit tab
        exit_action.setStatusTip('Click to exit the application')
        exit_action.triggered.connect(self.close)  # close application when clicked
        exit_action.setShortcut('Ctrl+Q')  # keyboard shortcut to close application
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu('Edit')




if __name__ == '__main__':
    app = QApplication(sys.argv)  # create Application
    gui = GUI()  # create instance of class
    gui.show()  # show the constructed PyQt window
    sys.exit(app.exec_())  # execute the application
