import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Bansos(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("bansos.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editUraian.clear()
        self.ui.editJml.clear()
        self.ui.editTahun.clear()
        self.ui.editSalur.clear()
        self.ui.editKategori.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Bansos Kosong")
            return
        self.aksi.simpanBansos(
            self.ui.editID.text(), self.ui.editUraian.text(), self.ui.editJml.text(),
            self.ui.editTahun.text(), self.ui.editSalur.text(), self.ui.editKategori.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahBansos(
            self.ui.editID.text(), self.ui.editUraian.text(), self.ui.editJml.text(),
            self.ui.editTahun.text(), self.ui.editSalur.text(), self.ui.editKategori.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusBansos(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataBansos()
        self.ui.tabelBansos.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelBansos.insertRow(i)
            self.ui.tabelBansos.setItem(i, 0, QTableWidgetItem(str(row['id_bansos'])))
            self.ui.tabelBansos.setItem(i, 1, QTableWidgetItem(str(row['uraian'])))
            self.ui.tabelBansos.setItem(i, 2, QTableWidgetItem(str(row['jml_bantuan'])))
            self.ui.tabelBansos.setItem(i, 3, QTableWidgetItem(str(row['tahun'])))
            self.ui.tabelBansos.setItem(i, 4, QTableWidgetItem(str(row['disalurkan'])))
            self.ui.tabelBansos.setItem(i, 5, QTableWidgetItem(str(row['kategori'])))
