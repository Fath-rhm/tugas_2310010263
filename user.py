from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class user(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        filenya = QFile('user.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formanggota = muatfile.load(filenya,self)

        self.aksi = crud()

        self.formanggota.btnTambah.clicked.connect(self.tambahuser)

        self.formanggota.btnUpdate.clicked.connect(self.updateuser)

        self.formanggota.btnHapus.clicked.connect(self.hapususer)

    def tambahuser(self):
        id_user = self.formanggota.txtIdUsr.text()
        username = self.formanggota.txtUsn.text()
        password = self.formanggota.txtPw.text()
        self.aksi.tambahUser(id_user, username, password)

    def updateuser(self):
        id_user = self.formanggota.txtIdUsr.text()
        username = self.formanggota.txtUsn.text()
        password = self.formanggota.txtPw.text()
        self.aksi.updateUser(id_user, username, password)

    def hapususer(self):
        id_user = self.formanggota.txtIdUsr.text()
        self.aksi.hapusUser(id_user)
