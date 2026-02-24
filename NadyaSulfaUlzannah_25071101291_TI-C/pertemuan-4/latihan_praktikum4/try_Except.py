# TypeError dengan metode Try-Except
try:
    hasil = "15" + 5
    print(hasil)
except TypeError:
    print("Terjadi TypeError! Tidak bisa menjumlahkan str dengan int")

# ValueError dengan metode Try-except
try:
    angka = int(input("Masukkan angka: "))
    print("Angka yang dimasukkan:", angka)
except ValueError:
    print("Terjadi ValueError! Input harus angka")

# ZeroDivisionError dengan metode Try-except
try:
    a = int(input("Masukkan angka: "))
    hasil = a / 0
    print(hasil)
except ZeroDivisionError:
    print("Terjadi ZeroDivisionError! Tidak boleh membagi dengan nol")

# NameError dengan metode Try-Except
try:
    nama = "Nadya"
    print(f"Hallo aku {nama}")
    print(f"Aku dari prodi {prodi}")
except NameError:
    print("Terjadi NameError! Variabel belum terdefinisi")

# IndexError dengan metode Try-except
try:
    data = [1,2,3,4]
    print(data[5])
except IndexError:
    print("Terjadi IndexError! Index tidak ada dalam list tersebut")

# KeyError dengan cara Try-Except
try:
    data = {"nama": "Nadya", "umur": 20}
    print(data["alamat"])
except KeyError:
    print("Terjadi KeyError! Key tidak ditemukan dalam dictionary")