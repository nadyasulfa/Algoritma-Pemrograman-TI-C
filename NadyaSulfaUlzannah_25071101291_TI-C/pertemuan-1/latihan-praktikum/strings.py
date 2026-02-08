# Sub- bab Python String
# 1. Assign String to a Variable
teks = "Halo teman"

# 2. Quotes Inside Quotes, pakai tanda kutip berbeda atau tanda(\)
kalimat = "Dia berkata, \"kamu sangat cantik\""

# 3. Multiline Strings, gunakan tanda (""" """)
paragraf = """Ini adalah contoh
string dengan
banyak baris"""

# 4. Strings are Arrays, bisa diakses dengan indeksnya
huruf_pertama = teks[0]

# 5. Looping Through a String, dapat diulang menggunakan for
for huruf in teks:
    print(huruf)

# 6. String Length, panjang str bisa diketahuidengan fungsi len()
panjang = len(teks)
print("Panjang string:", panjang)

# 7. Check String, untuk ngecek apakah suatu teks ada di dalam string, gunakan in
print("teman" in teks)

# 8. Check if NOT, untuk ngecek teks tidak ada di dalam string, gunakan not in
print("musuh" not in teks)

# 9. Menampilkan hasil lain
print(huruf_pertama)
print(kalimat)
print(paragraf)

# Sub-bab Slicing Strings
# string awal
teks = "Namaku Nadya"

# 1. Slicing (ambil sebagian string)
hasil1 = teks[0:6]
print("Slicing:", hasil1)

# 2. Slice From the Start
# Jika indeks awal tidak ditulis, Python akan mulai dari indeks 0
hasil2 = teks[:6]
print("Slice dari awal:", hasil2)

# 3. Slice To the End
# Jika indeks akhir tidak ditulis, Python akan mengambil sampai akhir string
hasil3 = teks[7:]
print("Slice sampai akhir:", hasil3)

# 4. Negative Indexing
# indeks negatif dihitung dari belakang string
hasil4 = teks[-5:-1]
print("Negative indexing:", hasil4)

# string awal
teks = "  Hari ini sangat Seru  "

# 1. Upper Case (huruf besar semua)
print(teks.upper())

# 2. Lower Case (huruf kecil semua)
print(teks.lower())

# 3. Remove Whitespace (hapus spasi di awal dan akhir str)
print(teks.strip())

# 4. Replace String (ganti str dengan kata lain)
print(teks.replace("Seru", "Menyenangkan"))

# 5. Split String (pecah str menjadi list berdasarkan pemisah)
print(teks.split(" "))

# 6. String Concatenation (gabungkan str dengan tanda(+))
nama = "Nadya"
print("Halo " + nama)

# 7. String Format (gabungkan str dengan format ())
umur = 19
print("Nama saya {}, umur saya {}".format(nama, umur))

# 8. F-Strings ()
print(f"Nama saya {nama} dan umur saya {umur}")

# 9. Placeholders and Modifiers (untuk mengatur format nilai)
nilai = 95.56789
print("Nilai saya {:.2f}".format(nilai))

# 10. Escape Character (untuk karakter khusus)  # \" : tanda kutip
print("Dia berkata, \"Hari ini sangat cerah\"")      # \n : baris baru
print("Bermain di taman\nItu Menyenangkan")       # \t : tab

# 11. String Methods (fungsi bawaan str)
print(teks.capitalize())
print(teks.count("a"))


