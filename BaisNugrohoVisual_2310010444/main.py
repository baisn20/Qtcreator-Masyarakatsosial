# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from proker import Proker
from renbang import Renbang
from bansos import Bansos
from galeri import Galeri

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load(QFile("main.ui"), self)

        self.ui.actionProker.triggered.connect(self.buka_proker)
        self.ui.actionRenbang.triggered.connect(self.buka_renbang)
        self.ui.actionBansos.triggered.connect(self.buka_bansos)
        self.ui.actionGaleri.triggered.connect(self.buka_galeri)

    def buka_proker(self):
        self.window_proker = Proker()
        self.window_proker.show()

    def buka_renbang(self):
        self.window_renbang = Renbang()
        self.window_renbang.show()

    def buka_bansos(self):
        self.window_bansos = Bansos()
        self.window_bansos.show()

    def buka_galeri(self):
        self.window_galeri = Galeri()
        self.window_galeri.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec())
