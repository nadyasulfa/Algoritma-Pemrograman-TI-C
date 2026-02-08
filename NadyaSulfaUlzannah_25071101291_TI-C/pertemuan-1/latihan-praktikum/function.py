# PYTHON FUNCTIONS

# 1. Python Fungctions (menjalankan tugas tertentu dan dapat di panggil berulang kali)
def sapa():
    print("Halo, selamat pagi")

sapa()

# 2. Python Arguments (nilai yang dikirim ke fungsi saat fungsi dipanggil)

def sapa_nama(nama):
    print("Halo, aku", nama)

sapa_nama("Nadya")


# 3. Python *args/**kwargs
# *args (digunakan untuk banyak argument tanpa nama
def jumlah(*angka):
    print("Jumlah :", sum(angka))

jumlah(1, 2, 3, 4, 5)

# **kwargs digunakan untuk banyak argument dengan nama

def biodata(**data):
    print("Nama :", data["nama"])
    print("Umur :", data["umur"])

biodata(nama="Nadya", umur=19)

# 4. Python Scope (ruang lingkup variabel, dimana variabel bisa di akses)

x = 10     # variabel global : di luar fungsi

def contoh_scope():
    y = 5  # variabel local  : di dalam fungsi
    print("Nilai y (local) :", y)

contoh_scope()
print("Nilai x (global) :", x)

# 5. Python Decorators (menambahkan fitur ke fungsi lain, tanpa mengubah kode aslinya)

def dekorator(func):
    def pembungkus():
        print("Sebelum fungsi dijalankan")
        func()
        print("Sesudah fungsi dijalankan")
    return pembungkus

@dekorator
def halo():
    print("Halo selamat pagi")

halo()

# 6. Python Lambda (fungsi pendek(satu baris) tanpa nama)
# Untuk operasi sederhana

tambah = lambda a, b: a + b
print("Hasil lambda :", tambah(3, 4))

# 7. Python Recursion (fungsi yang memanggil dirinya sendiri)
# harus ada kondisi berhenti, jika tidak, infinite loop (loop tidak pernah berhenti)
def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n - 1)

print("Faktorial 5 :", faktorial(5))


# 8. Python Generators (menghasilkan nilai satu per satu menggunakan yield)
# yield : menyimpan keadaan fungsi, lalu bisa dilanjutkan lagi

def generator_angka():
    yield 1
    yield 2
    yield 3

for angka in generator_angka():
    print("Generator menghasilkan :", angka)
