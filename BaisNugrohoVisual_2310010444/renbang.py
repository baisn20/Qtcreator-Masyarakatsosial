import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Renbang(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("renbang.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editKegiatan.clear()
        self.ui.editLokasi.clear()
        self.ui.editVolume.clear()
        self.ui.editSumber.clear()
        self.ui.editKet.clear()
        self.ui.editStatus.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Renbang Kosong")
            return
        self.aksi.simpanRenbang(
            self.ui.editID.text(), self.ui.editKegiatan.text(), self.ui.editLokasi.text(),
            self.ui.editVolume.text(), self.ui.editSumber.text(), self.ui.editKet.text(), self.ui.editStatus.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahRenbang(
            self.ui.editID.text(), self.ui.editKegiatan.text(), self.ui.editLokasi.text(),
            self.ui.editVolume.text(), self.ui.editSumber.text(), self.ui.editKet.text(), self.ui.editStatus.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusRenbang(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataRenbang()
        self.ui.tabelRenbang.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelRenbang.insertRow(i)
            self.ui.tabelRenbang.setItem(i, 0, QTableWidgetItem(str(row['id_renbang'])))
            self.ui.tabelRenbang.setItem(i, 1, QTableWidgetItem(str(row['kegiatan'])))
            self.ui.tabelRenbang.setItem(i, 2, QTableWidgetItem(str(row['lokasi'])))
            self.ui.tabelRenbang.setItem(i, 3, QTableWidgetItem(str(row['volume'])))
            self.ui.tabelRenbang.setItem(i, 4, QTableWidgetItem(str(row['dana_sumber'])))
            self.ui.tabelRenbang.setItem(i, 5, QTableWidgetItem(str(row['status'])))
