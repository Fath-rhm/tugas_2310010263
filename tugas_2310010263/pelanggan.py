from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud


class pelanggan(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        filenya = QFile('pelanggan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formanggota = muatfile.load(filenya,self)

        self.aksi = crud()

        self.formanggota.btnTambah.clicked.connect(self.tambahpelanggan)

        self.formanggota.btnUpdate.clicked.connect(self.updatepelanggan)

        self.formanggota.btnHapus.clicked.connect(self.hapuspelanggan)

    def tambahpelanggan(self):
        id_pelanggan= self.formanggota.txtIdPlg.text()
        no_ktp = self.formanggota.txtNoKtp.text()
        nama_lengkap = self.formanggota.txtNmLkp.text()
        alamat = self.formanggota.txtAlamat.text()
        jenis_kelamin = self.formanggota.cmbJk.currentText()
        self.aksi.tambahPelanggan(id_pelanggan, no_ktp, nama_lengkap, alamat, jenis_kelamin)

    def updatepelanggan(self):
        id_pelanggan= self.formanggota.txtIdPlg.text()
        no_ktp = self.formanggota.txtNoKtp.text()
        nama_lengkap = self.formanggota.txtNmLkp.text()
        alamat = self.formanggota.txtAlamat.text()
        jenis_kelamin = self.formanggota.cmbJk.currentText()
        self.aksi.tambahPelanggan(id_pelanggan, no_ktp, nama_lengkap, alamat, jenis_kelamin)

    def hapuspelanggan(self):
        id_pelanggan = self.formanggota.txtId.text()
        self.aksi.hapusPelanggan(id_pelanggan)
