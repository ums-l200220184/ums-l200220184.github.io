# Program Python untuk mengilustrasikan proses mengikuti kuliah di Informatika

class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.spp_terbayar = False
        self.matakuliah = []
        self.nilai = {}

    def bayar_spp(self):
        # Proses pembayaran SPP
        print(f"{self.nama} membayar SPP.")
        self.spp_terbayar = True

    def daftar_matakuliah(self, matakuliah):
        # Proses pendaftaran mata kuliah
        if self.spp_terbayar:
            self.matakuliah = matakuliah
            print(f"{self.nama} mendaftar mata kuliah: {', '.join(matakuliah)}.")
        else:
            print("SPP belum dibayar! Harap bayar SPP terlebih dahulu.")

    def ikuti_perkuliahan(self):
        # Proses mengikuti perkuliahan
        if self.matakuliah:
            print(f"{self.nama} sedang mengikuti perkuliahan untuk mata kuliah: {', '.join(self.matakuliah)}.")
        else:
            print("Belum ada mata kuliah yang terdaftar.")

    def kerjakan_tugas_dan_ujian(self):
        # Proses mengerjakan tugas dan ujian
        if self.matakuliah:
            print(f"{self.nama} mengerjakan tugas dan ujian.")
            for mk in self.matakuliah:
                # Simulasi penilaian
                self.nilai[mk] = self.hitung_nilai()
        else:
            print("Belum ada mata kuliah yang terdaftar.")

    def hitung_nilai(self):
        # Fungsi untuk menghitung nilai secara acak (simulasi)
        import random
        return random.randint(60, 100)

    def lihat_nilai_akhir(self):
        # Menampilkan nilai akhir
        if self.nilai:
            print("Nilai akhir:")
            for mk, nilai in self.nilai.items():
                print(f"- {mk}: {nilai}")
        else:
            print("Belum ada nilai yang tersedia.")

# Simulasi proses
mahasiswa = Mahasiswa("Budi")

# Tahap 1: Bayar SPP
mahasiswa.bayar_spp()

# Tahap 2: Daftar mata kuliah
mahasiswa.daftar_matakuliah(["Pemrograman", "Struktur Data", "Basis Data"])

# Tahap 3: Ikuti perkuliahan
mahasiswa.ikuti_perkuliahan()

# Tahap 4: Kerjakan tugas dan ujian
mahasiswa.kerjakan_tugas_dan_ujian()

# Tahap 5: Lihat nilai akhir
mahasiswa.lihat_nilai_akhir()
