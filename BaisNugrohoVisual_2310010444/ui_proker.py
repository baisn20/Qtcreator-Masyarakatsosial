# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proker.ui'
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

class Ui_FormProker(object):
    def setupUi(self, FormProker):
        if not FormProker.objectName():
            FormProker.setObjectName(u"FormProker")
        FormProker.resize(600, 500)
        self.formLayoutWidget = QWidget(FormProker)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 150))
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

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editWaktu = QLineEdit(self.formLayoutWidget)
        self.editWaktu.setObjectName(u"editWaktu")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editWaktu)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editAnggaran = QLineEdit(self.formLayoutWidget)
        self.editAnggaran.setObjectName(u"editAnggaran")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editAnggaran)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editKet = QLineEdit(self.formLayoutWidget)
        self.editKet.setObjectName(u"editKet")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editKet)

        self.btnSimpan = QPushButton(FormProker)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 190, 90, 29))
        self.btnHapus = QPushButton(FormProker)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 190, 90, 29))
        self.btnUbah = QPushButton(FormProker)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 190, 90, 29))
        self.btnBersih = QPushButton(FormProker)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 190, 90, 29))
        self.tabelProker = QTableWidget(FormProker)
        if (self.tabelProker.columnCount() < 5):
            self.tabelProker.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelProker.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelProker.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelProker.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelProker.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelProker.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelProker.setObjectName(u"tabelProker")
        self.tabelProker.setGeometry(QRect(50, 240, 500, 240))

        self.retranslateUi(FormProker)

        QMetaObject.connectSlotsByName(FormProker)
    # setupUi

    def retranslateUi(self, FormProker):
        FormProker.setWindowTitle(QCoreApplication.translate("FormProker", u"Data Program Kerja", None))
        self.l1.setText(QCoreApplication.translate("FormProker", u"ID Proker", None))
        self.l2.setText(QCoreApplication.translate("FormProker", u"Nama Proker", None))
        self.l3.setText(QCoreApplication.translate("FormProker", u"Waktu Laksana", None))
        self.l4.setText(QCoreApplication.translate("FormProker", u"Anggaran", None))
        self.l5.setText(QCoreApplication.translate("FormProker", u"Keterangan", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormProker", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormProker", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormProker", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormProker", u"Bersih", None))
        ___qtablewidgetitem = self.tabelProker.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormProker", u"ID", None));
        ___qtablewidgetitem1 = self.tabelProker.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormProker", u"Nama Proker", None));
        ___qtablewidgetitem2 = self.tabelProker.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormProker", u"Waktu", None));
        ___qtablewidgetitem3 = self.tabelProker.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormProker", u"Anggaran", None));
        ___qtablewidgetitem4 = self.tabelProker.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormProker", u"Ket", None));
    # retranslateUi

