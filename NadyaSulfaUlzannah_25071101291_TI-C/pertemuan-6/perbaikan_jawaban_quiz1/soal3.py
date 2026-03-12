buku = [
    ["Algoritma", 2000],
    ["Basis Data", 3000],
    ["Aljabar Linear", 2500],
    ["Kalkulus", 3500],
    ["Logika Matematika", 1500]
]

pinjaman = []

print("Daftar Buku:")
for i in range(len(buku)):
    print(i+1, ".", buku[i][0], "- Denda per hari: Rp", buku[i][1])

print("\nPilih buku yang ingin dipinjam (0 untuk selesai)")

while True:
    pilih = int(input("Masukkan nomor buku: "))

    if pilih == 0:
        break
    elif pilih >= 1 and pilih <= len(buku):
        pinjaman.append(buku[pilih-1])
        print("Buku berhasil ditambahkan")
    else:
        print("Nomor tidak valid")

terlambat = int(input("\nMasukkan jumlah hari keterlambatan: "))

while terlambat < 0:
    print("Error! Hari tidak boleh negatif")
    terlambat = int(input("Masukkan jumlah hari keterlambatan: "))

if terlambat == 0:
    print("Tidak ada denda")

else:
    total_denda = 0

    print("\nDaftar Buku yang Dipinjam dan Perhitungan Denda:")

    for i in range(len(pinjaman)):
        judul = pinjaman[i][0]
        denda_per_hari = pinjaman[i][1]
        denda = denda_per_hari * terlambat

        print(i+1, ".", judul)
        print("   Denda:", denda_per_hari, "x", terlambat, "=", denda)

        total_denda += denda

    print("\nTotal denda Anda: Rp", total_denda)