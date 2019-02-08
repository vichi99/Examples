from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        layout = QHBoxLayout()

        for n in range(10):
            btn = QPushButton(str(n))
            # btn.pressed.connect(lambda: self.test_function(n)) # mistake
            btn.pressed.connect(lambda n=n: self.test_function(n)) # mistake
            layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def test_function(self, a):
        print(a)

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
