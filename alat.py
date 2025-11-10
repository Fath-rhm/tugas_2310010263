from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud


class alat(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        filenya = QFile('alat.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formanggota = muatfile.load(filenya,self)

        self.aksi = crud()

        self.formanggota.btnTambah.clicked.connect(self.tambahalat)

        self.formanggota.btnUpdate.clicked.connect(self.updatealat)

        self.formanggota.btnHapus.clicked.connect(self.hapusalat)

    def tambahalat(self):
        id_alat = self.formanggota.txtId.text()
        jenis_alat = self.formanggota.cmbJenis.currentText()
        tipe_alat= self.formanggota.cmbTipe.currentText()
        merk = self.formanggota.txtMerk.text()
        warna = self.formanggota.txtWarna.text()
        sewa_perhari = self.formanggota.txtSewa.text()
        self.aksi.tambahAlat(id_alat, jenis_alat, tipe_alat, merk, warna, sewa_perhari)

    def updatealat(self):
        id_alat = self.formanggota.txtId.text()
        jenis_alat = self.formanggota.cmbJenis.currentText()
        tipe_alat= self.formanggota.cmbTipe.currentText()
        merk = self.formanggota.txtMerk.text()
        warna = self.formanggota.txtWarna.text()
        sewa_perhari = self.formanggota.txtSewa.text()
        self.aksi.updateAlat(id_alat, jenis_alat, tipe_alat, merk, warna, sewa_perhari)

    def hapusalat(self):
        id_alat = self.formanggota.txtId.text()
        self.aksi.hapusAlat(id_alat)
