from PyQt5 import QtWidgets, uic
import sys
from browse import browseInFolder

app = QtWidgets.QApplication(sys.argv)

from main import deleteCache, writeAutoExec

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ressources/mainwindow.ui', self) # Load the ui file
        self.show() # Show the GUI

        self.pushButton_2.clicked.connect(browseInFolder)
        self.pushButton.clicked.connect(deleteCache)
        self.pushButton_3.clicked.connect(writeAutoExec)

window = Ui()
app.exec_()