# PYTHON FOR LOOPS

# 1. Python For Loops
# untuk mengulang data yang bersifat iterable seperti string, list, tuple, atau range

for i in range(1, 4):
    print("Perulangan ke:", i)


# 2. Looping Through a String
# Mengulang setiap karakter dalam string, menggunakan for

nama = "Nadya"

for huruf in nama:
    print("Huruf:", huruf)


# 3. break Statement
# Menghentikan loop sebelum selesai

for i in range(1, 6):
    if i == 4:
        print("Loop dihentikan dengan break")
        break
    print("Angka:", i)


# 4. continue Statement
# Melewati satu perulangan dan lanjut ke perulangan berikutnya

for i in range(1, 6):
    if i == 3:
        print("Angka 3 dilewati")
        continue
    print("Angka:", i)


# 5. range() Function
# Menghasilkan urutan angka

for i in range(2, 10, 2):
    print("Angka genap:", i)


# 6. Else in For Loop
# else dijalankan jika loop selesai tanpa break

for i in range(1, 4):
    print("Loop:", i)
else:
    print("Loop selesai tanpa break")


# 7. Nested Loops
# Loop di dalam loop

for i in range(1, 4):
    for j in range(1, 3):
        print("i =", i, ", j =", j)


# 8. pass Statement
# pass digunakan sebagai placeholder, agar kode tidak error walaupun belum diisi

for i in range(1, 4):
    if i == 2:
        pass         # belum ada aksi
    print("Nilai:", i)
