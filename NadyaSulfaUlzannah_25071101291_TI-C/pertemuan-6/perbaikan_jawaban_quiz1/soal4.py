# input jumlah minggu dan kategori buku
minggu = int(input("Masukkan jumlah minggu: "))
kategori = int(input("Masukkan jumlah kategori buku: "))

# membuat matriks kosong
data = []

# input data peminjaman
for i in range(minggu):
    baris = []
    print("\nMinggu ke-", i+1)
    
    for j in range(kategori):
        jumlah = int(input("Jumlah buku kategori ke-" + str(j+1) + ": "))
        baris.append(jumlah)
    
    data.append(baris)

# menampilkan matriks
print("\nData Peminjaman Buku:")
for i in range(minggu):
    for j in range(kategori):
        print(data[i][j], end="\t")
    print()

# total peminjaman per minggu
print("\nTotal peminjaman per minggu:")
for i in range(minggu):
    total = 0
    for j in range(kategori):
        total += data[i][j]
    print("Minggu", i+1, "=", total)

# total peminjaman per kategori
print("\nTotal peminjaman per kategori:")
for j in range(kategori):
    total = 0
    for i in range(minggu):
        total += data[i][j]
    print("Kategori", j+1, "=", total)