# This Python file uses the following encoding: utf-8
import mysql.connector

class crud:
    def __init__(self):
        self.koneksiDB = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_masyarakat'
        )

    def simpanProker(self, id_proker, nama, waktu, anggaran, ket):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO proker (id_proker, nama_proker, waktu_laksana, anggaran, keterangan) VALUES (%s,%s,%s,%s,%s)"
        val = (id_proker, nama, waktu, anggaran, ket)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahProker(self, id_proker, nama, waktu, anggaran, ket):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE proker SET nama_proker=%s, waktu_laksana=%s, anggaran=%s, keterangan=%s WHERE id_proker=%s"
        val = (nama, waktu, anggaran, ket, id_proker)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusProker(self, id_proker):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM proker WHERE id_proker=%s", (id_proker,))
        self.koneksiDB.commit()
        kursor.close()

    def dataProker(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM proker ORDER BY id_proker ASC")
        return kursor.fetchall()

    def simpanRenbang(self, id_renbang, keg, lok, vol, dana, ket, status):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO renbang (id_renbang, kegiatan, lokasi, volume, dana_sumber, keterangan, status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (id_renbang, keg, lok, vol, dana, ket, status)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahRenbang(self, id_renbang, keg, lok, vol, dana, ket, status):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE renbang SET kegiatan=%s, lokasi=%s, volume=%s, dana_sumber=%s, keterangan=%s, status=%s WHERE id_renbang=%s"
        val = (keg, lok, vol, dana, ket, status, id_renbang)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusRenbang(self, id_renbang):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM renbang WHERE id_renbang=%s", (id_renbang,))
        self.koneksiDB.commit()
        kursor.close()

    def dataRenbang(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM renbang ORDER BY id_renbang ASC")
        return kursor.fetchall()

    def simpanBansos(self, id_bansos, uraian, jml, thn, salur, kat):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO bansos (id_bansos, uraian, jml_bantuan, tahun, disalurkan, kategori) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (id_bansos, uraian, jml, thn, salur, kat)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahBansos(self, id_bansos, uraian, jml, thn, salur, kat):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE bansos SET uraian=%s, jml_bantuan=%s, tahun=%s, disalurkan=%s, kategori=%s WHERE id_bansos=%s"
        val = (uraian, jml, thn, salur, kat, id_bansos)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusBansos(self, id_bansos):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM bansos WHERE id_bansos=%s", (id_bansos,))
        self.koneksiDB.commit()
        kursor.close()

    def dataBansos(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM bansos ORDER BY id_bansos ASC")
        return kursor.fetchall()

    def simpanGaleri(self, id_galeri, judul, tgl, ket):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO galeri (id_galeri, judul, tanggal, berita_keterangan) VALUES (%s,%s,%s,%s)"
        val = (id_galeri, judul, tgl, ket)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahGaleri(self, id_galeri, judul, tgl, ket):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE galeri SET judul=%s, tanggal=%s, berita_keterangan=%s WHERE id_galeri=%s"
        val = (judul, tgl, ket, id_galeri)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusGaleri(self, id_galeri):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM galeri WHERE id_galeri=%s", (id_galeri,))
        self.koneksiDB.commit()
        kursor.close()

    def dataGaleri(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM galeri ORDER BY id_galeri ASC")
        return kursor.fetchall()
