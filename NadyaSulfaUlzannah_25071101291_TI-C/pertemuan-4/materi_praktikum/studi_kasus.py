class Kucing:
    
    def __init__(self, jenis, warna):
        self.jenis = jenis
        self.warna = warna
        self.langkah = 0

    def input_langkah(self):
        try:
            self.langkah = int(input("Masukkan jumlah langkah: "))
        except ValueError:
            print("Terjadi ValueError! Harus angka.")
            return False
        return True

    def move(self):
        print(self.jenis, self.warna, "berjalan sebanyak", self.langkah, "langkah.")

# membuat objek
kucing1 = Kucing("Anggora", "Putih")

# jalankan input dan move
if kucing1.input_langkah():
    kucing1.move()