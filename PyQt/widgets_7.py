from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        # widget = QSpinBox()
        widget = QDoubleSpinBox()
        # widget.setMinimum(-6)
        # widget.setMaximum(6)
        widget.setRange(-2,15)
        widget.setPrefix("$")
        widget.setSuffix("c")
        # widget.setSingleStep(3)
        widget.setSingleStep(0.33)
        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_str)
        self.setCentralWidget(widget)

    def value_changed(self,i):
        print("value: {}".format(i))

    def value_changed_str(self,i):
        print("value_str: {}".format(i))


app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
