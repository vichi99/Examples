from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        # widget = QLabel("Hello")
        # font = widget.font()
        # font.setPointSize(40)
        # widget.setFont(font)
        # # widget.setAlignment(Qt.AlignCenter)
        # widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        widget = QLabel()
        widget.setPixmap(QPixmap("test.jpeg"))
        widget.setAlignment(Qt.AlignCenter)
        widget.setScaledContents(True)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
