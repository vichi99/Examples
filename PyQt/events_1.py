from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.windowTitleChanged.connect(self.onWindowTitleChange)

        self.setWindowTitle("My App")

        label = QLabel("Nice")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    def contextMenuEvent(self, e):
        print("context menu requested") # right click
        super(MainWindow, self).contextMenuEvent(e)

    def onWindowTitleChange(self, s):
        print(s)


app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()

# # if we want recognize event on button or place around button
# class CustomButton(Qbutton)
#
#     def event(self, e):
#         # e.accept()
#         e.ignore()
