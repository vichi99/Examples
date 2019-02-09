from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        # widget = QSlider()
        widget = QDial()
        widget.setRange(-2,15)
        # widget.setSingleStep(3)
        widget.setSingleStep(0.33)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        self.setCentralWidget(widget)

    def value_changed(self,i):
        print("value: {}".format(i))

    def slider_position(self,j):
        print("slider position: {}".format(j))

    def slider_pressed(self):
        print("pressed")

    def slider_released(self):
        print("released")



app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
