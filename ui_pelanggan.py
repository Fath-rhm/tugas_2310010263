# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pelanggan.ui'
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
        Form.resize(400, 588)
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

        self.txtIdPlg = QLineEdit(self.frame)
        self.txtIdPlg.setObjectName(u"txtIdPlg")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtIdPlg)

        self.jENISALATLabel = QLabel(self.frame)
        self.jENISALATLabel.setObjectName(u"jENISALATLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.jENISALATLabel)

        self.txtNoKtp = QLineEdit(self.frame)
        self.txtNoKtp.setObjectName(u"txtNoKtp")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNoKtp)

        self.tIPEALATLabel = QLabel(self.frame)
        self.tIPEALATLabel.setObjectName(u"tIPEALATLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tIPEALATLabel)

        self.txtNmLkp = QLineEdit(self.frame)
        self.txtNmLkp.setObjectName(u"txtNmLkp")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtNmLkp)

        self.mERKLabel = QLabel(self.frame)
        self.mERKLabel.setObjectName(u"mERKLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.mERKLabel)

        self.txtAlamat = QLineEdit(self.frame)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtAlamat)

        self.jENISKELAMINLabel = QLabel(self.frame)
        self.jENISKELAMINLabel.setObjectName(u"jENISKELAMINLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jENISKELAMINLabel)

        self.cmbJk = QComboBox(self.frame)
        self.cmbJk.addItem("")
        self.cmbJk.addItem("")
        self.cmbJk.setObjectName(u"cmbJk")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbJk)


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
        self.label.setGeometry(QRect(100, 10, 201, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDALATLabel.setText(QCoreApplication.translate("Form", u"ID PELANGGAN", None))
        self.jENISALATLabel.setText(QCoreApplication.translate("Form", u"NO KTP", None))
        self.tIPEALATLabel.setText(QCoreApplication.translate("Form", u"NAMA LENGKAP", None))
        self.mERKLabel.setText(QCoreApplication.translate("Form", u"ALAMAT", None))
        self.jENISKELAMINLabel.setText(QCoreApplication.translate("Form", u"JENIS KELAMIN", None))
        self.cmbJk.setItemText(0, QCoreApplication.translate("Form", u"laki-laki", None))
        self.cmbJk.setItemText(1, QCoreApplication.translate("Form", u"perempuan", None))

        self.btnTambah.setText(QCoreApplication.translate("Form", u"TAMBAH", None))
        self.btnUpdate.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>FORM PELANGGAN</p></body></html>", None))
    # retranslateUi

