import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from user import user
from alat import alat
from pelanggan import pelanggan
from peminjaman import peminjaman
from pembayaran import pembayaran

class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile('form.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formutama = muatfile.load(filenya,self)
        self.resize(self.formutama.size())
        self.setMenuBar(self.formutama.menuBar())
        #actionFORM_USER
        self.formutama.actionFORM_USER.triggered.connect(self.bukauser)
        #actionFORM_ALAT
        self.formutama.actionFORM_ALAT.triggered.connect(self.bukaalat)
        #actionFORM_PELANGGAN
        self.formutama.actionFORM_PELANGGAN.triggered.connect(self.bukapelanggan)
        #actionFORM_PEMINJAMAN
        self.formutama.actionFORM_PEMINJAMAN.triggered.connect(self.bukapeminjaman)
        #actionFORM_PEMBAYARAN
        self.formutama.actionFORM_PEMBAYARAN.triggered.connect(self.bukapembayaran)

    #fungsi buka form user
    def bukauser(self):
        self.userBuka = user()
        self.userBuka.show()

    #fungsi buka form alat
    def bukaalat(self):
        self.alatBuka = alat()
        self.alatBuka.show()

    #fungsi buka form pelanggan
    def bukapelanggan(self):
        self.pelangganBuka = pelanggan()
        self.pelangganBuka.show()

    #fungsi buka form peminjaman
    def bukapeminjaman(self):
        self.peminjamanBuka = peminjaman()
        self.peminjamanBuka.show()

    #fungsi buka form pembayaran
    def bukapembayaran(self):
        self.pembayaranBuka = pembayaran()
        self.pembayaranBuka.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = main()
    jendela.show()
    sys.exit(app.exec())
