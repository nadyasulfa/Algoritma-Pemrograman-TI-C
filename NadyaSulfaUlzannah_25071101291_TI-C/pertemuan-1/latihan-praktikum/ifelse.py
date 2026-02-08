# if elif else
# 1. Python Conditions and If Statements
# Condition adalah ekspresi yang menghasilkan True atau False.
# If statement menjalankan kode jika kondisi bernilai True.

umur = 19
nilai = 90

# 2. if (untuk menjalankan kode jika suatu kondisi bernilai True)
if umur >= 17:
    print("Sudah dewasa")

# 3. elif (else if), digunkan untuk mengecek kondisi lain jika kondisi if sebelumnya False
# 4. else (dijalankan jika semua kondisi if dan elif bernilai False)
# if - elif - else
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
else:
    print("Nilai C")

# 5. Shorthand if (bentuk singkat dari if dalam satu baris)
# Digunakan jika kodenya sangat sederhana
if umur >= 17: print("Boleh membuat KTP")

# 6. Logical operators (digunakan untuk menggabungkan beberapa kondisi)
# and : semua kondisi harus True
# or  : salah satu True
# not : membalik kondisi
if umur >= 17 and nilai >= 75:
    print("Memenuhi syarat")

# 7. Nested if (if dilam if)
# Digunakan untuk logika bertingkat
if umur >= 17:
    if nilai >= 75:
        print("Dewasa dan lulus")

# 8. Pass statement (perintah kosong)
# Digunakan saat struktur kode sudah ada tetapi belum ingin menulis isi program
if umur < 10:
    pass
else:
    print("Program selesai")
