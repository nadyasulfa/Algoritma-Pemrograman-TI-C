# =========================================
# UTS PRAKTIKUM ALGORITMA PEMROGRAMAN
# GAME SUIT (BATU - GUNTING - KERTAS)
# =========================================

# Data pilihan komputer (tanpa random, pakai urutan)
PILIHAN = ["batu", "gunting", "kertas"]

# === BAGIAN A ===

def input_pemain():
    """Fungsi untuk mengambil input pemain dengan validasi."""
    while True:
        pilihan = input("Pilih (batu/gunting/kertas): ").lower()
        if pilihan in PILIHAN:
            return pilihan
        else:
            print("Input tidak valid!")


def tentukan_hasil(pemain, lawan):
    """Fungsi untuk menentukan hasil pertandingan."""
    if pemain == lawan:
        return "Seri"
    elif (pemain == "batu" and lawan == "gunting") or \
         (pemain == "gunting" and lawan == "kertas") or \
         (pemain == "kertas" and lawan == "batu"):
        return "Menang"
    else:
        return "Kalah"


def hitung_skor(hasil):
    """Fungsi untuk menghitung skor berdasarkan hasil."""
    if hasil == "Menang":
        return 10
    elif hasil == "Seri":
        return 5
    else:
        return 0


def main_satu_ronde(nama, ronde):
    """Fungsi untuk menjalankan satu ronde permainan."""
    print("\n=== Ronde", ronde + 1, "===")

    pemain = input_pemain()
    lawan = PILIHAN[ronde % len(PILIHAN)]

    print("Pilihan lawan:", lawan)

    hasil = tentukan_hasil(pemain, lawan)
    print("Hasil:", hasil)

    skor = hitung_skor(hasil)
    print("Skor:", skor)

    return [nama, skor]


# === BAGIAN B ===

def tampilkan_riwayat(riwayat):
    """Fungsi untuk menampilkan riwayat permainan."""
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
        return

    print("\n=== RIWAYAT ===")
    print("No\t Nama\tSkor")

    for i in range(len(riwayat)):
        print(i+1, "\t", riwayat[i][0], "\t", riwayat[i][1])


# === BAGIAN C ===

def bubble_sort_riwayat(riwayat):
    """Mengurutkan riwayat dengan Bubble Sort (descending)."""
    hasil = []
    for item in riwayat:
        hasil.append(item)

    n = len(hasil)

    for i in range(n):
        for j in range(0, n - i - 1):
            if hasil[j][1] < hasil[j+1][1]:
                hasil[j], hasil[j+1] = hasil[j+1], hasil[j]

    return hasil


def tampilkan_leaderboard(riwayat):
    """Menampilkan leaderboard."""
    if len(riwayat) == 0:
        print("Belum ada data.")
        return

    urut = bubble_sort_riwayat(riwayat)

    print("\n=== LEADERBOARD ===")
    print("Rank\t Nama\tSkor")

    for i in range(len(urut)):
        tanda = ""
        if i == 0:
            tanda = " *"

        print(i+1, "\t", urut[i][0], "\t", urut[i][1], tanda)


# === PROGRAM UTAMA ===

def main():
    """Fungsi utama program."""
    riwayat = []
    ronde = 0
    maks_ronde = 5

    nama = input("Masukkan nama pemain: ")

    while ronde < maks_ronde:
        print("\nSisa permainan:", maks_ronde - ronde)

        hasil = main_satu_ronde(nama, ronde)
        riwayat.append(hasil)

        ronde += 1

        # Kalau masih ada kesempatan, tanya lanjut
        if ronde < maks_ronde:
            ulang = input("Main lagi? (y/n): ")
            if ulang.lower() != 'y':
                break
        else:
            print("\nKesempatan bermain sudah habis!")

    tampilkan_riwayat(riwayat)
    tampilkan_leaderboard(riwayat)
    

# Jalankan program
main()