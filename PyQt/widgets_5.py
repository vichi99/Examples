from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "five"])
        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged[str].connect(self.text_changed)
        self.setCentralWidget(widget)

    def item_changed(self, i):
        print(i)
        # print(i.text())

    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
