buku = [
    ["Algoritma", 2000],
    ["Basis Data", 3000],
    ["Aljabar Linear", 2500],
    ["Kalkulus", 3500],
    ["Logika Matematika", 1500]
]

for i in range (len(buku)):
    judul = buku[i][0]
    denda = buku[i][1]
    print(i+1, ".", judul, "-", denda)

pinjaman = []

while True:
    pilihan = int(input("Pilih daftar atau judul buku (input 0 untuk selesai): "))

    if pilihan == 0:
        break
    elif pilihan >=1 and pilihan <= len(buku):
        jumlah = int(input("Jumlah buku: "))
        pilihan_buku = buku[pilihan-1][0]
        denda_buku = buku[pilihan-1][1]
        pinjaman.append([pilihan_buku, jumlah, denda_buku])
    else:
        print("Daftar buku tidak tersedia")

total = 0

for j in pinjaman:
    subtotal = j[1] * j[2]
    total = total + subtotal
    judul_buku = j[0]
    jumlah = j[1]
    print(pilihan_buku, "x", jumlah, "=", subtotal)

print("Total denda = ", total)

hari_keterlambatan = int(input("Masukkan berapa hari keterlambatan : "))
denda = int(input("Masukkan denda buku yang di pinjam (lihat dari daftar judul buku) : "))

while hari_keterlambatan < 0:
    print("Error! input ulang")

total_denda = denda * hari_keterlambatan

print("Total hari keterlambatan : ", hari_keterlambatan)
print("Total denda yang harus di bayar : ", total_denda)

if total_denda == 0:
    print("Tidak ada denda")
else:
    print("Total denda anda : Rp", total_denda)