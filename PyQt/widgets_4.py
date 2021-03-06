from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "five"])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentIndexChanged[str].connect(self.text_changed)
        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
