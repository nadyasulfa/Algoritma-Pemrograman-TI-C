#Sub-bab Python Variables
# 1. Creating Variables, variabel diberi nilai langsung
umur = 19
nama = "Nadya"

# 2. Single or Double Quotes, code menerima tanda "" atau '' untuk teks (string)
alamat1 = 'Kampar'
alamat2 = "Panam"

# 3. Casting, mengubah tipe data
umur_str = str(umur)  # tipe data umur sebelum nya adalah int diubah menjadi str

# 4. Get the Type, digunakan untuk mengetahui tipe data suatu veriabel
print(type(umur))
print(type(umur_str))

# 5. Case-Sensitive, membedakan huruf besar dan huruf kecil, umur != Umur
Umur = 20

print("umur =", umur)
print("Umur =", Umur)

# Sub-bab Variable Names

# 1. Variable names, harus di awali huruf atau (_), tidak boleh pakai spasi
# Multi Words Variable Names, jika nama lebih dari satu kata tidak boleh pakai spasi
umur = 19

# 2. Camel Case, huruf pertama dari kata pertama kecil dan kata selanjutnya besar
prodiMahasiswa = "S1 Teknik Informatika"

# 3. Pascal Case, semua kata diawali huruf besar
NamaLengkap = "Nadya Sulfa Ul-zannah"

# 4. Snake Case, semua huruf kecil dan dipisahkan dengan underscore (_)
tempat_tinggal_sekarang = "Bangau Sakti"

print("Umur :", umur)
print("Prodi Mahasiswa :", prodiMahasiswa)
print("Nama Lengkap :", NamaLengkap)
print("Tempat tinggal sekarang :", tempat_tinggal_sekarang)

# Sub-bab Assign Multiple Values
# 1. Memberikan lebih dari satu nilai ke variabel sekaligus dalam satu baris kode

# 2. Many Values to Multiple Variables
# Memberikan banyak nilai ke banyak variabel dalam satu baris
a, b, c = 1, 2, 3
print("a =", a, "b =", b, "c =", c)

# 3. One Value to Multiple Variables
# Memberikan satu nilai yang sama ke banyak variabel
x = y = z = 10
print("x =", x, "y =", y, "z =", z)

# 4. Unpack a Collection
# Mengambil nilai dari list (data bisa diubah) atau tuple (data tetap) dan memasukkannya ke variabel
buah = ["semangka", "anggur", "mangga"]
buah1, buah2, buah3 = buah
print("Buah 1:", buah1)
print("Buah 2:", buah2)
print("Buah 3:", buah3)

# Sub-bab Output Variables

nama = "Nadya"
umur = 19
tinggi = 157

# 1. Metode panggil variabel
print(nama)

# 2. Metode koma
print((nama), (umur), (tinggi))

# 3. Metode +
print("namaku " + nama + " umurku " + str(umur))

# 4. Untuk angka, tanda (+) berfungsi sebagai operator matematika
# Tidak bisa menggabungkan string dan int / float dengan (+), maka akan error
x = 10
y = 9
print(x + y)

# 5. Agar gabungan str dan int / float dapat ditampilkan gunakan (,)
i = 19
j = "Tahun"
print(i, j)

# Sub-bab Global Variables
# 1. Global variables, variabel di luar fungdi, bisa diakses dimana saja
# 2. Globab keyword, dipakai jika ingin mengubah variabel global di dalam fungsi

umur = 19  # Variabel global

def cek_ktp():
    # Mengakses variabel global
    print("Umur di dalam fungsi:", umur)

def ubah_umur():
    # Mengubah variabel global
    global umur
    umur = 20

print("Umur sebelum diubah:", umur)

cek_ktp()      # memanggil fungsi

ubah_umur()    # mengubah nilai variabel global

print("Umur setelah diubah:", umur)



