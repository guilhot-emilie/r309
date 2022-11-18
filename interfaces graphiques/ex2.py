
from PyQt5.QtWidgets import *
import sys
from ex22 import Aide

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        lab = QLabel("Température : ")
        text = QLineEdit("")
        convertir = QPushButton("Convertir")
        unite = QComboBox()
        lab2 = QLabel("Conversion : ")
        result = QLabel("")
        aide = QPushButton("?")

        # Constructeur
        self.__lab = lab
        self.__text = text
        self.__convertir = convertir
        self.__unite = unite
        self.__lab2 = lab2
        self.__result = result
        self.__aide = aide

        # ComboBox
        unite.addItem("C -> K")
        unite.addItem("K -> C")

        # Affichage
        grid.addWidget(self.__lab, 0, 0)
        grid.addWidget(self.__text, 0, 1)
        grid.addWidget(self.__convertir, 1, 0)
        grid.addWidget(self.__unite, 1, 1)
        grid.addWidget(self.__lab2, 2, 0)
        grid.addWidget(self.__result, 2, 1)
        grid.addWidget(self.__aide, 2, 2)

        convertir.clicked.connect(self._actionOk)
        aide.clicked.connect(self._actionAide)
        self.setWindowTitle("One")

    def _actionOk(self):
        if self.__unite.currentText() == "C -> K":
            try:
                self.__result.setText(f"{float(self.__text.text()) + 273.15} K")
            except ValueError:
                self.__result.setText(f"Valeur incorrecte")
        else:
            try :
                self.__result.setText(f"{float(self.__text.text()) - 273.15} C")
            except ValueError:
                self.__result.setText(f"Valeur incorrecte")

    def _actionAide(self):
        self.__aide = Aide()
        self.__aide.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
