 # 1 #Inisialisasi matriks 3x4 dengan nilai 0
baris = 3                       # jumlah baris dalam matriks
kolom = 4                       # jumlah kolom dalam matriks

 #Cara 1:Menggunakan nestedloop
matriks = []                    # buat list kosong untuk menyimpan matriks
for i in range(baris):          # untuk setiap baris
    baris_baru = []             # buat list kosong untuk menyimpan elemen baris baru
    for j in range(kolom):      # untuk setiap kolom dalam baris
        baris_baru.append(0)    # tambahkan elemen 0 ke baris baru
    matriks.append(baris_baru)  # tambahkan baris baru ke matriks

print("1.1", matriks)
print("-" * 60)

#CARA 2 : MENGGUNAKAN LIST COMPERHENSION
matriks = [[0 for j in range(kolom)] for i in range(baris)]

print("1.2", matriks)
print("-" * 60)

# 2 #INISIALISASSI MATRIKS 3X3 DENGAN NILAI BERURUTAN
baris = 3
kolom = 3
nilai = 1
matriks = []

for i in range (baris):
    baris_baru = []
    for j in range(kolom):
        baris_baru.append(nilai)
        nilai +=1
    matriks.append(baris_baru)

print(matriks)
print("-" * 60)

# 3 #PROGRAM MEMBACA MATRIKS DARI KEYBOARD(INPUT MANUAL)
baris = int(input("Masukkan jumlah baris:"))
kolom = int(input("Masukkan jumlah kolom:"))
matriks = []

print("Masukkan elemen matriks {baris} x {kolom}:")

for i in range(baris):
    baris_baru = []
    for j in range(kolom):
        nilai = int(input(f"Elemen [{i}][{j}]:"))
        baris_baru.append(nilai)
    matriks.append(baris_baru)

print("Matriks berhasil terbaca")
print("-" * 60)

# 4 #Input tiap baris sekaligus, dipisah spasi
baris = int(input('Jumlah baris: '))
kolom =int(input('Jumlah kolom: '))
matriks = []

for i in range(baris):
    print(f'Masukkan baris ke-{i+1} ({kolom} angka, pisah spasi):')
    data = list(map(int, input().split()))
    matriks.append(data)
print(matriks)
print("-" * 60)

# 5 #CETAK MATRIKS
matriks = [
    [1,2,3],
    [4,5,6]
]

for i in range(len(matriks)):
    for j in range(len(matriks[0])):
        print(matriks[i][j], end="")
    print()
print("-" * 60)

# 6 #MENGAKSES ELEMEN MATRIKS
matriks = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

# Akses elemen tunggal
print(matriks[0][0]) # Output: 1 (baris 0, kolom 0)
print(matriks[1][2]) # Output: 6 (baris 1, kolom 2)
print(matriks[2][1]) # Output: 8 (baris 2, kolom 1)

# Akses seluruh baris
print(matriks[0]) # Output: [1, 2, 3]
# Akses seluruh kolom (misal kolom 1)
# menggunakanlist comprehension untuk mengambil elemen kolom 1 dari setiap baris
kolom_1 = [matriks[i][1] for i in range(len(matriks))]
print(kolom_1)
# Output: [2, 5, 8]
# Akses ukuran matriks
print('Baris:', len(matriks))
# Output: 3
print('Kolom:', len(matriks[0])) # Output: 3
print("-" * 60)

# 8 #MENJUMLAHKAN DUA BUAH MATRIKS
baris = 2
kolom = 2

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

C = [[0 for j in range(kolom)] for i in range(baris)]  #buat matriks C dengan ukuran yang sama

for i in range(baris):
    for j in range(kolom):
        C[i][j] = A[i][j] + B[i][j]

for row in C: # Menampilkan hasil penjumlahan matriks C
    print(baris)

print("-" * 60)

# 9 #MATRIKS TRANSPOSE
A = [[1,2,3],
[4,5,6]]

rows = len(A)
cols = len(A[0])

T = [[0 for i in range(rows)] for j in range(cols)]
for i in range(rows):
    for j in range(cols):
        T[j][i] = A[i][j]
for row in T:
    print(row)

print("-" * 60)

# 10 #MENENTUKAN ELEMEN TERBESAR DALAM MATRIKS
A = [[1,2,3],
     [4,5,6]]

max = A[0][0]
for i in A:
    for j in i:
        if j > max:
            j = max
print(max)
print("-" * 60)

# 11 #menghitung total semua elemen
A =[[2,1,4],
    [6,4,8]]

total = 0
for i in A:
    total = total + sum(i)
print(total)
print("-" * 60)