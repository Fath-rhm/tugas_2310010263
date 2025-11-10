# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 471)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 121, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 70, 341, 331))
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

        self.jENISALATLabel = QLabel(self.frame)
        self.jENISALATLabel.setObjectName(u"jENISALATLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.jENISALATLabel)

        self.txtUsn = QLineEdit(self.frame)
        self.txtUsn.setObjectName(u"txtUsn")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtUsn)

        self.tIPEALATLabel = QLabel(self.frame)
        self.tIPEALATLabel.setObjectName(u"tIPEALATLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tIPEALATLabel)

        self.txtPw = QLineEdit(self.frame)
        self.txtPw.setObjectName(u"txtPw")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtPw)


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
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>FORM USER</p></body></html>", None))
        self.iDALATLabel.setText(QCoreApplication.translate("Form", u"ID USER", None))
        self.jENISALATLabel.setText(QCoreApplication.translate("Form", u"USERNAME", None))
        self.tIPEALATLabel.setText(QCoreApplication.translate("Form", u"PASSWORD", None))
        self.btnTambah.setText(QCoreApplication.translate("Form", u"TAMBAH", None))
        self.btnUpdate.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
    # retranslateUi

