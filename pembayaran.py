from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud


class pembayaran(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        filenya = QFile('pembayaran.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formanggota = muatfile.load(filenya,self)

        self.aksi = crud()

        self.formanggota.btnTambah.clicked.connect(self.tambahpembayaran)

        self.formanggota.btnUpdate.clicked.connect(self.updatepembayaran)

        self.formanggota.btnHapus.clicked.connect(self.hapuspembayaran)

    def tambahpembayaran(self):
        no_nota= self.formanggota.txtNota.text()
        tgl = self.formanggota.dateTgl.date().toString("yyyy-MM-dd")
        denda = self.formanggota.txtDenda.text()
        total_biaya = self.formanggota.txtBiaya.text()
        jumlah_bayar = self.formanggota.txtJmlBayar.text()
        kembalian = self.formanggota.txtKembalian.text()
        status_pembayaran = self.formanggota.cmbPembayaran.currentText()
        status_pengembalian = self.formanggota.cmbPenggembalian.currentText()
        no_peminjaman = self.formanggota.txtIdUsr.text()
        self.aksi.tambahPembayaran(no_nota, tgl, denda, total_biaya, jumlah_bayar, kembalian, status_pembayaran, status_pengembalian, no_peminjaman)

    def updatepembayaran(self):
        no_nota= self.formanggota.txtNota.text()
        tgl = self.formanggota.dateTgl.date().toString("yyyy-MM-dd")
        denda = self.formanggota.txtDenda.text()
        total_biaya = self.formanggota.txtBiaya.text()
        jumlah_bayar = self.formanggota.txtJmlBayar.text()
        kembalian = self.formanggota.txtKembalian.text()
        status_pembayaran = self.formanggota.cmbPembayaran.currentText()
        status_pengembalian = self.formanggota.cmbPenggembalian.currentText()
        no_peminjaman = self.formanggota.txtIdUsr.text()
        self.aksi.updatePembayaran(no_nota, tgl, denda, total_biaya, jumlah_bayar, kembalian, status_pembayaran, status_pengembalian, no_peminjaman)

    def hapuspembayaran(self):
        no_nota = self.formanggota.txtNota.text()
        self.aksi.hapusPembayaran(no_nota)
