buku = [
    ["Algoritma", 2000],
    ["Basis Data", 3000],
    ["Aljabar Linear", 2500],
    ["Kalkulus", 3500],
    ["Logika Matematika", 1500]
]

print("DAFTAR BUKU")
for i in range (len(buku)):
    judul = buku[i][0]
    denda = buku[i][1]
    print(i+1, ".", judul, "-", denda)

pilihan = int(input("Pilih judul atau daftar buku yang ingin di pinjam : "))

if pilihan >= 1 and pilihan <= len(buku):
    pilihan_buku = buku[pilihan -1][0]
    denda_buku = buku[pilihan -1][1]
    print("Daftar atau judul buku yang dipilih : ", pilihan_buku)
    print("Denda yang per hari : ", denda_buku)
else:
    print("Error! nomor tidak valid")