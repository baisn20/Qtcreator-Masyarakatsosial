import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Proker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("proker.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editNama.clear()
        self.ui.editWaktu.clear()
        self.ui.editAnggaran.clear()
        self.ui.editKet.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Proker Kosong")
            return
        self.aksi.simpanProker(
            self.ui.editID.text(), self.ui.editNama.text(), self.ui.editWaktu.text(),
            self.ui.editAnggaran.text(), self.ui.editKet.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahProker(
            self.ui.editID.text(), self.ui.editNama.text(), self.ui.editWaktu.text(),
            self.ui.editAnggaran.text(), self.ui.editKet.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusProker(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataProker()
        self.ui.tabelProker.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelProker.insertRow(i)
            self.ui.tabelProker.setItem(i, 0, QTableWidgetItem(str(row['id_proker'])))
            self.ui.tabelProker.setItem(i, 1, QTableWidgetItem(str(row['nama_proker'])))
            self.ui.tabelProker.setItem(i, 2, QTableWidgetItem(str(row['waktu_laksana'])))
            self.ui.tabelProker.setItem(i, 3, QTableWidgetItem(str(row['anggaran'])))
            self.ui.tabelProker.setItem(i, 4, QTableWidgetItem(str(row['keterangan'])))
