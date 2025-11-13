# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'renbang.ui'
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

class Ui_FormRenbang(object):
    def setupUi(self, FormRenbang):
        if not FormRenbang.objectName():
            FormRenbang.setObjectName(u"FormRenbang")
        FormRenbang.resize(700, 550)
        self.formLayoutWidget = QWidget(FormRenbang)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 210))
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

        self.editKegiatan = QLineEdit(self.formLayoutWidget)
        self.editKegiatan.setObjectName(u"editKegiatan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editKegiatan)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editLokasi = QLineEdit(self.formLayoutWidget)
        self.editLokasi.setObjectName(u"editLokasi")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editLokasi)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editVolume = QLineEdit(self.formLayoutWidget)
        self.editVolume.setObjectName(u"editVolume")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editVolume)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editSumber = QLineEdit(self.formLayoutWidget)
        self.editSumber.setObjectName(u"editSumber")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editSumber)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.editKet = QLineEdit(self.formLayoutWidget)
        self.editKet.setObjectName(u"editKet")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editKet)

        self.l7 = QLabel(self.formLayoutWidget)
        self.l7.setObjectName(u"l7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.l7)

        self.editStatus = QLineEdit(self.formLayoutWidget)
        self.editStatus.setObjectName(u"editStatus")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editStatus)

        self.btnSimpan = QPushButton(FormRenbang)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 250, 90, 29))
        self.btnHapus = QPushButton(FormRenbang)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 250, 90, 29))
        self.btnUbah = QPushButton(FormRenbang)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 250, 90, 29))
        self.btnBersih = QPushButton(FormRenbang)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 250, 90, 29))
        self.tabelRenbang = QTableWidget(FormRenbang)
        if (self.tabelRenbang.columnCount() < 6):
            self.tabelRenbang.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelRenbang.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelRenbang.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelRenbang.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelRenbang.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelRenbang.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabelRenbang.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabelRenbang.setObjectName(u"tabelRenbang")
        self.tabelRenbang.setGeometry(QRect(50, 300, 600, 230))

        self.retranslateUi(FormRenbang)

        QMetaObject.connectSlotsByName(FormRenbang)
    # setupUi

    def retranslateUi(self, FormRenbang):
        FormRenbang.setWindowTitle(QCoreApplication.translate("FormRenbang", u"Data Rencana Pembangunan", None))
        self.l1.setText(QCoreApplication.translate("FormRenbang", u"ID Renbang", None))
        self.l2.setText(QCoreApplication.translate("FormRenbang", u"Kegiatan", None))
        self.l3.setText(QCoreApplication.translate("FormRenbang", u"Lokasi", None))
        self.l4.setText(QCoreApplication.translate("FormRenbang", u"Volume", None))
        self.l5.setText(QCoreApplication.translate("FormRenbang", u"Sumber Dana", None))
        self.l6.setText(QCoreApplication.translate("FormRenbang", u"Keterangan", None))
        self.l7.setText(QCoreApplication.translate("FormRenbang", u"Status", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormRenbang", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormRenbang", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormRenbang", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormRenbang", u"Bersih", None))
        ___qtablewidgetitem = self.tabelRenbang.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormRenbang", u"ID", None));
        ___qtablewidgetitem1 = self.tabelRenbang.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormRenbang", u"Kegiatan", None));
        ___qtablewidgetitem2 = self.tabelRenbang.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormRenbang", u"Lokasi", None));
        ___qtablewidgetitem3 = self.tabelRenbang.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormRenbang", u"Volume", None));
        ___qtablewidgetitem4 = self.tabelRenbang.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormRenbang", u"Sumber", None));
        ___qtablewidgetitem5 = self.tabelRenbang.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormRenbang", u"Status", None));
    # retranslateUi

