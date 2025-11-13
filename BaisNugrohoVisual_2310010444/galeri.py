import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Galeri(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("galeri.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editJudul.clear()
        self.ui.editTgl.clear()
        self.ui.editKet.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Galeri Kosong")
            return
        self.aksi.simpanGaleri(
            self.ui.editID.text(), self.ui.editJudul.text(), self.ui.editTgl.text(), self.ui.editKet.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahGaleri(
            self.ui.editID.text(), self.ui.editJudul.text(), self.ui.editTgl.text(), self.ui.editKet.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusGaleri(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataGaleri()
        self.ui.tabelGaleri.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelGaleri.insertRow(i)
            self.ui.tabelGaleri.setItem(i, 0, QTableWidgetItem(str(row['id_galeri'])))
            self.ui.tabelGaleri.setItem(i, 1, QTableWidgetItem(str(row['judul'])))
            self.ui.tabelGaleri.setItem(i, 2, QTableWidgetItem(str(row['tanggal'])))
            self.ui.tabelGaleri.setItem(i, 3, QTableWidgetItem(str(row['berita_keterangan'])))
