struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
    "Bab_2": {
        "landasan_teori.docx": 118,
        "referensi": {
            "paper_A.pdf": 340,
            "paper_B.pdf": 210
        }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def total_ukuran(folder: dict) -> int:
    total = 0
    for item in folder.values():
        if type(item) == int:   
            total += item
        else:                  
            total += total_ukuran(item)
    return total

def hitung_file(folder: dict) -> int:
    jumlah = 0
    for item in folder.values():
        if type(item) == int:
            jumlah += 1
        else:
            jumlah += hitung_file(item)
    return jumlah

def cari_terbesar(folder: dict) -> tuple[str, int]:
    nama_file_terbesar = ""
    ukuran_terbesar = 0

    for nama, item in folder.items():
        if type(item) == int:
            if item > ukuran_terbesar:
                nama_file_terbesar = nama
                ukuran_terbesar = item
        else:
            n, u = cari_terbesar(item)
            if u > ukuran_terbesar:
                nama_file_terbesar = n
                ukuran_terbesar = u

    return nama_file_terbesar, ukuran_terbesar

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0) -> None:
    print("  " * level + "📁 " + nama)

    for key, item in folder.items():
        if type(item) == int:
            print("  " * (level + 1) + f"📄 {key} ({item} KB)")
        else:
            tampilkan_tree(item, key, level + 1)

print("Total ukuran:", total_ukuran(struktur), "KB")
print("Jumlah file:", hitung_file(struktur), "file")

nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)")

tampilkan_tree(struktur, "Skripsi_Aqil")