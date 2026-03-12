buku = [
    ["Algoritma", 2000],
    ["Basis Data", 3000],
    ["Aljabar Linear", 2500],
    ["Kalkulus", 3500],
    ["Logika Matematika", 1500]
]

pinjaman = []

print("Daftar Buku ")
for i in range(len(buku)):
    print(i+1, ".", buku[i][0], "- Denda per hari: Rp", buku[i][1])

print("\nMasukkan nomor buku yang ingin dipinjam (0 untuk selesai)")

while True:
    pilih = int(input("Pilih nomor buku: "))
    
    if pilih == 0:
        break
    elif pilih >= 1 and pilih <= len(buku):
        hari = int(input("Lama pinjam (hari): "))

        judul = buku[pilih-1][0]
        denda = buku[pilih-1][1]
        pinjaman.append([judul, hari, denda])
        
        print("Buku berhasil ditambahkan\n")
    else:
        print("Nomor buku tidak valid!\n")

print("\nDaftar Buku yang Dipinjam:")
total_denda = 0

for i in range(len(pinjaman)):
    print(i+1, ".", pinjaman[i][0], "- Lama pinjam:", pinjaman[i][1], "hari")
    total_denda += pinjaman[i][2]

print("\nTotal estimasi denda jika semua buku terlambat 1 hari: Rp", total_denda)