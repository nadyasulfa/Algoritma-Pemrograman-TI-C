# NameError dengan metode Try-Except
try:
    nama = "Nadya"
    print(f"Hallo aku {nama}")
    print(f"Aku dari prodi {prodi}")
except NameError:
    print("Terjadi NameError! Variabel belum terdefinisi")