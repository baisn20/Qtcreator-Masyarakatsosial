# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bansos.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_FormBansos(object):
    def setupUi(self, FormBansos):
        if not FormBansos.objectName():
            FormBansos.setObjectName(u"FormBansos")
        FormBansos.resize(650, 500)
        self.formLayoutWidget = QWidget(FormBansos)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 180))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.l1 = QLabel(self.formLayoutWidget)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.l2 = QLabel(self.formLayoutWidget)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.editUraian = QLineEdit(self.formLayoutWidget)
        self.editUraian.setObjectName(u"editUraian")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editUraian)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editJml = QLineEdit(self.formLayoutWidget)
        self.editJml.setObjectName(u"editJml")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editJml)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editTahun = QLineEdit(self.formLayoutWidget)
        self.editTahun.setObjectName(u"editTahun")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTahun)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editSalur = QLineEdit(self.formLayoutWidget)
        self.editSalur.setObjectName(u"editSalur")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editSalur)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.editKategori = QLineEdit(self.formLayoutWidget)
        self.editKategori.setObjectName(u"editKategori")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editKategori)

        self.btnSimpan = QPushButton(FormBansos)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 220, 90, 29))
        self.btnHapus = QPushButton(FormBansos)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 220, 90, 29))
        self.btnUbah = QPushButton(FormBansos)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 220, 90, 29))
        self.btnBersih = QPushButton(FormBansos)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 220, 90, 29))
        self.tabelBansos = QTableWidget(FormBansos)
        if (self.tabelBansos.columnCount() < 6):
            self.tabelBansos.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelBansos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelBansos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelBansos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelBansos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelBansos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabelBansos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabelBansos.setObjectName(u"tabelBansos")
        self.tabelBansos.setGeometry(QRect(50, 270, 550, 200))

        self.retranslateUi(FormBansos)

        QMetaObject.connectSlotsByName(FormBansos)
    # setupUi

    def retranslateUi(self, FormBansos):
        FormBansos.setWindowTitle(QCoreApplication.translate("FormBansos", u"Data Bansos", None))
        self.l1.setText(QCoreApplication.translate("FormBansos", u"ID Bansos", None))
        self.l2.setText(QCoreApplication.translate("FormBansos", u"Uraian", None))
        self.l3.setText(QCoreApplication.translate("FormBansos", u"Jumlah Bantuan", None))
        self.l4.setText(QCoreApplication.translate("FormBansos", u"Tahun", None))
        self.l5.setText(QCoreApplication.translate("FormBansos", u"Disalurkan Ke", None))
        self.l6.setText(QCoreApplication.translate("FormBansos", u"Kategori", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormBansos", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormBansos", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormBansos", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormBansos", u"Bersih", None))
        ___qtablewidgetitem = self.tabelBansos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormBansos", u"ID", None));
        ___qtablewidgetitem1 = self.tabelBansos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormBansos", u"Uraian", None));
        ___qtablewidgetitem2 = self.tabelBansos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormBansos", u"Jumlah", None));
        ___qtablewidgetitem3 = self.tabelBansos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormBansos", u"Tahun", None));
        ___qtablewidgetitem4 = self.tabelBansos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormBansos", u"Penyalur", None));
        ___qtablewidgetitem5 = self.tabelBansos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormBansos", u"Kategori", None));
    # retranslateUi

