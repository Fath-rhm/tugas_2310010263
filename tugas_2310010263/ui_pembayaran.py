# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pembayaran.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 604)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 241, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 60, 341, 511))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.iDALATLabel = QLabel(self.frame)
        self.iDALATLabel.setObjectName(u"iDALATLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDALATLabel)

        self.txtNota = QLineEdit(self.frame)
        self.txtNota.setObjectName(u"txtNota")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNota)

        self.jENISALATLabel = QLabel(self.frame)
        self.jENISALATLabel.setObjectName(u"jENISALATLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.jENISALATLabel)

        self.txtDenda = QLineEdit(self.frame)
        self.txtDenda.setObjectName(u"txtDenda")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtDenda)

        self.tIPEALATLabel = QLabel(self.frame)
        self.tIPEALATLabel.setObjectName(u"tIPEALATLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tIPEALATLabel)

        self.txtBiaya = QLineEdit(self.frame)
        self.txtBiaya.setObjectName(u"txtBiaya")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtBiaya)

        self.mERKLabel = QLabel(self.frame)
        self.mERKLabel.setObjectName(u"mERKLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.mERKLabel)

        self.txtJmlBayar = QLineEdit(self.frame)
        self.txtJmlBayar.setObjectName(u"txtJmlBayar")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtJmlBayar)

        self.wARNALabel = QLabel(self.frame)
        self.wARNALabel.setObjectName(u"wARNALabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.wARNALabel)

        self.txtKembalian = QLineEdit(self.frame)
        self.txtKembalian.setObjectName(u"txtKembalian")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.txtKembalian)

        self.dateTgl = QDateEdit(self.frame)
        self.dateTgl.setObjectName(u"dateTgl")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateTgl)

        self.tANGGALLabel = QLabel(self.frame)
        self.tANGGALLabel.setObjectName(u"tANGGALLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.tANGGALLabel)

        self.cmbPeminjaman = QComboBox(self.frame)
        self.cmbPeminjaman.setObjectName(u"cmbPeminjaman")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbPeminjaman)

        self.nOPEMINJAMANLabel = QLabel(self.frame)
        self.nOPEMINJAMANLabel.setObjectName(u"nOPEMINJAMANLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.nOPEMINJAMANLabel)

        self.cmbPembayaran = QComboBox(self.frame)
        self.cmbPembayaran.setObjectName(u"cmbPembayaran")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.cmbPembayaran)

        self.cmbPengembalian = QComboBox(self.frame)
        self.cmbPengembalian.setObjectName(u"cmbPengembalian")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.cmbPengembalian)

        self.sTATUSPEMBAYARANLabel = QLabel(self.frame)
        self.sTATUSPEMBAYARANLabel.setObjectName(u"sTATUSPEMBAYARANLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.sTATUSPEMBAYARANLabel)

        self.sTATUSPENGEMBALIANLabel = QLabel(self.frame)
        self.sTATUSPENGEMBALIANLabel.setObjectName(u"sTATUSPENGEMBALIANLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.sTATUSPENGEMBALIANLabel)


        self.verticalLayout.addLayout(self.formLayout)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnTambah = QPushButton(self.frame_2)
        self.btnTambah.setObjectName(u"btnTambah")

        self.gridLayout_4.addWidget(self.btnTambah, 0, 0, 1, 1)

        self.btnUpdate = QPushButton(self.frame_2)
        self.btnUpdate.setObjectName(u"btnUpdate")

        self.gridLayout_4.addWidget(self.btnUpdate, 0, 1, 1, 1)

        self.btnHapus = QPushButton(self.frame_2)
        self.btnHapus.setObjectName(u"btnHapus")

        self.gridLayout_4.addWidget(self.btnHapus, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_2)

        self.viewData = QTableView(self.frame)
        self.viewData.setObjectName(u"viewData")

        self.verticalLayout.addWidget(self.viewData)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>FORM PEMBAYARAN</p></body></html>", None))
        self.iDALATLabel.setText(QCoreApplication.translate("Form", u"NO NOTA", None))
        self.jENISALATLabel.setText(QCoreApplication.translate("Form", u"DENDA", None))
        self.tIPEALATLabel.setText(QCoreApplication.translate("Form", u"TOTAL_BIAYA", None))
        self.mERKLabel.setText(QCoreApplication.translate("Form", u"JUMLAH BAYAR", None))
        self.wARNALabel.setText(QCoreApplication.translate("Form", u"KEMBALIAN", None))
        self.dateTgl.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.tANGGALLabel.setText(QCoreApplication.translate("Form", u"TANGGAL", None))
        self.nOPEMINJAMANLabel.setText(QCoreApplication.translate("Form", u"NO PEMINJAMAN", None))
        self.sTATUSPEMBAYARANLabel.setText(QCoreApplication.translate("Form", u"STATUS PEMBAYARAN", None))
        self.sTATUSPENGEMBALIANLabel.setText(QCoreApplication.translate("Form", u"STATUS PENGEMBALIAN", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"TAMBAH", None))
        self.btnUpdate.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
    # retranslateUi

