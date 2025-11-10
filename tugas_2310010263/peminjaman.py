from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud


class peminjaman(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        filenya = QFile('peminjaman.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formanggota = muatfile.load(filenya,self)

        self.aksi = crud()

        self.formanggota.btnTambah.clicked.connect(self.tambahpeminjaman)

        self.formanggota.btnUpdate.clicked.connect(self.updatepeminjaman)

        self.formanggota.btnHapus.clicked.connect(self.hapuspeminjaman)

    def tambahpeminjaman(self):
        no_peminjaman = self.formanggota.txtIdUsr.text()
        tgl_pinjam = self.formanggota.datePinjam.date().toString("yyyy-MM-dd")
        tgl_selesai = self.formanggota.dateSelesai.date().toString("yyyy-MM-dd")
        id_pelanggan = self.formanggota.cmbPelanggan.currentText()
        id_alat = self.formanggota.cmbIdAlat.currentText()
        id_user = self.formanggota.cmbIdUser.currentText()
        self.aksi.tambahPeminjaman(no_peminjaman, tgl_pinjam, tgl_selesai, id_pelanggan, id_alat, id_user)

    def updatepeminjaman(self):
        no_peminjaman = self.formanggota.txtIdUsr.text()
        tgl_pinjam = self.formanggota.datePinjam.date().toString("yyyy-MM-dd")
        tgl_selesai = self.formanggota.dateSelesai.date().toString("yyyy-MM-dd")
        id_pelanggan = self.formanggota.cmbPelanggan.currentText()
        id_alat = self.formanggota.cmbIdAlat.currentText()
        id_user = self.formanggota.cmbIdUser.currentText()
        self.aksi.updatePeminjaman(no_peminjaman, tgl_pinjam, tgl_selesai, id_pelanggan, id_alat, id_user)

    def hapuspeminjaman(self):
        id_peminjaman= self.formanggota.txtIdUsr.text()
        self.aksi.hapusPeminjaman(id_peminjaman)
