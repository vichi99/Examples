from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    my_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        button = QPushButton("Hello")
        button.pressed.connect(self.my_button)

        self.my_signal.connect(self.caught_my_signal)
        self.setCentralWidget(button)

    def my_button(self):
        print("button pushed")
        self.my_signal.emit("signal catched")

    def caught_my_signal(self,s):
        print(s)

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
