import os

while True:

    print("\n========================")
    print("PYTHON FILE MANAGER V1.0")
    print("==========================")
    print("[1] Read File")
    print("[2] Write File")
    print("[3] Delete File")
    print("[0] Exit")

    menu = input("Pilih menu: ")

    files = [f for f in os.listdir() if f.endswith(".txt")]

    # READ
    if menu == "1":

        if not files:
            print("Tidak ada file .txt ditemukan.")
            continue

        for i, f in enumerate(files, 1):
            print(f"[{i}] {f}")

        try:
            pilih = int(input("Pilih file: "))
            file = open(files[pilih - 1], "r")
            print(file.read())
            file.close()

        except:
            print("Terjadi kesalahan.")

    # WRITE
    elif menu == "2":

        nama = input("Nama file: ")

        if not nama.endswith(".txt"):
            nama += ".txt"

        isi = input("Isi file: ")

        try:
            file = open(nama, "w")
            file.write(isi)
            file.close()

            print("File berhasil disimpan.")

        except:
            print("Gagal menulis file.")

    # DELETE
    elif menu == "3":

        if not files:
            print("Tidak ada file .txt ditemukan.")
            continue

        for i, f in enumerate(files, 1):
            print(f"[{i}] {f}")

        try:
            pilih = int(input("Pilih file: "))
            konfirmasi = input("Yakin hapus? (y/n): ")

            if konfirmasi.lower() == "y":
                os.remove(files[pilih - 1])
                print("File berhasil dihapus.")

        except:
            print("Terjadi kesalahan.")

    # EXIT
    elif menu == "0":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid.")