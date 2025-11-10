# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'peminjaman.ui'
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
        Form.resize(400, 538)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 90, 341, 431))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.iDALATLabel = QLabel(self.frame)
        self.iDALATLabel.setObjectName(u"iDALATLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDALATLabel)

        self.txtIdUsr = QLineEdit(self.frame)
        self.txtIdUsr.setObjectName(u"txtIdUsr")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtIdUsr)

        self.tANGGALPINJAMLabel = QLabel(self.frame)
        self.tANGGALPINJAMLabel.setObjectName(u"tANGGALPINJAMLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.tANGGALPINJAMLabel)

        self.datePinjam = QDateEdit(self.frame)
        self.datePinjam.setObjectName(u"datePinjam")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.datePinjam)

        self.tANGGALSELESAILabel = QLabel(self.frame)
        self.tANGGALSELESAILabel.setObjectName(u"tANGGALSELESAILabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tANGGALSELESAILabel)

        self.dateSelesai = QDateEdit(self.frame)
        self.dateSelesai.setObjectName(u"dateSelesai")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateSelesai)

        self.iDPELANGGANLabel = QLabel(self.frame)
        self.iDPELANGGANLabel.setObjectName(u"iDPELANGGANLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.iDPELANGGANLabel)

        self.cmbPelanggan = QComboBox(self.frame)
        self.cmbPelanggan.setObjectName(u"cmbPelanggan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbPelanggan)

        self.iDALATLabel_2 = QLabel(self.frame)
        self.iDALATLabel_2.setObjectName(u"iDALATLabel_2")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.iDALATLabel_2)

        self.cmbIdAlat = QComboBox(self.frame)
        self.cmbIdAlat.setObjectName(u"cmbIdAlat")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbIdAlat)

        self.iDUSERLabel = QLabel(self.frame)
        self.iDUSERLabel.setObjectName(u"iDUSERLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.iDUSERLabel)

        self.cmbIdUser = QComboBox(self.frame)
        self.cmbIdUser.setObjectName(u"cmbIdUser")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbIdUser)


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

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 40, 211, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDALATLabel.setText(QCoreApplication.translate("Form", u"NO PEMINJAMAN", None))
        self.tANGGALPINJAMLabel.setText(QCoreApplication.translate("Form", u"TANGGAL PINJAM", None))
        self.datePinjam.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.tANGGALSELESAILabel.setText(QCoreApplication.translate("Form", u"TANGGAL SELESAI", None))
        self.dateSelesai.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.iDPELANGGANLabel.setText(QCoreApplication.translate("Form", u"ID PELANGGAN", None))
        self.iDALATLabel_2.setText(QCoreApplication.translate("Form", u"ID ALAT", None))
        self.iDUSERLabel.setText(QCoreApplication.translate("Form", u"ID USER", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"TAMBAH", None))
        self.btnUpdate.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>FORM PEMINJAMAN</p><p><br/></p></body></html>", None))
    # retranslateUi

