# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(462, 542)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 90, 401, 16))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 130, 261, 231))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnUser = QPushButton(self.frame)
        self.btnUser.setObjectName(u"btnUser")

        self.verticalLayout.addWidget(self.btnUser)

        self.btnPelanggan = QPushButton(self.frame)
        self.btnPelanggan.setObjectName(u"btnPelanggan")

        self.verticalLayout.addWidget(self.btnPelanggan)

        self.btnAlat = QPushButton(self.frame)
        self.btnAlat.setObjectName(u"btnAlat")

        self.verticalLayout.addWidget(self.btnAlat)

        self.btnPeminjaman = QPushButton(self.frame)
        self.btnPeminjaman.setObjectName(u"btnPeminjaman")

        self.verticalLayout.addWidget(self.btnPeminjaman)

        self.btnPembayaran = QPushButton(self.frame)
        self.btnPembayaran.setObjectName(u"btnPembayaran")

        self.verticalLayout.addWidget(self.btnPembayaran)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"APLIKASI JASA PEMINJAMAN ALAT MUSIK", None))
#if QT_CONFIG(accessibility)
        self.frame.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.btnUser.setText(QCoreApplication.translate("Form", u"USER", None))
        self.btnPelanggan.setText(QCoreApplication.translate("Form", u"PELANGGAN", None))
        self.btnAlat.setText(QCoreApplication.translate("Form", u"ALAT", None))
        self.btnPeminjaman.setText(QCoreApplication.translate("Form", u"PEMINJAMAN", None))
        self.btnPembayaran.setText(QCoreApplication.translate("Form", u"PEMBAYARAN", None))
    # retranslateUi

