# sub-bab Syntax
"""
Dalam python ada identation / tab di awal baris code
kegunaannya sama dengan {} pada C
jika identation salah, maka program akan error

Comment (komentar) yaitu catatan yang tidak di baca oleh code program
biasa menggunakan tanda # (untuk comment satu baris)
dan tanda " atau ' (untuk comment banyak baris)
"""

# contoh Program cek kepemilikan KTP

# 1. Variabel yaitu tempat menyimpan sebuah data atau nilai
nama = "Nadya"
umur = 19

#sub-bab Statement

# 1. Statement yaitu satu baris perintah yang dijalankan
print("Cek Kepemilikan KTP")

# 2. Many Statements yaitu beberapa statement yang ditulis berurutan
print("Nama:", nama)
print("Umur:", umur)

# 3. Semicolon : memisahkan beberapa (statement) yang ditulis dalam satu baris, bersifat opsional
print("Contoh semicolon : "); print("Namaku", nama); print("Umurku", umur)

if umur >= 17:
    print("Status: Sudah punya KTP") # Ini adalah contoh identation
else:
    print("Status: Belum punya KTP")
