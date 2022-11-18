import sys
from PyQt5.QtWidgets import *


class Aide(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        lab = QLabel("Permet de convertir un nombre soit de Kelvin vers Celcius, soit de Celcius vers Kelvin")


        #  les composants au grid layout
        grid.addWidget(lab, 0, 0)

        self.setWindowTitle("Aide")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aide()
    window.show()
    app.exec()