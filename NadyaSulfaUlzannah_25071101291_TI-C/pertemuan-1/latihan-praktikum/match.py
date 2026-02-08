# PYTHON MATCH STATEMENT

# Variabel yang akan digunakan
hari = "Sabtu"
nilai = 85
umur = 19

# 1. Python Match
# match digunakan sebagai pengganti if-else untuk mencocokkan nilai tertentu
# mirip switch-case

match hari:
    case "Senin":
        print("Hari kuliah")
    case "Sabtu":
        print("Hari libur")


# 2. The Python Match Statement
# Struktur dasar match-case, akan menjalankan case yang sesuai

match hari:
    case "Senin":
        print("Masuk kuliah")
    case "Minggu":
        print("Libur total")


# 3. Default Value (case _)
# case _ berfungsi sebagai default, dijalankan jika tidak ada case yang cocok

match hari:
    case "Senin":
        print("Hari kuliah")
    case "Minggu":
        print("Hari libur")
    case _:
        print("Hari biasa")


# 4. Combine Values
# Menggabungkan beberapa nilai dalam satu case menggunakan |

match hari:
    case "Sabtu" | "Minggu":
        print("Ini akhir pekan")
    case _:
        print("Bukan akhir pekan")


# 5. If Statements as Guards
# Guard adalah kondisi tambahan menggunakan if di dalam case

match nilai:
    case n if n >= 90:
        print("Nilai A")
    case n if n >= 80:
        print("Nilai B")
    case n if n >= 70:
        print("Nilai C")
    case _:
        print("Tidak lulus")


# 6. If Statements as Guards (Contoh Lain)
# Guard juga bisa digunakan untuk kondisi logika lain

match umur:
    case u if u >= 17:
        print("Boleh membuat KTP")
    case _:
        print("Belum boleh membuat KTP")
