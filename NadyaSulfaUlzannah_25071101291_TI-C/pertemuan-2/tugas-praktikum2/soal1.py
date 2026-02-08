def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    return sum(nilai) / len(nilai)

data_nilai = [80, 75, 90, 60, 85]
hasil = rata_rata(data_nilai)

print("Rata-rata =", hasil)