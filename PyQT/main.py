from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from PyQt5.Qt import PYQT_VERSION_STR
#import PyQt5
import sys
class MainWindow(QMainWindow):
    pass
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()

print ("test")
