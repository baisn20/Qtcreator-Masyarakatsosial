# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'galeri.ui'
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

class Ui_FormGaleri(object):
    def setupUi(self, FormGaleri):
        if not FormGaleri.objectName():
            FormGaleri.setObjectName(u"FormGaleri")
        FormGaleri.resize(500, 450)
        self.formLayoutWidget = QWidget(FormGaleri)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 400, 120))
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

        self.editJudul = QLineEdit(self.formLayoutWidget)
        self.editJudul.setObjectName(u"editJudul")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editJudul)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editTgl = QLineEdit(self.formLayoutWidget)
        self.editTgl.setObjectName(u"editTgl")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editTgl)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editKet = QLineEdit(self.formLayoutWidget)
        self.editKet.setObjectName(u"editKet")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editKet)

        self.btnSimpan = QPushButton(FormGaleri)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 160, 90, 29))
        self.btnHapus = QPushButton(FormGaleri)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 160, 90, 29))
        self.btnUbah = QPushButton(FormGaleri)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 160, 90, 29))
        self.btnBersih = QPushButton(FormGaleri)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 160, 90, 29))
        self.tabelGaleri = QTableWidget(FormGaleri)
        if (self.tabelGaleri.columnCount() < 4):
            self.tabelGaleri.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelGaleri.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelGaleri.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelGaleri.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelGaleri.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelGaleri.setObjectName(u"tabelGaleri")
        self.tabelGaleri.setGeometry(QRect(50, 210, 400, 200))

        self.retranslateUi(FormGaleri)

        QMetaObject.connectSlotsByName(FormGaleri)
    # setupUi

    def retranslateUi(self, FormGaleri):
        FormGaleri.setWindowTitle(QCoreApplication.translate("FormGaleri", u"Data Galeri", None))
        self.l1.setText(QCoreApplication.translate("FormGaleri", u"ID Galeri", None))
        self.l2.setText(QCoreApplication.translate("FormGaleri", u"Judul", None))
        self.l3.setText(QCoreApplication.translate("FormGaleri", u"Tanggal", None))
        self.l4.setText(QCoreApplication.translate("FormGaleri", u"Keterangan", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormGaleri", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormGaleri", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormGaleri", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormGaleri", u"Bersih", None))
        ___qtablewidgetitem = self.tabelGaleri.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormGaleri", u"ID", None));
        ___qtablewidgetitem1 = self.tabelGaleri.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormGaleri", u"Judul", None));
        ___qtablewidgetitem2 = self.tabelGaleri.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormGaleri", u"Tanggal", None));
        ___qtablewidgetitem3 = self.tabelGaleri.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormGaleri", u"Ket", None));
    # retranslateUi

