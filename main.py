import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from user import user
from pelanggan import pelanggan
from alat import alat
from peminjaman import peminjaman
from pembayaran import pembayaran

class main(QMainWindow):
        def __init__(self):
                super(main, self).__init__()

                filenya = QFile('main.ui')
                filenya.open(QFile.ReadOnly)

                muatfile = QUiLoader()
                self.formutama = muatfile.load(filenya,self)

                self.setCentralWidget(self.formutama)
                self.resize(self.formutama.size())

                #btnUser form user
                self.btnUser = self.findChild(QWidget, "btnUser")
                self.btnUser.clicked.connect(self.on_btnUser_clicked)

                #btnPelanggan form pelanggan
                self.btnPelanggan = self.findChild(QWidget, "btnPelanggan")
                self.btnPelanggan.clicked.connect(self.on_btnPelanggan_clicked)

                #btnAlat form alat
                self.btnAlat = self.findChild(QWidget, "btnAlat")
                self.btnAlat.clicked.connect(self.on_btnAlat_clicked)

                #btnPeminjaman from peminjaman
                self.btnPeminjaman = self.findChild(QWidget, "btnPeminjaman")
                self.btnPeminjaman.clicked.connect(self.on_btnPeminjaman_clicked)

                #btnPembayaran form pembayaran
                self.btnPembayaran = self.findChild(QWidget, "btnPembayaran")
                self.btnPembayaran.clicked.connect(self.on_btnPembayaran_clicked)

                #Menampilkan form user
        def on_btnUser_clicked(self):
                self.bukaUser = user()
                self.bukaUser.show()

                #Menampilkan form pelanggan
        def on_btnPelanggan_clicked(self):
                self.bukaPelanggan = pelanggan()
                self.bukaPelanggan.show()

                #Menampilkan form alat
        def on_btnAlat_clicked(self):
            self.bukaAlat = alat()
            self.bukaAlat.show()

                #Menampilkan form peminjaman
        def on_btnPeminjaman_clicked(self):
                self.bukaPeminjaman = peminjaman()
                self.bukaPeminjaman.show()

                #Menampilkan form pembayaran
        def on_btnPembayaran_clicked(self):
                self.bukaPembayaran = pembayaran()
                self.bukaPembayaran.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = main()
    jendela.show()
    sys.exit(app.exec())
