# =========================================
# UJIAN TENGAH SEMESTER
# PRAKTIKUM ALGORITMA PEMROGRAMAN
# =========================================

# Data angka yang sudah disediakan
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

# === BAGIAN A ===

def tebak_angka(angka_rahasia, maks_percobaan):
    """Fungsi untuk menjalankan proses tebak angka."""
    sisa_percobaan = maks_percobaan

    while sisa_percobaan > 0:
        tebakan = int(input("Masukkan tebakan Anda: "))

        if tebakan < angka_rahasia:
            print("Terlalu kecil")
        elif tebakan > angka_rahasia:
            print("Terlalu besar")
        else:
            print("Benar!")
            return True, sisa_percobaan

        sisa_percobaan -= 1
        print("Sisa percobaan:", sisa_percobaan)

    print("Kesempatan habis! Angka rahasia adalah", angka_rahasia)
    return False, 0


def hitung_skor(berhasil, sisa_percobaan):
    """Fungsi untuk menghitung skor pemain."""
    if berhasil:
        return sisa_percobaan * 10
    else:
        return 0


def main_satu_ronde(nama, nomor_ronde):
    """Fungsi untuk menjalankan satu ronde permainan."""
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]

    print("\n=== Ronde", nomor_ronde + 1, "===")

    berhasil, sisa = tebak_angka(angka_rahasia, 7)
    skor = hitung_skor(berhasil, sisa)

    print("Skor ronde ini:", skor)

    return [nama, skor]


# === BAGIAN B ===

def tampilkan_riwayat(riwayat):
    """Fungsi untuk menampilkan riwayat permainan."""
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
        return

    print("\n=== RIWAYAT PERMAINAN ===")
    print("No\tNama\tSkor")

    for i in range(len(riwayat)):
        print(i + 1, "\t", riwayat[i][0], "\t", riwayat[i][1])


# === BAGIAN C ===

def selection_sort_riwayat(riwayat):
    """Fungsi untuk mengurutkan riwayat berdasarkan skor (descending)."""
    # Salinan list agar data asli tidak berubah
    hasil = []
    for item in riwayat:
        hasil.append(item)

    n = len(hasil)

    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if hasil[j][1] > hasil[max_index][1]:
                max_index = j

        # Tukar posisi
        hasil[i], hasil[max_index] = hasil[max_index], hasil[i]

    return hasil


def tampilkan_leaderboard(riwayat):
    """Fungsi untuk menampilkan leaderboard."""
    if len(riwayat) == 0:
        print("Belum ada data leaderboard.")
        return

    urut = selection_sort_riwayat(riwayat)

    print("\n=== LEADERBOARD ===")
    print("Rank\tNama\tSkor")

    for i in range(len(urut)):
        tanda = ""
        if i == 0:
            tanda = " *"

        print(i + 1, "\t", urut[i][0], "\t", urut[i][1], tanda)


# === PROGRAM UTAMA ===

def main():
    """Fungsi utama program."""
    riwayat = []
    nomor_ronde = 0

    nama = input("Masukkan nama pemain: ")
    
    while True:
        hasil = main_satu_ronde(nama, nomor_ronde)
        riwayat.append(hasil)
    
        nomor_ronde += 1

        ulang = input("Ingin bermain lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

    tampilkan_riwayat(riwayat)
    tampilkan_leaderboard(riwayat)


# Menjalankan program
main()