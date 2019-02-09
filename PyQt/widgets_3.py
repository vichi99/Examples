from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        widget = QCheckBox()
        # widget.setChecked(True)
        # widget.setCheckState(Qt.Checked)
        widget.setCheckState(Qt.PartiallyChecked)

        widget.setTristate(True)

        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print ("{}: {}".format(s == Qt.Checked, s))


app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
