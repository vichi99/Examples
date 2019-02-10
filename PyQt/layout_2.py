from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("blue"), 1, 0)
        layout.addWidget(Color("sky blue"), 0, 2)
        layout.addWidget(Color("green"), 2, 1)

        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
