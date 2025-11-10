import mysql.connector

class crud:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
        host = 'localhost',
        user =  'root',
        password = '',
        database = 'db_2310010263')

    #FUNCTION CRUD UNTUK TABEL USER
    def tambahUser(self, id_user, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into user(id_user, username, password) value(%s, %s, %s)",
        (id_user, username, password))
        self.koneksi.commit()
        aksi.close()

    def updateUser(self, id_user, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute("update user set username = %s, password = %s, where id_user= %s",
        (username, password, id_user))
        self.koneksi.commit()
        aksi.close()

    def hapusUser(self, id_user):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from user where id_user = %s",
        (id_user))
        self.koneksi.commit()
        aksi.close()

    #FUNCTION UNTUK TABEL PELANGGAN
    def tambahPelanggan(self, id_pelanggan, no_ktp, nama_lengkap, alamat, jenis_kelamin):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into pelanggan(id_pelanggan, no_ktp, nama_lengkap, alamat, jenis_kelamin) value(%s, %s, %s, %s, %s)",
        (id_pelanggan, no_ktp, nama_lengkap, alamat, jenis_kelamin))
        self.koneksi.commit()
        aksi.close()

    def updatePelanggan(self, id_pelanggan, no_ktp, nama_lengkap, alamat, jenis_kelamin):
        aksi = self.koneksi.cursor()
        aksi.execute("update pelanggan set no_ktp = $s, nama_lengkap = %s, alamat= %s, jenis_kelamin = %s, wehere id_pelanggan= %s",
        (no_ktp, nama_lengkap, alamat, jenis_kelamin, id_pelanggan))
        self.koneksi.commit()
        aksi.close()

    def hapusPelanggan(self, id_pelanggan):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from pelanggan where id_pelanggan = %s",
        (id_pelanggan))
        self.koneksi.commit()
        aksi.close()

    #FUNCTION UNTUK TABEL ALAT
    def tambahAlat(self, id_alat, jenis_alat, tipe_alat, merk, warna, sewa_perhari):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into alat(id_alat, jenis_alat, tipe_alat, merk, warna, sewa_perhari) value(%s, %s, %s, %s, %s, %s)",
        (id_alat, jenis_alat, tipe_alat, merk, warna, sewa_perhari))
        self.koneksi.commit()
        aksi.close()

    def updateAlat(self, id_alat, jenis_alat, tipe_alat, merk, warna, sewa_perhari):
        aksi = self.koneksi.cursor()
        aksi.execute("update alat set jenis_alat = $s, tipe_alat = %s, merk = %s, warna = %s, sewa_perhari = %s, wehere id_alat= %s",
        (jenis_alat, tipe_alat, merk, warna, sewa_perhari, id_alat))
        self.koneksi.commit()
        aksi.close()

    def hapusAlat(self, id_alat):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from alat where id_alat = %s",
        (id_alat))
        self.koneksi.commit()
        aksi.close()

    #FUNCTION UNTUK TABEL PEMINJAMAN
    def tambahPeminjaman(self, no_peminjaman, tgl_pinjam, tgl_selesai, id_pelanggan, id_alat, id_user):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into peminjaman(no_peminjaman, tgl_pinjam, tgl_selesai, id_pelanggan, id_alat, id_user) value(%s, %s, %s, %s, %s, %s)",
        (no_peminjaman, tgl_pinjam, tgl_selesai, id_pelanggan, id_alat, id_user))
        self.koneksi.commit()
        aksi.close()

    def updatePeminjaman(self, no_peminjaman, tgl_pinjam, tgl_selesai, id_pelanggan, id_alat, id_user):
        aksi = self.koneksi.cursor()
        aksi.execute("update peminjaman set tgl_pinjam = $s, tgl_selesai = %s, id_pelanggan = %s, id_alat = %s, id_user, where id_peminjaman= %s",
        (tgl_pinjam, tgl_selesai, id_pelanggan, id_alat, id_user, no_peminjaman))
        self.koneksi.commit()
        aksi.close()

    def hapusPeminjaman(self, id_peminjaman):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from peminjaman where id_peminjaman= %s",
        (id_peminjaman))
        self.koneksi.commit()
        aksi.close()

    #FUNCTION UNTUK TABEL PEMBAYARAN
    def tambahPembayaran(self, no_nota, tgl, denda, total_biaya, jumlah_bayar, kembalian, status_pembayaran, status_pengembalian, no_peminjaman):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into pembayaran(no_nota, tgl, denda, total_biaya, jumlah_bayar, kembalian, status_pembayaran, status_pengembalian, no_peminjaman) value(%s, %s, %s, %s, %s, %s, %s, $s, $s)",
        (no_nota, tgl, denda, total_biaya, jumlah_bayar, kembalian, status_pembayaran, status_pengembalian, no_peminjaman))
        self.koneksi.commit()
        aksi.close()

    def updatePembayaran(self, no_nota, tgl, denda, total_biaya, jumlah_bayar, kembalian, status_pembayaran, status_pengembalian, no_peminjaman):
        aksi = self.koneksi.cursor()
        aksi.execute("update Pembayaran set tgl = $s, dneda = %s, total_biaya = %s, jumlah_bayar = %s, kembalian = %s, status_pembayaran = %s, status_pengembalian  = %s, no_peminjaman = %s, where no_nota = %s",
        (tgl, denda, total_biaya, jumlah_bayar, kembalian, status_pembayaran, status_pengembalian, no_peminjaman, no_nota))
        self.koneksi.commit()
        aksi.close()

    def hapusPembayaran(self, no_nota):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from pembayaran where no_nota= %s",
        (no_nota))
        self.koneksi.commit()
        aksi.close()

