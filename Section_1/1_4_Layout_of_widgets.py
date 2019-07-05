import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *


class GUI(QMainWindow):  # inherit from QmainWindow
    def __init__(self):
        super().__init__()  # initialize super class, which creates the Window
        self.initUI()

    def initUI(self):  # set properties and add widgets
        self.setWindowTitle('POyQt5 GUI')  # refer to window as self
        self.resize(400, 300)
        self.add_menus_and_status()

        #self.positional_widget_layout()
        #self.horizontal_vertical_box_layout()
        self.layout_using_grid()

    def layout_using_grid(self):
        label_1 = QLabel('First label')
        label_2 = QLabel('Another label')
        label_span = QLabel('Label spanning columns span span span span')

        button_1 = QPushButton('Click 1')
        button_2 = QPushButton('Click 2')

        grid_layout = QGridLayout()

        grid_layout.addWidget(label_1, 0, 0)  # row=0, col=0
        grid_layout.addWidget(button_1, 0, 1)  # row=0, col=1
        grid_layout.addWidget(label_2, 1, 0)  # row=1, col=0
        grid_layout.addWidget(button_2, 1, 1)  # row=1, col=1

        grid_layout.addWidget(label_span, 2, 0, 1, 3)   #row=2, col=0, rowspan=1, colspan=3

        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft) # alighn grid at the top and left
        grid_layout.setAlignment(label_1, Qt.AlignRight)
        grid_layout.setAlignment(label_2, Qt.AlignRight)

        layout_widget = QWidget()  # create QWidget object
        layout_widget.setLayout(grid_layout)  # set layout

        self.setCentralWidget(layout_widget)  # make QWidget the central widget

    def horizontal_vertical_box_layout(self):
        label_1 = QLabel('First label')
        label_2 = QLabel('Another label')


        button_1 = QPushButton('Click 1')
        button_2 = QPushButton('Click 2')



        hbox_1 = QHBoxLayout()
        hbox_1.addStretch()
        hbox_2 = QHBoxLayout()
        hbox_2.addStretch()

        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)

        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)

        vbox = QVBoxLayout()
        vbox.addStretch()

        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        layout_widget = QWidget()       # create QWidget object
        layout_widget.setLayout(vbox)   # set layout

        self.setCentralWidget(layout_widget)    # make QWidget the central widget


    def positional_widget_layout(self):
        label_1 = QLabel('Our first label', self)  # label w/out text, window is the parent
        print(self.menuBar().size())             # default size: PyQt5.QtCore.QSize(100, 30)
        mbar_height = self.menuBar().height()
        print(mbar_height)
        label_1.move(10, mbar_height)            # position label below menubar

        label_2 = QLabel('Another label', self)  # create another labvel
        label_2.move(10, mbar_height * 2)        # alighn and position below label_1

        button_1 = QPushButton('click 1', self)
        button_2 = QPushButton('click 2', self)

        button_1.move(label_1.width(), label_1.height())
        button_2.move(label_1.width(), label_1.height() * 2)

    def add_menus_and_status(self):
        self.statusBar().showMessage('Text in statusbar')

        menubar = self.menuBar()  # create menu bar
        file_menu = menubar.addMenu('File')  # add menu to menu bar
        new_icon = QIcon('icons/new_icon.png')  # create icon
        new_action = QAction(new_icon, 'New', self)  # create an Action
        new_action.setStatusTip('New File')  # statusBar updated
        file_menu.addAction(new_action)  # add Action to menu

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
