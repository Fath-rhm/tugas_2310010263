# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(446, 396)
        self.actionkkjckasdv = QAction(main)
        self.actionkkjckasdv.setObjectName(u"actionkkjckasdv")
        self.actionFORM_PELANGGAN = QAction(main)
        self.actionFORM_PELANGGAN.setObjectName(u"actionFORM_PELANGGAN")
        self.actionFORM_ALAT = QAction(main)
        self.actionFORM_ALAT.setObjectName(u"actionFORM_ALAT")
        self.actionFORM_PEMINJAMAN = QAction(main)
        self.actionFORM_PEMINJAMAN.setObjectName(u"actionFORM_PEMINJAMAN")
        self.actionFORM_PEMBAYARAN = QAction(main)
        self.actionFORM_PEMBAYARAN.setObjectName(u"actionFORM_PEMBAYARAN")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 50, 261, 231))
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

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 401, 16))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 446, 21))
        self.menuduwqegfhen = QMenu(self.menubar)
        self.menuduwqegfhen.setObjectName(u"menuduwqegfhen")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuduwqegfhen.menuAction())
        self.menuduwqegfhen.addAction(self.actionkkjckasdv)
        self.menuduwqegfhen.addAction(self.actionFORM_PELANGGAN)
        self.menuduwqegfhen.addAction(self.actionFORM_ALAT)
        self.menuduwqegfhen.addAction(self.actionFORM_PEMINJAMAN)
        self.menuduwqegfhen.addAction(self.actionFORM_PEMBAYARAN)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionkkjckasdv.setText(QCoreApplication.translate("main", u"FORM USER", None))
        self.actionFORM_PELANGGAN.setText(QCoreApplication.translate("main", u"FORM PELANGGAN", None))
        self.actionFORM_ALAT.setText(QCoreApplication.translate("main", u"FORM ALAT", None))
        self.actionFORM_PEMINJAMAN.setText(QCoreApplication.translate("main", u"FORM PEMINJAMAN", None))
        self.actionFORM_PEMBAYARAN.setText(QCoreApplication.translate("main", u"FORM PEMBAYARAN", None))
#if QT_CONFIG(accessibility)
        self.frame.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.btnUser.setText(QCoreApplication.translate("main", u"USER", None))
        self.btnPelanggan.setText(QCoreApplication.translate("main", u"PELANGGAN", None))
        self.btnAlat.setText(QCoreApplication.translate("main", u"ALAT", None))
        self.btnPeminjaman.setText(QCoreApplication.translate("main", u"PEMINJAMAN", None))
        self.btnPembayaran.setText(QCoreApplication.translate("main", u"PEMBAYARAN", None))
        self.label.setText(QCoreApplication.translate("main", u"APLIKASI JASA PEMINJAMAN ALAT MUSIK", None))
        self.menuduwqegfhen.setTitle(QCoreApplication.translate("main", u"HALAMAN UTAMA", None))
    # retranslateUi

