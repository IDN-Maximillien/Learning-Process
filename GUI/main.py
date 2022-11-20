from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(960, 540, 200, 200)
    win.setWindowTitle('Main Window!')
    
    label = QtWidgets.QLabel(win)
    label.setText('Label 1')
    label.move(100, 100)
    
    win.show()
    sys.exit(app.exec_())

window()