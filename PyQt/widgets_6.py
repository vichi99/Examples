from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(20)
        widget.setPlaceholderText("Enter text")
        # widget.setReadOnly(True)
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed:{}".format(
                        self.centralWidget().setText("BOOM")))


    def selection_changed(self):
        print("selection changed:{}".format(
                        self.centralWidget().selectedText()))

    def text_changed(self, i):
        print("Text changed: {}".format(i))

    def text_edited(self, s):
        print("Text edited: {}".format(s))

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
