#Structure of qt5 GUIs

# Imports
import sys
from PyQt5.QtWidgets import *

# create Application
app = QApplication(sys.argv)
win = QWidget()

# Create Window
win.setWindowTitle('PyQt5 GUI')
win.resize(400, 300)

# show the constructed Qt window
win.show()

# execute the application
sys.exit(app.exec_())
