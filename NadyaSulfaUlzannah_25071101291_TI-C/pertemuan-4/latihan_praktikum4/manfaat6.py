# dapat digunkan untuk mengontrol alur program
try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input salah!")
else:                       # else dijalankan jika tidak ada error
    print("Input benar.")
finally:                    # finally selalu jalan
    print("Program selesai.")

    # ini membuat struktur program lebih terorganisir