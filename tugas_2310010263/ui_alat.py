# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alat.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 596)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 131, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 50, 341, 511))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.iDALATLabel = QLabel(self.frame)
        self.iDALATLabel.setObjectName(u"iDALATLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDALATLabel)

        self.txtId = QLineEdit(self.frame)
        self.txtId.setObjectName(u"txtId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtId)

        self.jENISALATLabel = QLabel(self.frame)
        self.jENISALATLabel.setObjectName(u"jENISALATLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.jENISALATLabel)

        self.cmbJenis = QComboBox(self.frame)
        self.cmbJenis.addItem("")
        self.cmbJenis.addItem("")
        self.cmbJenis.addItem("")
        self.cmbJenis.addItem("")
        self.cmbJenis.addItem("")
        self.cmbJenis.setObjectName(u"cmbJenis")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbJenis)

        self.tIPEALATLabel = QLabel(self.frame)
        self.tIPEALATLabel.setObjectName(u"tIPEALATLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tIPEALATLabel)

        self.cmbTipe = QComboBox(self.frame)
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.addItem("")
        self.cmbTipe.setObjectName(u"cmbTipe")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbTipe)

        self.mERKLabel = QLabel(self.frame)
        self.mERKLabel.setObjectName(u"mERKLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.mERKLabel)

        self.txtMerk = QLineEdit(self.frame)
        self.txtMerk.setObjectName(u"txtMerk")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtMerk)

        self.wARNALabel = QLabel(self.frame)
        self.wARNALabel.setObjectName(u"wARNALabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.wARNALabel)

        self.txtWarna = QLineEdit(self.frame)
        self.txtWarna.setObjectName(u"txtWarna")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtWarna)

        self.sEWAPERHAARILabel = QLabel(self.frame)
        self.sEWAPERHAARILabel.setObjectName(u"sEWAPERHAARILabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.sEWAPERHAARILabel)

        self.txtSewa = QLineEdit(self.frame)
        self.txtSewa.setObjectName(u"txtSewa")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtSewa)


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

        self.tableView = QTableView(self.frame)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"FORM ALAT", None))
        self.iDALATLabel.setText(QCoreApplication.translate("Form", u"ID ALAT", None))
        self.jENISALATLabel.setText(QCoreApplication.translate("Form", u"JENIS ALAT", None))
        self.cmbJenis.setItemText(0, QCoreApplication.translate("Form", u"Dipetik", None))
        self.cmbJenis.setItemText(1, QCoreApplication.translate("Form", u"Digesek", None))
        self.cmbJenis.setItemText(2, QCoreApplication.translate("Form", u"Ditiup", None))
        self.cmbJenis.setItemText(3, QCoreApplication.translate("Form", u"Dipukul", None))
        self.cmbJenis.setItemText(4, QCoreApplication.translate("Form", u"Ditekan", None))

        self.tIPEALATLabel.setText(QCoreApplication.translate("Form", u"TIPE ALAT", None))
        self.cmbTipe.setItemText(0, QCoreApplication.translate("Form", u"Gitar", None))
        self.cmbTipe.setItemText(1, QCoreApplication.translate("Form", u"Ukulele", None))
        self.cmbTipe.setItemText(2, QCoreApplication.translate("Form", u"Kecapi", None))
        self.cmbTipe.setItemText(3, QCoreApplication.translate("Form", u"Biola", None))
        self.cmbTipe.setItemText(4, QCoreApplication.translate("Form", u"Selo", None))
        self.cmbTipe.setItemText(5, QCoreApplication.translate("Form", u"Rebab", None))
        self.cmbTipe.setItemText(6, QCoreApplication.translate("Form", u"Seruling", None))
        self.cmbTipe.setItemText(7, QCoreApplication.translate("Form", u"Terompet", None))
        self.cmbTipe.setItemText(8, QCoreApplication.translate("Form", u"Klarinet", None))
        self.cmbTipe.setItemText(9, QCoreApplication.translate("Form", u"Gendang", None))
        self.cmbTipe.setItemText(10, QCoreApplication.translate("Form", u"Drum set", None))
        self.cmbTipe.setItemText(11, QCoreApplication.translate("Form", u"Keyboard", None))

        self.mERKLabel.setText(QCoreApplication.translate("Form", u"MERK", None))
        self.wARNALabel.setText(QCoreApplication.translate("Form", u"WARNA", None))
        self.sEWAPERHAARILabel.setText(QCoreApplication.translate("Form", u"SEWA PERHARI", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"TAMBAH", None))
        self.btnUpdate.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
    # retranslateUi

