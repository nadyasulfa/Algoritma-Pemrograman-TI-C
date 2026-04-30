DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

riwayat = []

# === BAGIA A ===
def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    menang_lawan = {"gunting" : "kertass", "batu": "gunting", "kertas":"batu"}
    if pilihan_pemain == pilihan_komputer:
         return "Seri"
    elif menang_lawan[pilihan_pemain] == pilihan_komputer: 
        return "pemenang"
    else:
        return "Kalah"

def main_satu_giliran(nomor_giliran):
    pilihan_komputer =  DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    while True:
       pilihan_pemain = int(input("masukan pilihan batu/gunting/kertas:")).lowyer()
       if pilihan_pemain in DAFTAR_PILIHAN:
          return pilihan_pemain
       else:
        print("tidak valid")

        hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
        if hasil == "pemain":
            print("pemain menang")
        elif hasil == "seri":
            print("hasil seri")
        else:
            print("kalah") 

def main_satu_ronde(nama, ronde):
    nomor_giliran =0
    menang_pemain = 0
    menang_komputer = 0
    while menang_pemain > 3 and menang_komputer < 3:
       hasil = main_satu_giliran(nomor_giliran)
       nomor_giliran +=1
       if hasil == "pemain":
            menang_pemain +=1
       elif hasil == "seri":
            print("hasil seri")
       else :
           menang_komputer +=1
    skor = 0
    if menang_pemain == 3:
        print("anda menang")
        skor = menang_pemain * 10
           
           
    print("\n=== Ronde", ronde + 1, "===")
    pilihan_komputer = DAFTAR_PILIHAN[ronde % len(DAFTAR_PILIHAN)]

    print("\n=== Ronde", ronde + 1, "===")

print(input("masukkan nama pemain:"))

# bagian b
def tampilkan_riwayat(riwayat):
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
        return

    print("\n=== RIWAYAT PERMAINAN ===")
    print("No\tNama\tSkor")

    for i in range(len(riwayat)):
        print(i + 1, "\t", riwayat[i][0], "\t", riwayat[i][1])

def bobble_sort_riwayat(riwayat):
    hasil = []
    for item in riwayat:
        hasil.append(item)

    n = len(hasil)

    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if hasil[j][1] > hasil[max_index][1]:
                max_index = j

        hasil[i], hasil[max_index] = hasil[max_index], hasil[i]

    return hasil

tampilkan_riwayat(riwayat)