class Buku:
    def __init__(self, judul, denda_per_hari):
        self.judul = judul
        self.denda_per_hari = denda_per_hari

    def tampilkan(self):
        print(self.judul, "- Denda Rp", self.denda_per_hari, "/hari")


class Peminjaman:
    def __init__(self):
        self.total_denda = 0

    def tambah(self, buku, hari_terlambat):
        denda = buku.denda_per_hari * hari_terlambat
        self.total_denda += denda

    def ringkasan(self):
        print("Total denda Anda: Rp", self.total_denda)


buku_list = [
    Buku("Algoritma", 2000),
    Buku("Basis Data", 3000),
    Buku("Aljabar Linear", 2500)
]

print("Daftar Buku:")
for i in range(len(buku_list)):
    print(i+1, end=". ")
    buku_list[i].tampilkan()

p = Peminjaman()

pilih = int(input("Pilih nomor buku: "))

hari = int(input("Masukkan hari keterlambatan: "))

p.tambah(buku_list[pilih-1], hari)

p.ringkasan()