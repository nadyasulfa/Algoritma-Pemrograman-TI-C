# PYTHON OPERATORS

# 1. Arithmetic Operators (operasi matematika)
a = 10
b = 3
print(a + b)        # Penjumlahan
print(a - b)        # Pengurangan
print(a * b)        # Perkalian

# 2. Division in Python
print(a / b)        # /  : hasil float
print(a // b)       # // : hasil int (dibulatkan ke bawah)

# 3. Assignment Operators (untuk memberikan nilai ke variabel)
x = 5
x += 2
print(x)

# 4. Walrus Operator (:=)
# Digunakan untuk memberi nilai dan langsung dipakai dalam satu baris
if (n := len("nadya")) > 3:
    print(n)

# 5. Comparison Operators (untuk membandingkan dua nilai, hasilnya boolean)
print(a > b)        # Lebih besar
print(a == b)       # Sama dengan
print(a != b)       # Tidak sama

# 6. Chaining Comparison Operators (membandingkan lebih dari dua nilai sekaligus)
umur = 19
print(17 < umur < 25)

# 7. Logical Operators (untuk logika boolean)
print(umur >= 17 and umur <= 25)    # Kedua benar
print(umur < 17 or umur > 60)       # Salah satu benar
print(not False)                    # Kebalikan

# 8. Identity Operators (untuk membandingkan objek, bukan niali)
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)       # is     : objek sama (mmebandingkan alamat objek di memori)
print(list1 is list3)       # is not : objek tidak sama
print(list1 == list3)       # ==     : membandingkan nilai

# 9. Membership Operators (untuk mengecek keanggotaan data)
buah = ["apel", "mangga", "jeruk"]
print("apel" in buah)       # in     : Ada
print("pisang" not in buah) # not in : Tidak ada

# 10. Membership in Strings (untuk mengecek teks di dalam str)
teks = "Namaku Nadya"
print("Nadya" in teks)

# 11. Bitwise Operators (digunakan pada bilangan biner)
print(5 & 3)                # & : Bitwise AND
print(5 | 3)                # | : Bitwise OR
print(5 ^ 3)                # ^ : Bitwise XOR

# 12. Operator Precedence (urutan prioritas operasi saat dieksekusi)
hasil = 10 + 3 * 2
print(hasil)

# 13. Left-to-Right Evaluation (jika prioritas sama, dieksekusi dari kiri ke kanan)
hasil2 = 10 - 3 - 2
print(hasil2)
